/**
 * @namespace Sk
 *
 */

// this is stored into sys specially, rather than created by sys
Sk.sysmodules = new Sk.builtin.dict([]);
Sk.realsyspath = undefined;

/**
 * @param {string} name to look for
 * @param {string} ext extension to use (.py or .js)
 * @param {Object=} searchPath an iterable set of path strings
 */
Sk.importSearchPathForName = function(name, ext, searchPath) {
  var fn;
  var j;
  var fns = [];
  var nameAsPath = name.replace(/\./g, "/");
  var it, i;

  var tryPathAndBreakOnSuccess = function(filename, packagePath) {
    return Sk.misceval.chain(
      Sk.misceval.tryCatch(
        function() {
          // https://all-dream.com/pythonWeb/pages/moodle/lesson/
          if (
            filename.indexOf(".py") > 0 &&
            filename.indexOf(
              "/lesson/"
            ) >= 0
          ) {
            if (filename.indexOf("__init__.py") > 0) {
              return undefined;
            }
            var request = new XMLHttpRequest();
            request.open("GET", filename, false);
            request.send(null);
            if (request.status === 200) {
              return request.responseText;
            }
            return undefined;
          } else {
            // console.log('Sk.importSearchPathForName', filename, Sk.read(filename));
            return Sk.read(filename);
          }
        },
        function(e) {
          /* Exceptions signal "not found" */
        }
      ),
      function(code) {
        if (code !== undefined) {
          // console.log('Sk.importSearchPathForName', filename, code);
          // This will cause the iterFor() to return the specified value
          return new Sk.misceval.Break({
            filename: filename,
            code: code,
            packagePath: packagePath
          });
        }
      }
    );
  };

  if (searchPath === undefined) {
    searchPath = Sk.realsyspath;
  }

  return Sk.misceval.iterFor(searchPath.tp$iter(), function(pathStr) {
    // For each element of path, try loading the module, and if that
    // doesn't work, try the corresponding package.
    return Sk.misceval.chain(
      tryPathAndBreakOnSuccess(pathStr.v + "/" + nameAsPath + ext, false), // module
      function(r) {
        // console.log('Sk.importSearchPathForName',nameAsPath, r);
        return r
          ? r
          : tryPathAndBreakOnSuccess(
              pathStr.v + "/" + nameAsPath + "/__init__" + ext,
              pathStr.v + "/" + nameAsPath
            ); // package
      }
    );
  });
};

/**
 * Complete any initialization of Python classes which relies on internal
 * dependencies.
 *
 * This includes making Python classes subclassable and ensuring that the
 * {@link Sk.builtin.object} magic methods are wrapped inside Python functions.
 *
 * @return {undefined}
 */
Sk.doOneTimeInitialization = function(canSuspend) {
  var proto, name, i, x, func, typesWithFunctionsToWrap, builtin_type, j;

  // can't fill these out when making the type because tuple/dict aren't
  // defined yet.
  Sk.builtin.type.basesStr_ = new Sk.builtin.str("__bases__");
  Sk.builtin.type.mroStr_ = new Sk.builtin.str("__mro__");

  // Register a Python class with an internal dictionary, which allows it to
  // be subclassed
  var setUpClass = function(child) {
    var parent = child.tp$base;
    var bases = [];
    var base;

    for (base = parent; base !== undefined; base = base.tp$base) {
      bases.push(base);
    }

    child.tp$mro = new Sk.builtin.tuple([child]);
    if (!child.tp$base) {
      child.tp$base = bases[0];
    }
    child["$d"] = new Sk.builtin.dict([]);
    child["$d"].mp$ass_subscript(
      Sk.builtin.type.basesStr_,
      new Sk.builtin.tuple(bases)
    );
    child["$d"].mp$ass_subscript(Sk.builtin.type.mroStr_, child.tp$mro);
  };

  for (x in Sk.builtin) {
    func = Sk.builtin[x];
    if (
      (func.prototype instanceof Sk.builtin.object ||
        func === Sk.builtin.object) &&
      !func.sk$abstract
    ) {
      setUpClass(func);
    }
  }

  // Wrap the inner Javascript code of Sk.builtin.object's Python methods inside
  // Sk.builtin.func, as that class was undefined when these functions were declared
  typesWithFunctionsToWrap = [
    Sk.builtin.object,
    Sk.builtin.type,
    Sk.builtin.func,
    Sk.builtin.method
  ];

  for (i = 0; i < typesWithFunctionsToWrap.length; i++) {
    builtin_type = typesWithFunctionsToWrap[i];
    proto = builtin_type.prototype;
    for (j = 0; j < builtin_type.pythonFunctions.length; j++) {
      name = builtin_type.pythonFunctions[j];

      if (proto[name] instanceof Sk.builtin.func) {
        // If functions have already been initialized, do not wrap again.
        break;
      }

      proto[name].co_kwargs = null;
      proto[name] = new Sk.builtin.func(proto[name]);
    }
  }

  for (var file in Sk.internalPy.files) {
    var fileWithoutExtension = file.split(".")[0].split("/")[1];
    var mod = Sk.importBuiltinWithBody(
      fileWithoutExtension,
      false,
      Sk.internalPy.files[file],
      true
    );
    mod = Sk.misceval.retryOptionalSuspensionOrThrow(mod);
    Sk.asserts.assert(
      mod["$d"][fileWithoutExtension] !== undefined,
      "Should have imported name " + fileWithoutExtension
    );
    Sk.builtins[fileWithoutExtension] = mod["$d"][fileWithoutExtension];
  }
};

/**
 * currently only pull once from Sk.syspath. User might want to change
 * from js or from py.
 */
Sk.importSetUpPath = function(canSuspend) {
  var i;
  var paths;
  if (!Sk.realsyspath) {
    paths = [
      new Sk.builtin.str("src/builtin"),
      new Sk.builtin.str("src/lib"),
      new Sk.builtin.str("./lesson"),
      new Sk.builtin.str(".")
    ];
    for (i = 0; i < Sk.syspath.length; ++i) {
      paths.push(new Sk.builtin.str(Sk.syspath[i]));
    }
    Sk.realsyspath = new Sk.builtin.list(paths);

    Sk.doOneTimeInitialization(canSuspend);
  }
};

/**
 * @param {string} name name of module to import
 * @param {boolean=} dumpJS whether to output the generated js code
 * @param {string=} modname what to call the module after it's imported if
 * it's to be renamed (i.e. __main__)
 * @param {string=} suppliedPyBody use as the body of the text for the module
 * rather than Sk.read'ing it.
 * @param {Object=} relativeToPackage perform import relative to this package
 * @param {boolean=} returnUndefinedOnTopLevelNotFound return 'undefined' rather than throwing ImportError if the *first* load failed
 * @param {boolean=} canSuspend whether we may return a Suspension object
 */
Sk.importModuleInternal_ = function(
  name,
  dumpJS,
  modname,
  suppliedPyBody,
  relativeToPackage,
  returnUndefinedOnTopLevelNotFound,
  canSuspend
) {
  //dumpJS = true;
  var filename;
  var prev;
  var parentModName;
  var parentModule;
  var modNameSplit;
  var ret;
  var module;
  var topLevelModuleToReturn = null;
  var relativePackageName =
    relativeToPackage !== undefined
      ? relativeToPackage.tp$getattr(Sk.builtin.str.$name)
      : undefined;
  var absolutePackagePrefix =
    relativePackageName !== undefined ? relativePackageName.v + "." : "";
  var searchPath =
    relativeToPackage !== undefined
      ? relativeToPackage.tp$getattr(Sk.builtin.str.$path)
      : undefined;
  Sk.importSetUpPath(canSuspend);

  if (relativeToPackage && !relativePackageName) {
    if (returnUndefinedOnTopLevelNotFound) {
      return undefined;
    } else {
      throw new Sk.builtin.ValueError(
        "Attempted to import relative to invalid package (no name)"
      );
    }
  }

  // if no module name override, supplied, use default name
  if (modname === undefined) {
    modname = absolutePackagePrefix + name;
  }

  modNameSplit = name.split(".");

  // if leaf is already in sys.modules, early out
  try {
    prev = Sk.sysmodules.mp$subscript(modname);
    // if we're a dotted module, return the top level, otherwise ourselves
    if (modNameSplit.length > 1) {
      return Sk.sysmodules.mp$subscript(
        absolutePackagePrefix + modNameSplit[0]
      );
    } else {
      return prev;
    }
  } catch (x) {
    // not in sys.modules, continue
  }

  if (modNameSplit.length > 1) {
    // if we're a module inside a package (i.e. a.b.c), then we'll need to return the
    // top-level package ('a'). recurse upwards on our parent, importing
    // all parent packages. so, here we're importing 'a.b', which will in
    // turn import 'a', and then return 'a' eventually.
    parentModName = modNameSplit.slice(0, modNameSplit.length - 1).join(".");
    topLevelModuleToReturn = Sk.importModuleInternal_(
      parentModName,
      dumpJS,
      undefined,
      undefined,
      relativeToPackage,
      returnUndefinedOnTopLevelNotFound,
      canSuspend
    );
  }

  ret = Sk.misceval.chain(
    topLevelModuleToReturn,
    function(topLevelModuleToReturn_) {
      var codeAndPath, co, googClosure;
      var searchFileName = name;
      var result;

      topLevelModuleToReturn = topLevelModuleToReturn_;

      // If we're inside a package, look search using its __path__
      if (modNameSplit.length > 1) {
        if (!topLevelModuleToReturn) {
          return undefined;
        }
        parentModule = Sk.sysmodules.mp$subscript(
          absolutePackagePrefix + parentModName
        );
        searchFileName = modNameSplit[modNameSplit.length - 1];
        searchPath = parentModule.tp$getattr(Sk.builtin.str.$path);
      }

      // otherwise:
      // - create module object
      // - add module object to sys.modules
      // - compile source to (function(){...});
      // - run module and set the module locals returned to the module __dict__
      module = new Sk.builtin.module();

      if (suppliedPyBody) {
        filename = name + ".py";
        co = Sk.compile(suppliedPyBody, filename, "exec", canSuspend);
      } else {
        co = Sk.misceval.chain(
          undefined,
          function() {
            // If an onBeforeImport method is supplied, call it and if
            // the result is false or a string, prevent the import.
            // This allows for a user to conditionally prevent the usage
            // of certain libraries.
            if (Sk.onBeforeImport && typeof Sk.onBeforeImport === "function") {
              return Sk.onBeforeImport(name);
            }

            return;
          },
          function(result) {
            if (result === false) {
              throw new Sk.builtin.ImportError(
                "Importing " + name + " is not allowed"
              );
            } else if (typeof result === "string") {
              throw new Sk.builtin.ImportError(result);
            }

            // Try loading as a builtin (i.e. already in JS) module, then try .py files
            return Sk.importSearchPathForName(
              searchFileName,
              ".js",
              searchPath
            );
          },
          function(codeAndPath) {
            if (codeAndPath) {
              return {
                funcname: "$builtinmodule",
                code: codeAndPath.code,
                filename: codeAndPath.filename,
                packagePath: codeAndPath.packagePath
              };
            } else {
              return Sk.misceval.chain(
                Sk.importSearchPathForName(searchFileName, ".py", searchPath),
                function(codeAndPath_) {
                  codeAndPath = codeAndPath_; // We'll want it in a moment
                  if (codeAndPath) {
                    // console.log('codeAndPath', codeAndPath.code, codeAndPath.filename);
                    return Sk.compile(
                      codeAndPath.code,
                      codeAndPath.filename,
                      "exec",
                      canSuspend
                    );
                  }
                },
                function(co) {
                  if (co) {
                    co.packagePath = codeAndPath.packagePath;
                    return co;
                  }
                }
              );
            }
          }
        );
      }
      return co;
    },
    function(co) {
      var finalcode;
      var withLineNumbers;
      var modscope;

      if (!co) {
        return undefined;
      }

      // Now we know this module exists, we can add it to the cache
      Sk.sysmodules.mp$ass_subscript(modname, module);

      module.$js = co.code; // todo; only in DEBUG?
      finalcode = co.code;

      if (filename == null) {
        filename = co.filename;
      }

      if (Sk.dateSet == null || !Sk.dateSet) {
        finalcode = "Sk.execStart = Sk.lastYield = new Date();\n" + co.code;
        Sk.dateSet = true;
      }

      // if (!COMPILED)
      // {
      if (dumpJS) {
        withLineNumbers = function(code) {
          var j;
          var pad;
          var width;
          var i;
          var beaut = Sk.js_beautify(code);
          var lines = beaut.split("\n");
          for (i = 1; i <= lines.length; ++i) {
            width = ("" + i).length;
            pad = "";
            for (j = width; j < 5; ++j) {
              pad += " ";
            }
            lines[i - 1] = "/* " + pad + i + " */ " + lines[i - 1];
          }
          return lines.join("\n");
        };
        finalcode = withLineNumbers(finalcode);
        Sk.debugout(finalcode);
      }
      // }

      finalcode += "\n" + co.funcname + ";";

      modscope = Sk.global["eval"](finalcode);

      module["$d"] = {
        __name__: new Sk.builtin.str(modname),
        __doc__: Sk.builtin.none.none$,
        __package__: co.packagePath
          ? new Sk.builtin.str(modname)
          : parentModName
          ? new Sk.builtin.str(absolutePackagePrefix + parentModName)
          : relativePackageName
          ? relativePackageName
          : Sk.builtin.none.none$
      };
      if (co.packagePath) {
        module["$d"]["__path__"] = new Sk.builtin.tuple([
          new Sk.builtin.str(co.packagePath)
        ]);
      }

      return modscope(module["$d"]);
    },
    function(modlocs) {
      var i;

      if (modlocs === undefined) {
        if (returnUndefinedOnTopLevelNotFound && !topLevelModuleToReturn) {
          return undefined;
        } else {
          //  尝试加载本地py文件
          throw new Sk.builtin.ImportError("No module named " + name);
        }
      }

      // Some builtin modules replace their globals entirely.
      // For their benefit, we copy over any of the standard
      // dunder-values they didn't supply.
      if (modlocs !== module["$d"]) {
        for (i in module["$d"]) {
          if (!modlocs[i]) {
            modlocs[i] = module["$d"][i];
          }
        }
        module["$d"] = modlocs;
      }

      // If an onAfterImport method is defined on the global Sk
      // then call it now after a library has been successfully imported
      // and compiled.
      if (Sk.onAfterImport && typeof Sk.onAfterImport === "function") {
        try {
          Sk.onAfterImport(name);
        } catch (e) {}
      }

      if (topLevelModuleToReturn) {
        // if we were a dotted name, then we want to return the top-most
        // package. we store ourselves into our parent as an attribute
        parentModule.tp$setattr(
          new Sk.builtin.str(modNameSplit[modNameSplit.length - 1]),
          module
        );
        //print("import returning parent module, modname", modname, "__name__", toReturn.tp$getattr("__name__").v);
        return topLevelModuleToReturn;
      }

      if (relativeToPackage) {
        relativeToPackage.tp$setattr(new Sk.builtin.str(name), module);
      }

      //print("name", name, "modname", modname, "returning leaf");
      // otherwise we return the actual module that we just imported
      return module;
    }
  );

  return canSuspend ? ret : Sk.misceval.retryOptionalSuspensionOrThrow(ret);
};

/**
 * @param {string} name the module name
 * @param {boolean=} dumpJS print out the js code after compilation for debugging
 * @param {boolean=} canSuspend can this function suspend and return a Suspension object?
 */
Sk.importModule = function(name, dumpJS, canSuspend) {
  return Sk.importModuleInternal_(
    name,
    dumpJS,
    undefined,
    undefined,
    undefined,
    false,
    canSuspend
  );
};

Sk.importMain = function(name, dumpJS, canSuspend) {
  Sk.dateSet = false;
  Sk.filesLoaded = false;
  // Added to reset imports
  Sk.sysmodules = new Sk.builtin.dict([]);
  Sk.realsyspath = undefined;

  Sk.resetCompiler();

  return Sk.importModuleInternal_(
    name,
    dumpJS,
    "__main__",
    undefined,
    undefined,
    false,
    canSuspend
  );
};

/**
 * **Run Python Code in Skulpt**
 *
 * When you want to hand Skulpt a string corresponding to a Python program this is the function.
 *
 * @param name {string}  File name to use for messages related to this run
 * @param dumpJS {boolean} print out the compiled javascript
 * @param body {string} Python Code
 * @param canSuspend {boolean}  Use Suspensions for async execution
 *
 */
Sk.importMainWithBody = function(name, dumpJS, body, canSuspend) {
  Sk.dateSet = false;
  Sk.filesLoaded = false;
  // Added to reset imports
  Sk.sysmodules = new Sk.builtin.dict([]);
  Sk.realsyspath = undefined;

  Sk.resetCompiler();

  return Sk.importModuleInternal_(
    name,
    dumpJS,
    "__main__",
    body,
    undefined,
    false,
    canSuspend
  );
};

/**
 * Imports internal python files into the `__builtin__` module. Used during startup
 * to compile and import all *.py files from the src/ directory.
 *
 * @param name {string}  File name to use for messages related to this run
 * @param dumpJS {boolean} print out the compiled javascript
 * @param body {string} Python Code
 * @param canSuspend {boolean}  Use Suspensions for async execution
 *
 */
Sk.importBuiltinWithBody = function(name, dumpJS, body, canSuspend) {
  return Sk.importModuleInternal_(
    name,
    dumpJS,
    "__builtin__." + name,
    body,
    undefined,
    false,
    canSuspend
  );
};

Sk.builtin.__import__ = function(name, globals, locals, fromlist, level) {
  //print("Importing: ", JSON.stringify(name), JSON.stringify(fromlist), level);
  //if (name == "") { debugger; }

  // Save the Sk.globals variable importModuleInternal_ may replace it when it compiles
  // a Python language module.
  var saveSk = Sk.globals;

  // This might be a relative import, so first we get hold of the module object
  // representing this module's package (so we can search its __path__).
  // module.__package__ contains its name, so we use that to look it up in sys.modules.

  var relativeToPackage;
  var relativeToPackageName;
  var relativeToPackageNames;

  if (level === undefined) {
    level = Sk.__future__.absolute_import ? 0 : -1;
  }

  if (
    level !== 0 &&
    globals["__package__"] &&
    globals["__package__"] !== Sk.builtin.none.none$
  ) {
    relativeToPackageName = globals["__package__"].v;
    if (relativeToPackageName && level > 0) {
      // Trim <level> packages off the end
      relativeToPackageNames = relativeToPackageName.split(".");
      if (level - 1 >= relativeToPackageNames.length) {
        throw new Sk.builtin.ValueError(
          "Attempted relative import beyond toplevel package"
        );
      }
      relativeToPackageNames.length -= level - 1;
      relativeToPackageName = relativeToPackageNames.join(".");
    }
    try {
      relativeToPackage = Sk.sysmodules.mp$subscript(relativeToPackageName);
    } catch (e) {
      relativeToPackageName = undefined;
    }
  }

  if (level > 0 && relativeToPackage === undefined) {
    throw new Sk.builtin.ValueError("Attempted relative import in non-package");
  }

  var dottedName = name.split(".");
  var firstDottedName = dottedName[0];

  return Sk.misceval.chain(
    undefined,
    function() {
      // Attempt local load first (and just fall through to global
      // case if level == -1 and we fail to load the top-level package)
      if (level !== 0 && relativeToPackage !== undefined) {
        if (name === "") {
          // "from .. import ..."
          return relativeToPackage;
        } else {
          return Sk.importModuleInternal_(
            name,
            undefined,
            relativeToPackageName + "." + name,
            undefined,
            relativeToPackage,
            level == -1,
            true
          );
        }
      }
    },
    function(ret) {
      if (ret === undefined) {
        // Either it was always a global import, or it was an
        // either-way import that just fell through.
        relativeToPackage = undefined;
        relativeToPackageName = undefined;
        // console.log('builtin.__import__ 1', name, level);
        return Sk.importModuleInternal_(
          name,
          undefined,
          undefined,
          undefined,
          undefined,
          false,
          true
        );
      } else {
        return ret;
      }
    },
    function(ret) {
      // We might also have to load modules named by the fromlist.
      // If there is no fromlist, we have reached the end of the lookup, return
      if (!fromlist || fromlist.length === 0) {
        return ret;
      } else {
        // try to load from-names as modules from the file system
        // if they are not present on the module itself
        var i;
        var fromName;
        var leafModule;
        var importChain;

        leafModule = Sk.sysmodules.mp$subscript(
          (relativeToPackageName || "") +
            (relativeToPackageName && name ? "." : "") +
            name
        );

        for (i = 0; i < fromlist.length; i++) {
          fromName = fromlist[i];

          // "ret" is the module we're importing from
          // Only import from file system if we have not found the fromName in the current module
          if (
            fromName != "*" &&
            leafModule.tp$getattr(new Sk.builtin.str(fromName)) === undefined
          ) {
            // console.log('builtin.__import__ 2', name, fromName, leafModule);
            importChain = Sk.misceval.chain(
              importChain,
              Sk.importModuleInternal_.bind(
                null,
                fromName,
                undefined,
                undefined,
                undefined,
                leafModule,
                true,
                true
              )
            );
          }
        }

        return Sk.misceval.chain(importChain, function() {
          // if there's a fromlist we want to return the leaf module
          // (ret), not the toplevel namespace
          Sk.asserts.assert(leafModule);
          return leafModule;
        });
      }
    },
    function(ret) {
      if (saveSk !== Sk.globals) {
        Sk.globals = saveSk;
      }
      return ret;
    }
  );
};

Sk.importStar = function(module, loc, global) {
  var __all__ = module.tp$getattr(new Sk.builtin.str("__all__"));

  if (__all__) {
    // TODO this does not support naming *modules* in __all__,
    // only variables
    for (
      let it = Sk.abstr.iter(__all__), i = it.tp$iternext();
      i !== undefined;
      i = it.tp$iternext()
    ) {
      loc[i.v] = Sk.abstr.gattr(module, i);
    }
  } else {
    let props = Object["getOwnPropertyNames"](module["$d"]);
    for (let i in props) {
      if (props[i].charAt(0) != "_") {
        loc[props[i]] = module["$d"][props[i]];
      }
    }
  }
};

Sk.exportSymbol("Sk.importMain", Sk.importMain);
Sk.exportSymbol("Sk.importMainWithBody", Sk.importMainWithBody);
Sk.exportSymbol("Sk.importBuiltinWithBody", Sk.importBuiltinWithBody);
Sk.exportSymbol("Sk.builtin.__import__", Sk.builtin.__import__);
Sk.exportSymbol("Sk.importStar", Sk.importStar);
