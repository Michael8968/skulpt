/**
 * @constructor
 * @param {Array.<Object>} L
 */
Sk.builtin.dict = function dict (L) {
    var v;
    var it, k;
    var i;
    if (!(this instanceof Sk.builtin.dict)) {
        return new Sk.builtin.dict(L);
    }


    if (L === undefined) {
        L = [];
    }

    this.size = 0;
    this.buckets = {};

    if (Object.prototype.toString.apply(L) === "[object Array]") {
        // Handle dictionary literals
        for (i = 0; i < L.length; i += 2) {
            this.mp$ass_subscript(L[i], L[i + 1]);
        }
    } else if (L instanceof Sk.builtin.dict) {
        // Handle calls of type "dict(mapping)" from Python code
        for (it = Sk.abstr.iter(L), k = it.tp$iternext();
            k !== undefined;
            k = it.tp$iternext()) {
            v = L.mp$subscript(k);
            if (v === undefined) {
                //print(k, "had undefined v");
                v = null;
            }
            this.mp$ass_subscript(k, v);
        }
    } else if (Sk.builtin.checkIterable(L)) {
        // Handle calls of type "dict(iterable)" from Python code
        for (it = Sk.abstr.iter(L), i = it.tp$iternext(); i !== undefined; i = it.tp$iternext()) {
            if (i.mp$subscript) {
                this.mp$ass_subscript(i.mp$subscript(0), i.mp$subscript(1));
            } else {
                throw new Sk.builtin.TypeError("element " + this.size + " is not a sequence");
            }
        }
    } else {
        throw new Sk.builtin.TypeError("object is not iterable");
    }

    this.__class__ = Sk.builtin.dict;
    this.tp$call = undefined; // Not callable, even though constructor is

    return this;
};

Sk.builtin.dict.tp$call = function(args, kw) {
    var d, i;
    Sk.builtin.pyCheckArgsLen("dict", args, 0, 1);
    d = new Sk.builtin.dict(args[0]);
    if (kw) {
        for (i = 0; i < kw.length; i += 2) {
            d.mp$ass_subscript(new Sk.builtin.str(kw[i]), kw[i+1]);
        }
    }
    return d;
};

Sk.abstr.setUpInheritance("dict", Sk.builtin.dict, Sk.builtin.object);
Sk.abstr.markUnhashable(Sk.builtin.dict);

var kf = Sk.builtin.hash;

Sk.builtin.dict.prototype.key$lookup = function (bucket, key) {
    var item;
    var eq;
    var i;

    // Fast path: We spend a *lot* of time looking up strings
    // in dictionaries. (Every attribute access, for starters.)
    if (key.ob$type === Sk.builtin.str) {
        for (i = 0; i < bucket.items.length; i++) {
            item = bucket.items[i];
            if (item.lhs.ob$type === Sk.builtin.str && item.lhs.v === key.v) {
                return item;
            }
        }
        return null;
    }

    for (i = 0; i < bucket.items.length; i++) {
        item = bucket.items[i];
        eq = Sk.misceval.richCompareBool(item.lhs, key, "Eq");
        if (eq) {
            return item;
        }
    }

    return null;
};

Sk.builtin.dict.prototype.key$pop = function (bucket, key) {
    var item;
    var eq;
    var i;

    for (i = 0; i < bucket.items.length; i++) {
        item = bucket.items[i];
        eq = Sk.misceval.richCompareBool(item.lhs, key, "Eq");
        if (eq) {
            bucket.items.splice(i, 1);
            this.size -= 1;
            return item;
        }
    }
    return undefined;
};

// Perform dictionary lookup, either return value or undefined if key not in dictionary
Sk.builtin.dict.prototype.mp$lookup = function (key) {
    var k = kf(key);
    var bucket = this.buckets[k.v];
    var item;

    // todo; does this need to go through mp$ma_lookup

    if (bucket !== undefined) {
        item = this.key$lookup(bucket, key);
        if (item) {
            return item.rhs;
        }
    }

    // Not found in dictionary
    return undefined;
};

Sk.builtin.dict.prototype.mp$subscript = function (key) {
    Sk.builtin.pyCheckArgsLen("[]", arguments.length, 1, 2, false, false);
    var s;
    var res = this.mp$lookup(key);

    if (res !== undefined) {
        // Found in dictionary
        return res;
    } else {
        // Not found in dictionary
        s = new Sk.builtin.str(key);
        throw new Sk.builtin.KeyError(s.v);
    }
};

Sk.builtin.dict.prototype.sq$contains = function (ob) {
    var res = this.mp$lookup(ob);

    return (res !== undefined);
};

Sk.builtin.dict.prototype.mp$ass_subscript = function (key, w) {
    var k = kf(key);
    var bucket = this.buckets[k.v];
    var item;

    if (bucket === undefined) {
        // New bucket
        bucket = {$hash: k, items: [
            {lhs: key, rhs: w}
        ]};
        this.buckets[k.v] = bucket;
        this.size += 1;
        return;
    }

    item = this.key$lookup(bucket, key);
    if (item) {
        item.rhs = w;
        return;
    }

    // Not found in dictionary
    bucket.items.push({lhs: key, rhs: w});
    this.size += 1;
};

Sk.builtin.dict.prototype.mp$del_subscript = function (key) {
    Sk.builtin.pyCheckArgsLen("del", arguments.length, 1, 1, false, false);
    var k = kf(key);
    var bucket = this.buckets[k.v];
    var item;
    var s;

    // todo; does this need to go through mp$ma_lookup

    if (bucket !== undefined) {
        item = this.key$pop(bucket, key);
        if (item !== undefined) {
            return;
        }
    }

    // Not found in dictionary
    s = new Sk.builtin.str(key);
    throw new Sk.builtin.KeyError(s.v);
};

Sk.builtin.dict.prototype["$r"] = function () {
    var v;
    var iter, k;
    var ret = [];
    for (iter = Sk.abstr.iter(this), k = iter.tp$iternext();
        k !== undefined;
        k = iter.tp$iternext()) {
        v = this.mp$subscript(k);
        if (v === undefined) {
            //print(k, "had undefined v");
            v = null;
        }

        // we need to check if value is same as object
        // otherwise it would cause an stack overflow
        if(v === this) {
            ret.push(Sk.misceval.objectRepr(k).v + ": {...}");
        } else {
            ret.push(Sk.misceval.objectRepr(k).v + ": " + Sk.misceval.objectRepr(v).v);
        }
    }
    return new Sk.builtin.str("{" + ret.join(", ") + "}");
};

Sk.builtin.dict.prototype.mp$length = function () {
    return this.size;
};

Sk.builtin.dict.prototype["get"] = new Sk.builtin.func(function (self, k, d) {
    Sk.builtin.pyCheckArgsLen("get()", arguments.length, 1, 2, false, true);
    var ret;

    if (d === undefined) {
        d = Sk.builtin.none.none$;
    }

    ret = self.mp$lookup(k);
    if (ret === undefined) {
        ret = d;
    }

    return ret;
});

Sk.builtin.dict.prototype["pop"] = new Sk.builtin.func(function (self, key, d) {
    Sk.builtin.pyCheckArgsLen("pop()", arguments.length, 1, 2, false, true);
    var k = kf(key);
    var bucket = self.buckets[k.v];
    var item;
    var s;

    // todo; does this need to go through mp$ma_lookup
    if (bucket !== undefined) {
        item = self.key$pop(bucket, key);
        if (item !== undefined) {
            return item.rhs;
        }
    }

    // Not found in dictionary
    if (d !== undefined) {
        return d;
    }

    s = new Sk.builtin.str(key);
    throw new Sk.builtin.KeyError(s.v);
});

Sk.builtin.dict.prototype["has_key"] = new Sk.builtin.func(function (self, k) {
    Sk.builtin.pyCheckArgsLen("has_key()", arguments.length, 1, 1, false, true);
    return new Sk.builtin.bool( self.sq$contains(k));
});

Sk.builtin.dict.prototype["items"] = new Sk.builtin.func(function (self) {
    Sk.builtin.pyCheckArgsLen("items()", arguments.length, 0, 0, false, true);
    var v;
    var iter, k;
    var ret = [];

    for (iter = Sk.abstr.iter(self), k = iter.tp$iternext();
        k !== undefined;
        k = iter.tp$iternext()) {
        v = self.mp$subscript(k);
        if (v === undefined) {
            //print(k, "had undefined v");
            v = null;
        }
        ret.push(new Sk.builtin.tuple([k, v]));
    }
    return new Sk.builtin.list(ret);
});

Sk.builtin.dict.prototype["keys"] = new Sk.builtin.func(function (self) {
    Sk.builtin.pyCheckArgsLen("keys()", arguments.length, 0, 0, false, true);
    var iter, k;
    var ret = [];

    for (iter = Sk.abstr.iter(self), k = iter.tp$iternext();
        k !== undefined;
        k = iter.tp$iternext()) {
        ret.push(k);
    }
    return new Sk.builtin.list(ret);
});

Sk.builtin.dict.prototype["values"] = new Sk.builtin.func(function (self) {
    Sk.builtin.pyCheckArgsLen("values()", arguments.length, 0, 0, false, true);
    var v;
    var iter, k;
    var ret = [];

    for (iter = Sk.abstr.iter(self), k = iter.tp$iternext();
        k !== undefined;
        k = iter.tp$iternext()) {
        v = self.mp$subscript(k);
        if (v === undefined) {
            v = null;
        }
        ret.push(v);
    }
    return new Sk.builtin.list(ret);
});

Sk.builtin.dict.prototype["clear"] = new Sk.builtin.func(function (self) {
    Sk.builtin.pyCheckArgsLen("clear()", arguments.length, 0, 0, false, true);
    var k;
    var iter;

    for (iter = Sk.abstr.iter(self), k = iter.tp$iternext();
        k !== undefined;
        k = iter.tp$iternext()) {
        self.mp$del_subscript(k);
    }
});

Sk.builtin.dict.prototype["setdefault"] = new Sk.builtin.func(function (self, key, default_) {
    try {
        return self.mp$subscript(key);
    } catch (e) {
        if (default_ === undefined) {
            default_ = Sk.builtin.none.none$;
        }
        self.mp$ass_subscript(key, default_);
        return default_;
    }
});

/*
    this function mimics the cpython implementation, which is also the reason for the
    almost similar code, this may be changed in future
*/
Sk.builtin.dict.prototype.dict_merge = function(b) {
    var iter;
    var k, v;
    if(b instanceof Sk.builtin.dict) {
        // fast way
        for (iter = b.tp$iter(), k = iter.tp$iternext(); k !== undefined; k = iter.tp$iternext()) {
            v = b.mp$subscript(k);
            if (v === undefined) {
                throw new Sk.builtin.AttributeError("cannot get item for key: " + k.v);
            }
            this.mp$ass_subscript(k, v);
        }
    } else {
        // generic slower way
        var keys = Sk.misceval.callsimArray(b["keys"], [b]);
        for (iter = Sk.abstr.iter(keys), k = iter.tp$iternext(); k !== undefined; k = iter.tp$iternext()) {
            v = b.tp$getitem(k); // get value
            if (v === undefined) {
                throw new Sk.builtin.AttributeError("cannot get item for key: " + k.v);
            }
            this.mp$ass_subscript(k, v);
        }
    }
};

/**
 *   update() accepts either another dictionary object or an iterable of key/value pairs (as tuples or other iterables of length two).
 *   If keyword arguments are specified, the dictionary is then updated with those key/value pairs: d.update(red=1, blue=2).
 *   https://hg.python.org/cpython/file/4ff865976bb9/Objects/dictobject.c
 */
var update_f = function (kwargs, self, other) {
    // case another dict or obj with keys and getitem has been provided
    if(other !== undefined && (other.tp$name === "dict" || other["keys"])) {
        self.dict_merge(other); // we merge with override
    } else if(other !== undefined && Sk.builtin.checkIterable(other)) {
        // 2nd case, we expect an iterable that contains another iterable of length 2
        var iter;
        var k, v;
        var seq_i = 0; // index of current sequence item
        for (iter = Sk.abstr.iter(other), k = iter.tp$iternext(); k !== undefined; k = iter.tp$iternext(), seq_i++) {
            // check if value is iter
            if (!Sk.builtin.checkIterable(k)) {
                throw new Sk.builtin.TypeError("cannot convert dictionary update sequence element #" + seq_i + " to a sequence");
            }

            // cpython impl. would transform iterable into sequence
            // we just call iternext twice if k has length of 2
            if(k.sq$length() === 2) {
                var k_iter = Sk.abstr.iter(k);
                var k_key = k_iter.tp$iternext();
                var k_value = k_iter.tp$iternext();
                self.mp$ass_subscript(k_key, k_value);
            } else {
                // throw exception
                throw new Sk.builtin.ValueError("dictionary update sequence element #" + seq_i + " has length " + k.sq$length() + "; 2 is required");
            }
        }
    } else if(other !== undefined) {
        // other is not a dict or iterable
        throw new Sk.builtin.TypeError("'" +Sk.abstr.typeName(other) + "' object is not iterable");
    }

    // apply all key/value pairs of kwargs
    // create here kwargs_dict, there could be exceptions in other cases before
    var kwargs_dict = new Sk.builtins.dict(kwargs);
    self.dict_merge(kwargs_dict);

    // returns none, when successful or throws exception
    return  Sk.builtin.none.none$;
};

update_f.co_kwargs = true;
Sk.builtin.dict.prototype.update = new Sk.builtin.func(update_f);

Sk.builtin.dict.prototype.__contains__ = new Sk.builtin.func(function (self, item) {
    Sk.builtin.pyCheckArgsLen("__contains__", arguments.length, 2, 2);
    return new Sk.builtin.bool(self.sq$contains(item));
});

Sk.builtin.dict.prototype.__cmp__ = new Sk.builtin.func(function (self, other, op) {
    // __cmp__ cannot be supported until dict lt/le/gt/ge operations are supported
    return Sk.builtin.NotImplemented.NotImplemented$;
});

Sk.builtin.dict.prototype.__delitem__ = new Sk.builtin.func(function (self, item) {
    Sk.builtin.pyCheckArgsLen("__delitem__", arguments.length, 1, 1, false, true);
    return Sk.builtin.dict.prototype.mp$del_subscript.call(self, item);
});

Sk.builtin.dict.prototype.__getitem__ = new Sk.builtin.func(function (self, item) {
    Sk.builtin.pyCheckArgsLen("__getitem__", arguments.length, 1, 1, false, true);
    return Sk.builtin.dict.prototype.mp$subscript.call(self, item);
});

Sk.builtin.dict.prototype.__setitem__ = new Sk.builtin.func(function (self, item, value) {
    Sk.builtin.pyCheckArgsLen("__setitem__", arguments.length, 2, 2, false, true);
    return Sk.builtin.dict.prototype.mp$ass_subscript.call(self, item, value);
});

Sk.builtin.dict.prototype.__hash__ = new Sk.builtin.func(function (self) {
    Sk.builtin.pyCheckArgsLen("__hash__", arguments.length, 0, 0, false, true);
    return Sk.builtin.dict.prototype.tp$hash.call(self);
});

Sk.builtin.dict.prototype.__len__ = new Sk.builtin.func(function (self) {
    Sk.builtin.pyCheckArgsLen("__len__", arguments.length, 0, 0, false, true);
    return Sk.builtin.dict.prototype.mp$length.call(self);
});

Sk.builtin.dict.prototype.__getattribute__ = new Sk.builtin.func(function (self, attr) {
    Sk.builtin.pyCheckArgsLen("__getattribute__", arguments.length, 1, 1, false, true);
    if (!Sk.builtin.checkString(attr)) { throw new Sk.builtin.TypeError("__getattribute__ requires a string"); }
    return Sk.builtin.dict.prototype.tp$getattr.call(self, attr);
});

Sk.builtin.dict.prototype.__iter__ = new Sk.builtin.func(function (self) {
    Sk.builtin.pyCheckArgsLen("__iter__", arguments.length, 0, 0, false, true);

    return new Sk.builtin.dict_iter_(self);
});

Sk.builtin.dict.prototype.tp$iter = function () {
    return new Sk.builtin.dict_iter_(this);
};

Sk.builtin.dict.prototype.__repr__ = new Sk.builtin.func(function (self) {
    Sk.builtin.pyCheckArgsLen("__repr__", arguments.length, 0, 0, false, true);
    return Sk.builtin.dict.prototype["$r"].call(self);
});

/* python3 recommends implementing simple ops */
Sk.builtin.dict.prototype.ob$eq = function (other) {

    var iter, k, v, otherv;

    if (this === other) {
        return Sk.builtin.bool.true$;
    }

    if (!(other instanceof Sk.builtin.dict)) {
        return Sk.builtin.NotImplemented.NotImplemented$;
    }

    if (this.size !== other.size) {
        return Sk.builtin.bool.false$;
    }

    for (iter = this.tp$iter(), k = iter.tp$iternext();
        k !== undefined;
        k = iter.tp$iternext()) {
        v = this.mp$subscript(k);
        otherv = other.mp$subscript(k);

        if (!Sk.misceval.richCompareBool(v, otherv, "Eq")) {
            return Sk.builtin.bool.false$;
        }
    }

    return Sk.builtin.bool.true$;
};

Sk.builtin.dict.prototype.ob$ne = function (other) {

    var isEqual = this.ob$eq(other);

    if (isEqual instanceof Sk.builtin.NotImplemented) {
        return isEqual;
    } else if (isEqual.v) {
        return Sk.builtin.bool.false$;
    } else {
        return Sk.builtin.bool.true$;
    }

};

Sk.builtin.dict.prototype["copy"] = new Sk.builtin.func(function (self) {
    Sk.builtin.pyCheckArgsLen("copy", arguments.length, 0, 0, false, true);

    var it; // Iterator
    var k; // Key of dict item
    var v; // Value of dict item
    var newCopy = new Sk.builtin.dict([]);

    for (it = Sk.abstr.iter(self), k = it.tp$iternext();
        k !== undefined;
        k = it.tp$iternext()) {
        v = self.mp$subscript(k);
        if (v === undefined) {
            v = null;
        }
        newCopy.mp$ass_subscript(k, v);
    }

    return newCopy;
});

Sk.builtin.dict.$fromkeys = function fromkeys(self, seq, value) {
    var k, iter, val, res, iterable;

    if (self instanceof Sk.builtin.dict) {
        // instance call
        Sk.builtin.pyCheckArgsLen("fromkeys", arguments.length, 1, 2, false, true);

        res = self;
        iterable = seq;
        val = value === undefined ? Sk.builtin.none.none$ : value;
    } else {
        // static call
        Sk.builtin.pyCheckArgsLen("fromkeys", arguments.length, 1, 2, false, false);

        res = new Sk.builtin.dict([]);
        iterable = self;
        val = seq === undefined ? Sk.builtin.none.none$ : seq;
    }

    if (!Sk.builtin.checkIterable(iterable)) {
        throw new Sk.builtin.TypeError("'" + Sk.abstr.typeName(iterable) + "' object is not iterable");
    }

    for (iter = Sk.abstr.iter(iterable), k = iter.tp$iternext();
        k !== undefined;
        k = iter.tp$iternext()) {
        res.mp$ass_subscript(k, val);
    }

    return res;
};

Sk.builtin.dict.prototype._internalGenericGetAttr = Sk.builtin.object.prototype.GenericGetAttr;

Sk.builtin.dict.prototype.tp$getattr = function (name) {
    if (name != null && (Sk.builtin.checkString(name) || typeof name === "string")) {
        var _name = name;

        // get javascript string
        if (Sk.builtin.checkString(name)) {
            _name = Sk.ffi.remapToJs(name);
        }        // buckets -> 106 -> items -> lhs.v / rhs.v
        if (_name === "x" || _name === "y") {
            var iter, k, items, value;
            var ret = [];

            for (iter = Sk.abstr.iter(this), k = iter.tp$iternext();
                k !== undefined;
                k = iter.tp$iternext()) {
                ret.push(k);
            }
            // console.log("Sk.builtin.dict.prototype.tp$getattr", ret, _name);
            if (_name === "x") {
                value = this.mp$lookup(ret[0]);
                return value;
            } else if (_name === "y") {
                value = this.mp$lookup(ret[1]);
                return value;
            }
        }
    }

    // if we have not returned yet, try the genericgetattr
    return this._internalGenericGetAttr(name);
};

Sk.builtin.dict.prototype["iteritems"] = new Sk.builtin.func(function (self) {
    throw new Sk.builtin.NotImplementedError("dict.iteritems is not yet implemented in Skulpt");
});

Sk.builtin.dict.prototype["iterkeys"] = new Sk.builtin.func(function (self) {
    throw new Sk.builtin.NotImplementedError("dict.iterkeys is not yet implemented in Skulpt");
});

Sk.builtin.dict.prototype["itervalues"] = new Sk.builtin.func(function (self) {
    throw new Sk.builtin.NotImplementedError("dict.itervalues is not yet implemented in Skulpt");
});

Sk.builtin.dict.prototype["popitem"] = new Sk.builtin.func(function (self) {
    throw new Sk.builtin.NotImplementedError("dict.popitem is not yet implemented in Skulpt");
});

Sk.builtin.dict.prototype["viewitems"] = new Sk.builtin.func(function (self) {
    throw new Sk.builtin.NotImplementedError("dict.viewitems is not yet implemented in Skulpt");
});

Sk.builtin.dict.prototype["viewkeys"] = new Sk.builtin.func(function (self) {
    throw new Sk.builtin.NotImplementedError("dict.viewkeys is not yet implemented in Skulpt");
});

Sk.builtin.dict.prototype["viewvalues"] = new Sk.builtin.func(function (self) {
    throw new Sk.builtin.NotImplementedError("dict.viewvalues is not yet implemented in Skulpt");
});

Sk.exportSymbol("Sk.builtin.dict", Sk.builtin.dict);

/**
 * @constructor
 * @param {Object} obj
 */
Sk.builtin.dict_iter_ = function (obj) {
    var k, i, bucket, allkeys, buckets;
    if (!(this instanceof Sk.builtin.dict_iter_)) {
        return new Sk.builtin.dict_iter_(obj);
    }
    this.$index = 0;
    this.$obj = obj;
    allkeys = [];
    buckets = obj.buckets;
    for (k in buckets) {
        if (buckets.hasOwnProperty(k)) {
            bucket = buckets[k];
            if (bucket && bucket.$hash !== undefined && bucket.items !== undefined) {
                // skip internal stuff. todo; merge pyobj and this
                for (i = 0; i < bucket.items.length; i++) {
                    allkeys.push(bucket.items[i].lhs);
                }
            }
        }
    }
    this.$keys = allkeys;
    this.tp$iter = this;
    this.tp$iternext = function () {
        // todo; StopIteration
        if (this.$index >= this.$keys.length) {
            return undefined;
        }
        return this.$keys[this.$index++];
        // return this.$obj[this.$keys[this.$index++]].lhs;
    };
    this.$r = function () {
        return new Sk.builtin.str("dictionary-keyiterator");
    };
    return this;
};

Sk.abstr.setUpInheritance("dictionary-keyiterator", Sk.builtin.dict_iter_, Sk.builtin.object);

Sk.builtin.dict_iter_.prototype.__class__ = Sk.builtin.dict_iter_;

Sk.builtin.dict_iter_.prototype.__iter__ = new Sk.builtin.func(function (self) {
    return self;
});

Sk.builtin.dict_iter_.prototype.next$ = function (self) {
    var ret = self.tp$iternext();
    if (ret === undefined) {
        throw new Sk.builtin.StopIteration();
    }
    return ret;
};
