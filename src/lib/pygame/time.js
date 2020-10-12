var $builtinmodule = function (name) {
    mod = {};
    mod.wait = new Sk.builtin.func(function (amount) {
        var t_m = Sk.importModule("time", false, true);
        var sec = Sk.ffi.remapToJs(amount) / 1000;
        return Sk.misceval.callsimOrSuspend(t_m.$d['sleep'], Sk.ffi.remapToPy(sec));
    });

    mod.get_ticks = new Sk.builtin.func(function () {
      if (PygameLib.initial_time > 0) {
        return Sk.ffi.remapToPy((new Date()).getTime() - PygameLib.initial_time);
      } else {
        return Sk.ffi.remapToPy(0);
      }
    });
    mod.delay = new Sk.builtin.func(function (amount) {
        var t_m = Sk.importModule("time", false, false);
        var sec = Sk.ffi.remapToJs(amount) / 1000;
        return Sk.misceval.callsimOrSuspend(t_m.$d['sleep'], Sk.ffi.remapToPy(sec));
    });
    mod.set_timer = new Sk.builtin.func(function (eventid, milliseconds) {
        var event = Sk.ffi.remapToJs(eventid);
        var ms = Sk.ffi.remapToJs(milliseconds);
        if (PygameLib.eventTimer[event]) {
            clearInterval(PygameLib.eventTimer[event].timer);
        }
        else {
            PygameLib.eventTimer[event] = {};
            PygameLib.eventTimer[event].f = function () {
                var e = [event, {}];
                PygameLib.eventQueue.unshift(e);
            }
        }
        if (ms) {
            PygameLib.eventTimer[event].timer = setInterval(PygameLib.eventTimer[event].f, ms);
        }
        return mod;
    });

    mod.Clock = Sk.misceval.buildClass(mod, time_Clock, 'Clock', []);
    // mod.Clock = new Sk.builtin.func(time_Clock);
    PygameLib.ClockType = mod.Clock;
    return mod;
};

function time_Clock($gbl, $loc) {
    // // console.log('time_Clock', $gbl, $loc);
    $loc.__init__ = new Sk.builtin.func(function (self) {
        self['prevTime'] = Sk.builtin.none.none$;
        self['getTime'] = Sk.builtin.none.none$;
        self['rawTime'] = Sk.ffi.remapToPy(0);
        self['fpsArray'] = Sk.ffi.remapToPy([]);
        self['fpsIdx'] = Sk.ffi.remapToPy(0);
        return Sk.builtin.none.none$;
    }, $gbl);
    $loc.__init__.co_name = new Sk.builtins['str']('__init__');

    $loc.tick = new Sk.builtin.func(function (self, framerate) {

        var currTime = (new Date()).getTime();
        var mills = 0;
        if (Sk.ffi.remapToJs(self['prevTime']) !== null) {
            var prevTime = Sk.ffi.remapToJs(self['prevTime']);
            mills = (currTime - prevTime);
        }
        self['prevTime'] = Sk.ffi.remapToPy(currTime);
        self['getTime'] = Sk.ffi.remapToPy(mills);
        var arr = Sk.ffi.remapToJs(self['fpsArray']);
        var idx = Sk.ffi.remapToJs(self['fpsIdx']);
        if (arr.length < 10) {
            arr.push(mills);
        } else {
            arr[idx] = mills;
        }
        idx = (idx + 1) % 10;
        self['fpsArray'] = Sk.ffi.remapToPy(arr);
        self['fpsIdx'] = Sk.ffi.remapToPy(idx);
        if (framerate !== undefined) {
            var timeout = parseInt(1000 / Sk.ffi.remapToJs(framerate)) - mills;
            if (timeout <= 0) {timeout = 25;}
            //延迟 delaytime 毫秒
            // var susp = new Sk.misceval.Suspension();
            // susp.resume = function () {
            //     return Sk.builtin.none.none$;
            // }
            // susp.data = {
            //     type: "Sk.promise", promise: new Promise(function (resolve) {
            //         var f = function () {
            //             self['rawTime'] = Sk.ffi.remapToPy((new Date()).getTime() - currTime);
            //             resolve(mills);
            //         };
            //         // if (PygameLib.running) {
            //         //     Sk.setTimeout(f, timeout);
            //         // }
            //         Sk.setTimeout(f, timeout);
            //         // Sk.setTimeout(resolve, timeout);
            //     })
            // };
            // return susp;
            return new Sk.misceval.promiseToSuspension(
                new Promise(function (resolve) {
                    var f = function () {
                        self['rawTime'] = Sk.ffi.remapToPy((new Date()).getTime() - currTime);
                        resolve(mills);
                    };

                    if (PygameLib.running) {
                        Sk.setTimeout(f, timeout);
                    }
                }));
        }
        self['rawTime'] = Sk.ffi.remapToPy(Date.now() - currTime);
        return Sk.ffi.remapToPy(mills);
    }, $gbl);
    $loc.tick.co_name = new Sk.builtins['str']('tick');
    $loc.tick.co_varnames = ['framerate'];
    $loc.tick.$defaults = [Sk.ffi.remapToPy(0)];

    $loc.tick_busy_loop = new Sk.builtin.func(function (self, framerate) {
        var currTime = Date.now();
        var mills = 0;
        if (Sk.ffi.remapToJs(self['prevTime']) !== null) {
            var prevTime = Sk.ffi.remapToJs(self['prevTime']);
            mills = (currTime - prevTime);
        }
        self['prevTime'] = Sk.ffi.remapToPy(currTime);
        self['getTime'] = Sk.ffi.remapToPy(mills);

        if (framerate !== undefined) {
            var timeout = 1000 / Sk.ffi.remapToJs(framerate);
            return new Sk.misceval.promiseToSuspension(
                new Promise(function (resolve) {
                    var f = function () {
                        self['rawTime'] = Sk.ffi.remapToPy(Date.now() - currTime);
                        resolve(mills);
                    };
                    if (PygameLib.running) {
                        Sk.setTimeout(f, timeout);
                    }
                }));
        }
        self['rawTime'] = Sk.ffi.remapToPy(Date.now() - currTime);
        return Sk.ffi.remapToPy(mills);
    }, $gbl);
    $loc.tick_busy_loop.co_name = new Sk.builtins['str']('tick_busy_loop');
    $loc.tick_busy_loop.co_varnames = ['framerate'];
    $loc.tick_busy_loop.$defaults = [Sk.ffi.remapToPy(0)];

    $loc.get_time = new Sk.builtin.func(function (self) {
        return self['getTime'];
    });
    $loc.get_time.co_name = new Sk.builtins['str']('get_time');

    $loc.get_rawtime = new Sk.builtin.func(function (self) {
        return self['rawTime'];
    });
    $loc.get_rawtime.co_name = new Sk.builtins['str']('get_rawtime');

    $loc.get_fps = new Sk.builtin.func(function (self) {
        var arr = Sk.ffi.remapToJs(self['fpsArray']);
        if (arr.length < 10 || arr[0] === 0) {
            return Sk.ffi.remapToPy(0);
        }
        var sum = 0;
        for (var i = 0; i < 10; i++) {
            sum += arr[i];
        }
        return Sk.ffi.remapToPy(sum / 10);
    });
}

time_Clock.co_name = new Sk.builtins['str']('Clock');
