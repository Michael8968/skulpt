var $builtinmodule = function (name) {
    var mod = {};
    mod.get = new Sk.builtin.func(get_event);
    mod.EventType = Sk.misceval.buildClass(mod, event_EventType_f, "EventType", []);
    PygameLib.EventType = mod.EventType;
    mod.Event = new Sk.builtin.func(function (type, dict) {
        return Sk.misceval.callsim(mod.EventType, type, dict)
    });

    mod.wait = new Sk.builtin.func(function () {
        return new Sk.misceval.promiseToSuspension(new Promise(function (resolve) {
            var f = function () {
                if (PygameLib.eventQueue.length) {
                    var event = PygameLib.eventQueue.splice(0, 1)[0];
                    var type = Sk.ffi.remapToPy(event[0]);
                    var dictjs = event[1];
                    kvs = [];
                    for (k in dictjs) {
                        kvs.push(Sk.ffi.remapToPy(k));
                        kvs.push(Sk.ffi.remapToPy(dictjs[k]));
                    }
                    var dict = new Sk.builtin.dict(kvs);
                    var e = Sk.misceval.callsim(PygameLib.EventType, type, dict);
                    resolve(e);
                }
                else
                    {Sk.setTimeout(f, 10);}
            };

            Sk.setTimeout(f, 10);
        }));
    });
    mod.poll = mod.wait;
    return mod;
};

//pygame.event module
//pygame.event.get()
//get() -> Eventlist
//get(type) -> Eventlist
//get(typelist) -> Eventlist
var get_event = function (types) {
    Sk.builtin.pyCheckArgs('get_event', arguments, 0, 1, false, false);
    var list = [];
    var t, d;
    var types_js = types ? Sk.ffi.remapToJs(types) : [];
    var queue = types ? (Sk.abstr.typeName(types) == "list" ? PygameLib.eventQueue.filter(e => types_js.includes(e[0])) : PygameLib.eventQueue.filter(e => e[0] == types_js))
        : PygameLib.eventQueue;

    for (var i = 0; i < queue.length; i++) {
        var event = queue[i];
        var type = Sk.ffi.remapToPy(event[0]);
        var dictjs = event[1];
        kvs = [];
        for (k in dictjs) {
            kvs.push(Sk.ffi.remapToPy(k));
            kvs.push(Sk.ffi.remapToPy(dictjs[k]));
        }
        var dict = new Sk.builtin.dict(kvs);
        var e = Sk.misceval.callsim(PygameLib.EventType, type, dict);
        list.push(e);

        // var index = PygameLib.eventQueue.indexOf(queue[i]);
        // PygameLib.eventQueue = PygameLib.eventQueue.slice(index);
        // console.log('PygameLib.eventQueue', PygameLib.eventQueue);

    }
    queue.splice(0);
    return new Sk.builtin.list(list);
}

function event_EventType_f($gbl, $loc) {
    $loc.__init__ = new Sk.builtin.func(function (self, type, dict) {
        Sk.builtin.pyCheckArgs('__init__', arguments, 2, 3, false, false);
        dict = dict || new Sk.builtin.dict();
        self['dict'] = dict;
        self['type'] = type;
        dictjs = Sk.ffi.remapToJs(dict);
        for (k in dictjs) {
            self[k] = Sk.ffi.remapToPy(dictjs[k]);
        }
        // var typejs = Sk.ffi.remapToJs(self['type']);
        // // console.log('event_EventType_f', self['type'], typejs);
        return Sk.builtin.none.none$;
    });
    $loc.__init__.co_name = new Sk.builtins['str']('__init__');
    $loc.__init__.co_varnames = ['self', 'type', 'dict'];

    $loc.__repr__ = new Sk.builtin.func(function (self) {
        var dict = Sk.ffi.remapToJs(self['dict']);
        var type = Sk.ffi.remapToJs(self['type']);
        return Sk.ffi.remapToPy('<Event(' + type + ' ' + dict + ')>');
    });
    $loc.__repr__.co_name = new Sk.builtins['str']('__repr__');
    $loc.__repr__.co_varnames = ['self'];

    var type_getter = new Sk.builtin.func(function (self) {
        return self['type'];
    });
    var type_setter = new Sk.builtin.func(function (self, val) {
        self['type'] = val;
    });
    $loc.type = Sk.misceval.callsimOrSuspend(Sk.builtins.property, type_getter, type_setter);

    var key_getter = new Sk.builtin.func(function (self) {
        return self['key'];
    });
    var key_setter = new Sk.builtin.func(function (self, val) {
        self['key'] = val;
    });
    $loc.key = Sk.misceval.callsimOrSuspend(Sk.builtins.property, key_getter, key_setter);

    var pos_getter = new Sk.builtin.func(function (self) {
        return self['pos'];
    });
    var pos_setter = new Sk.builtin.func(function (self, val) {
        self['pos'] = val;
    });
    $loc.pos = Sk.misceval.callsimOrSuspend(Sk.builtins.property, pos_getter, pos_setter);

    var button_getter = new Sk.builtin.func(function (self) {
        return self['button'];
    });
    var button_setter = new Sk.builtin.func(function (self, val) {
        self['button'] = val;
    });
    $loc.button = Sk.misceval.callsimOrSuspend(Sk.builtins.property, button_getter, button_setter);
}
