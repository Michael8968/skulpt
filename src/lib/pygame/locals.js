var $builtinmodule = function (name) {
    mod = {};
    for (k in PygameLib.constants) {
        mod[k] = Sk.ffi.remapToPy(PygameLib.constants[k]);
    }
    mod.modifierStateChange = new Sk.builtin.func(function (eventtype, event) {
      let modifier = 0;

      const capsModifier = (e, m) => e.getModifierState('CapsLock') ? m + 8192 : m;

      let operator = (i,n) => modifier = (eventtype === 'keyup' ? (i, n) => i - n : (i, n) => i + n)(i,n);

      switch (event.code) {
      case 'ShiftLeft':    return capsModifier(event, operator(modifier, 1));
      case 'ShiftRight':   return capsModifier(event, operator(modifier, 2));
      case 'ControlRight': return capsModifier(event, operator(modifier, 64));
      case 'ControlLeft':  return capsModifier(event, operator(modifier, 128));
      case 'AltRight':     return capsModifier(event, operator(modifier, 256));
      case 'AltLeft':      return capsModifier(event, operator(modifier, 512));
      case 'MetaRight':    return capsModifier(event, operator(modifier, 1024));
      case 'MetaLeft':     return capsModifier(event, operator(modifier, 2048));
      default:             return capsModifier(event, modifier);
      }
    });

    mod.normalizeEventCode = new Sk.builtin.func(function (jsevent) {
      if (!jsevent.code) {
        let code = keyKeyCodeLocationCodeMap[[jsevent.key.toLowerCase(), jsevent.keyCode, jsevent.location].toString()];
        if (code) {
          jsevent.code = code;
        }
      }

      return jsevent;
    });

    mod.mapEvent = new Sk.builtin.func(function (eventtype, jsevent) {
      jsevent = normalizeEventCode(jsevent);
      return Sk.misceval.callsimOrSuspend(event().Event, Sk.ffi.remapToPy(typeMap[eventtype]), Sk.ffi.remapToPy({
        unicode: jsevent.key.length === 1 ? jsevent.key : '',
        key: keyMap[jsevent.code],
        scancode: scanCodeMap[jsevent.code] || 0,
        mod: modifierStateChange(eventtype, jsevent)
      }));
    });

    mod.resetModifier = new Sk.builtin.func(function () {
      modifier = 0;
    });

    return mod;
};
