Sk.builtin.str.$emptystr = new Sk.builtin.str("");

/**
 * Python bool True constant.
 * @type {Sk.builtin.bool}
 * @memberOf Sk.builtin.bool
 */
Sk.builtin.bool.true$ = /** @type {Sk.builtin.bool} */ (Object.create(Sk.builtin.bool.prototype, {v: {value: 1, enumerable: true}}));

/**
 * Python bool False constant.
 * @type {Sk.builtin.bool}
 * @memberOf Sk.builtin.bool
 */
Sk.builtin.bool.false$ = /** @type {Sk.builtin.bool} */ (Object.create(Sk.builtin.bool.prototype, {v: {value: 0, enumerable: true}}));

/* Constants used for kwargs */

// Sk.builtin.int_
Sk.builtin.int_.co_varnames = [ "number", "base" ];
Sk.builtin.int_.$defaults = [ 0, Sk.builtin.none.none$ ];

// Sk.builtin.lng
Sk.builtin.lng.co_varnames = [ "number", "base" ];
Sk.builtin.lng.$defaults = [ 0, Sk.builtin.none.none$ ];

// Sk.builtin.sorted
Sk.builtin.sorted.co_varnames = ["list", "cmp", "key", "reverse"];
Sk.builtin.sorted.$defaults = [Sk.builtin.none.none$, Sk.builtin.none.none$, Sk.builtin.bool.false$];

// Sk.builtin.dict.fromkeys
Sk.builtin.dict.$fromkeys.co_name = new Sk.builtin.str("fromkeys");
Sk.builtin.dict.prototype["fromkeys"] = new Sk.builtin.func(Sk.builtin.dict.$fromkeys);

// String constants
Sk.builtin.str.$empty = new Sk.builtin.str("");

Sk.builtin.str.$default_factory = new Sk.builtin.str("default_factory");
Sk.builtin.str.$imag = new Sk.builtin.str("imag");
Sk.builtin.str.$real = new Sk.builtin.str("real");

Sk.builtin.str.$abs = new Sk.builtin.str("__abs__");
Sk.builtin.str.$call = new Sk.builtin.str("__call__");
Sk.builtin.str.$cmp = new Sk.builtin.str("__cmp__");
Sk.builtin.str.$complex = new Sk.builtin.str("__complex__");
Sk.builtin.str.$contains = new Sk.builtin.str("__contains__");
Sk.builtin.str.$copy = new Sk.builtin.str("__copy__");
Sk.builtin.str.$dict = new Sk.builtin.str("__dict__");
Sk.builtin.str.$dir = new Sk.builtin.str("__dir__");
Sk.builtin.str.$enter = new Sk.builtin.str("__enter__");
Sk.builtin.str.$eq = new Sk.builtin.str("__eq__");
Sk.builtin.str.$exit = new Sk.builtin.str("__exit__");
Sk.builtin.str.$index = new Sk.builtin.str("__index__");
Sk.builtin.str.$init = new Sk.builtin.str("__init__");
Sk.builtin.str.$int_ = new Sk.builtin.str("__int__");
Sk.builtin.str.$iter = new Sk.builtin.str("__iter__");
Sk.builtin.str.$float_ = new Sk.builtin.str("__float__");
Sk.builtin.str.$format = new Sk.builtin.str("__format__");
Sk.builtin.str.$ge = new Sk.builtin.str("__ge__");
Sk.builtin.str.$getattr = new Sk.builtin.str("__getattr__");
Sk.builtin.str.$getattribute = new Sk.builtin.str("__getattribute__");
Sk.builtin.str.$getitem = new Sk.builtin.str("__getitem__");
Sk.builtin.str.$gt = new Sk.builtin.str("__gt__");
Sk.builtin.str.$le = new Sk.builtin.str("__le__");
Sk.builtin.str.$len = new Sk.builtin.str("__len__");
Sk.builtin.str.$lt = new Sk.builtin.str("__lt__");
Sk.builtin.str.$name = new Sk.builtin.str("__name__");
Sk.builtin.str.$ne = new Sk.builtin.str("__ne__");
Sk.builtin.str.$new = new Sk.builtin.str("__new__");
Sk.builtin.str.$next2 = new Sk.builtin.str("next");
Sk.builtin.str.$next3 = new Sk.builtin.str("__next__");
Sk.builtin.str.$path = new Sk.builtin.str("__path__");
Sk.builtin.str.$repr = new Sk.builtin.str("__repr__");
Sk.builtin.str.$reversed = new Sk.builtin.str("__reversed__");
Sk.builtin.str.$round = new Sk.builtin.str("__round__");
Sk.builtin.str.$setattr = new Sk.builtin.str("__setattr__");
Sk.builtin.str.$setitem = new Sk.builtin.str("__setitem__");
Sk.builtin.str.$str = new Sk.builtin.str("__str__");
Sk.builtin.str.$trunc = new Sk.builtin.str("__trunc__");
Sk.builtin.str.$write = new Sk.builtin.str("write");

Sk.misceval.op2method_ = {
    "Eq"   : Sk.builtin.str.$eq,
    "NotEq": Sk.builtin.str.$ne,
    "Gt"   : Sk.builtin.str.$gt,
    "GtE"  : Sk.builtin.str.$ge,
    "Lt"   : Sk.builtin.str.$lt,
    "LtE"  : Sk.builtin.str.$le
};

var builtinNames = [
    "int_",
    "lng",
    "sorted",
    "range",
    "round",
    "len",
    "min",
    "max",
    "sum",
    "zip",
    "abs",
    "fabs",
    "ord",
    "chr",
    "hex",
    "oct",
    "bin",
    "dir",
    "repr",
    "open",
    "isinstance",
    "hash",
    "getattr",
    "hasattr",
    "id",
    "map",
    "filter",
    "reduce",
    "sorted",
    "any",
    "all",
    "input",
    "raw_input",
    "setattr",
    "quit",
    "quit",
    "divmod",
    "format",
    "globals",
    "issubclass"
];

for (var i = 0; i < builtinNames.length; i++) {
    Sk.builtin[builtinNames[i]].co_name = new Sk.builtin.str(builtinNames[i]);
}

// for (var i = 0; i < builtinConstants.length; i++) {
//     Sk.builtin[builtinNames[i]].co_name = new Sk.builtin.str(builtinNames[i]);
// }
// // constants
// builtinConstants = {
//     'KEYDOWN': 2,
//     'KEYUP': 3,
//     'KMOD_ALT': 768,
//     'KMOD_CAPS': 8192,
//     'KMOD_CTRL': 192,
//     'KMOD_LALT': 256,
//     'KMOD_LCTRL': 64,
//     'KMOD_LMETA': 1024,
//     'KMOD_LSHIFT': 1,
//     'KMOD_META': 3072,
//     'KMOD_MODE': 16384,
//     'KMOD_NONE': 0,
//     'KMOD_NUM': 4096,
//     'KMOD_RALT': 512,
//     'KMOD_RCTRL': 128,
//     'KMOD_RMETA': 2048,
//     'KMOD_RSHIFT': 2,
//     'KMOD_SHIFT': 3,
//     'K_0': 48,
//     'K_1': 49,
//     'K_2': 50,
//     'K_3': 51,
//     'K_4': 52,
//     'K_5': 53,
//     'K_6': 54,
//     'K_7': 55,
//     'K_8': 56,
//     'K_9': 57,
//     'K_AMPERSAND': 38,
//     'K_ASTERISK': 42,
//     'K_AT': 64,
//     'K_BACKQUOTE': 96,
//     'K_BACKSLASH': 92,
//     'K_BACKSPACE': 8,
//     'K_BREAK': 318,
//     'K_CAPSLOCK': 301,
//     'K_CARET': 94,
//     'K_CLEAR': 12,
//     'K_COLON': 58,
//     'K_COMMA': 44,
//     'K_DELETE': 127,
//     'K_DOLLAR': 36,
//     'K_DOWN': 274,
//     'K_END': 279,
//     'K_EQUALS': 61,
//     'K_ESCAPE': 27,
//     'K_EURO': 321,
//     'K_EXCLAIM': 33,
//     'K_F1': 282,
//     'K_F10': 291,
//     'K_F11': 292,
//     'K_F12': 293,
//     'K_F13': 294,
//     'K_F14': 295,
//     'K_F15': 296,
//     'K_F2': 283,
//     'K_F3': 284,
//     'K_F4': 285,
//     'K_F5': 286,
//     'K_F6': 287,
//     'K_F7': 288,
//     'K_F8': 289,
//     'K_F9': 290,
//     'K_FIRST': 0,
//     'K_GREATER': 62,
//     'K_HASH': 35,
//     'K_HELP': 315,
//     'K_HOME': 278,
//     'K_INSERT': 277,
//     'K_KP0': 256,
//     'K_KP1': 257,
//     'K_KP2': 258,
//     'K_KP3': 259,
//     'K_KP4': 260,
//     'K_KP5': 261,
//     'K_KP6': 262,
//     'K_KP7': 263,
//     'K_KP8': 264,
//     'K_KP9': 265,
//     'K_KP_DIVIDE': 267,
//     'K_KP_ENTER': 271,
//     'K_KP_EQUALS': 272,
//     'K_KP_MINUS': 269,
//     'K_KP_MULTIPLY': 268,
//     'K_KP_PERIOD': 266,
//     'K_KP_PLUS': 270,
//     'K_LALT': 308,
//     'K_LAST': 323,
//     'K_LCTRL': 306,
//     'K_LEFT': 276,
//     'K_LEFTBRACKET': 91,
//     'K_LEFTPAREN': 40,
//     'K_LESS': 60,
//     'K_LMETA': 310,
//     'K_LSHIFT': 304,
//     'K_LSUPER': 311,
//     'K_MENU': 319,
//     'K_MINUS': 45,
//     'K_MODE': 313,
//     'K_NUMLOCK': 300,
//     'K_PAGEDOWN': 281,
//     'K_PAGEUP': 280,
//     'K_PAUSE': 19,
//     'K_PERIOD': 46,
//     'K_PLUS': 43,
//     'K_POWER': 320,
//     'K_PRINT': 316,
//     'K_QUESTION': 63,
//     'K_QUOTE': 39,
//     'K_QUOTEDBL': 34,
//     'K_RALT': 307,
//     'K_RCTRL': 305,
//     'K_RETURN': 13,
//     'K_RIGHT': 275,
//     'K_RIGHTBRACKET': 93,
//     'K_RIGHTPAREN': 41,
//     'K_RMETA': 309,
//     'K_RSHIFT': 303,
//     'K_RSUPER': 312,
//     'K_SCROLLOCK': 302,
//     'K_SEMICOLON': 59,
//     'K_SLASH': 47,
//     'K_SPACE': 32,
//     'K_SYSREQ': 317,
//     'K_TAB': 9,
//     'K_UNDERSCORE': 95,
//     'K_UNKNOWN': 0,
//     'K_UP': 273,
//     'K_a': 97,
//     'K_b': 98,
//     'K_c': 99,
//     'K_d': 100,
//     'K_e': 101,
//     'K_f': 102,
//     'K_g': 103,
//     'K_h': 104,
//     'K_i': 105,
//     'K_j': 106,
//     'K_k': 107,
//     'K_l': 108,
//     'K_m': 109,
//     'K_n': 110,
//     'K_o': 111,
//     'K_p': 112,
//     'K_q': 113,
//     'K_r': 114,
//     'K_s': 115,
//     'K_t': 116,
//     'K_u': 117,
//     'K_v': 118,
//     'K_w': 119,
//     'K_x': 120,
//     'K_y': 121,
//     'K_z': 122,
//     'LIL_ENDIAN': 1234,
//     'MOUSEBUTTONDOWN': 5,
//     'MOUSEBUTTONUP': 6,
//     'MOUSEMOTION': 4,
//     'NOEVENT': 0,
//     'NOFRAME': 32,
//     'NUMEVENTS': 32,
// }
