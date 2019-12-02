var $builtinmodule = function (name) {
  var mod = {};

  mod.system = new Sk.builtin.func(function (cmd) {
    Sk.builtin.pyCheckArgs("system", arguments, 1, 1);
    Sk.builtin.pyCheckType("cmd", "string", Sk.builtin.checkString(cmd));

    var value = Sk.ffi.remapToJs(cmd);
    if (value === 'cls' || value === 'clear') {
      $(document).trigger('sk.system.clear');
      return Sk.builtin.asnum$(0);
    }

    return new Sk.builtin.str('sh: ' + value + ': command not found.');
  });

  return mod;
};
