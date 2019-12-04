var globalScope = typeof window !== 'undefined' ? window : global;

var $builtinmodule = function (name) {
  mixer_locs.Sound = SoundClass(mixer_locs);
  mixer_locs.Sound.$isclass = true;
  mixer_locs.Channel = ChannelClass(mixer_locs);
  mixer_locs.Channel.$isclass = true;

  mixer_locs.music = makeModule(music(globalScope));
  return mixer_locs;
};

function isValid(o) {
    if (typeof(o) != 'undefined' && o != null) {
        return true;
    } else {
      return false
    };
}

function remapInner(obj) {
  if (typeof obj === 'function') {
    return function () {
      return remapInner(obj());
    };
  } else {
    var res = {};
    for (var x in obj) {
      if (obj[x].$isclass) {
        res[x] = obj[x];
        delete res[x].$isclass;
      } else {
        res[x] = Sk.ffi.remapToPy(obj[x]);
      }
    }
  }
  return res;
}

function makeModule(locs) {
  var smodule = new Sk.builtin.module();
  smodule.$d = remapInner(locs);
  return smodule;
}

var notImplemented = new Sk.builtin.func(function () {
    throw new Sk.builtin.NotImplementedError("Not yet implemented");
});
//构造事件对象
// function mixer() {
    // mixer_locs.Sound = SoundClass(mixer_locs);
    // mixer_locs.Sound.$isclass = true;
    // mixer_locs.Channel = ChannelClass(mixer_locs);
    // mixer_locs.Channel.$isclass = true;
    //
    // mixer_locs.music = makeModule(music(globalScope));
    // return mixer_locs;
// }

//====================== music ========================
var music = function (globalScope) {
    var soundJS = "";
    var _sound = null;
    var _num = 0;
    var _loops = 0;//循环次数

    return {
        __doc__: 'pygame播放背景音乐',
        __name__: 'pygame.mixer.music',
        __package__: Sk.builtin.none.none$,
        __PYGAMEinit__: notImplemented,
        //初始化显示模块
        load: function load(filename) {
            if (isValid(filename)) {
              soundJS = Sk.ffi.remapToJs(filename);
            }
            if (soundJS.length > 0) {
                _sound = document.createElement('audio');
                _sound.id = soundJS;
                // var Soundpath = Sk.GameGraphics.assets(soundJS);
                var Soundpath = Sk.audioPath + Sk.ffi.remapToJs(soundJS);
                _sound.setAttribute('src', Soundpath);
                _num = 0; //播放次数

                // window.audios.push(_sound);
            }
        },
        //播放背景乐文件
        play: function play(loops, start) {
            if (isValid(_sound)) {
                _loops = 0;
                if (isValid(loops)) {
                    _loops = Sk.ffi.remapToJs(loops);//播放次数
                }
                _sound.loop = false;
                _sound.load();
                _sound.play();
                _num++;
                _sound.onended = function () {//重复次数
                    if (_num <= _loops || _loops < 0) {
                        _sound.play();
                        _num++;
                    }
                };
            }
        },
        //重新开始背景乐
        rewind: function rewind() {
        },
        //停止背景乐播放
        stop: function stop() {
            if (isValid(_sound)) {
              _sound.pause();
            }
        },
        //继续背景乐播放
        unpause: function unpause() {
        },
        //音乐背景淡入
        fadeout: function fadeout(time) {
            if (isValid(_sound)) {
              _sound.pause();
            }
        },
        //设置音量
        set_volume: function set_volume(value) {
            if (isValid(_sound)) {
                if (isValid(value)) {
                  Volume = Sk.ffi.remapToJs(value);
                }
                _sound.volume = Volume;
                _sound.load();
            }
        },
        //获取音量
        get_volume: function get_volume() {
            var Volume = 0;
            if (isValid(_sound)) {
                Volume = _sound.volume;
            }
            return Sk.ffi.remapToPy(Volume);
        },
        //判断背景乐是否繁忙
        get_busy: function get_busy() {
        },
        //设置背景乐播放位置
        set_pos: function set_pos(pos) {
        },
        //获取背景乐播放位置
        get_pos: function get_pos(pos) {
        }
    };
};


//创建一个Sound类
var SoundClass = function (gbl) {
    return Sk.misceval.buildClass(gbl, sound$1, 'Sound', []);
};

//初始化Sound
var initSound = function (self, filename) {
    // console.log('initSound', filename);
    var soundJS = "";
    if (isValid(filename)) {
      soundJS = Sk.ffi.remapToJs(filename);
    }
    if (soundJS.length > 0) {
        self._sound = document.createElement('audio');
        self._sound.id = soundJS;
        // var Soundpath = Sk.GameGraphics.assets(Sk.audioPath+soundJS);
        var Soundpath = Sk.audioPath + Sk.ffi.remapToJs(soundJS);
        console.log('Soundpath', Soundpath);
        self._sound.setAttribute('src', Soundpath);
        self._num = 0; //播放次数

        // window.audios.push(self._sound);
    }
};
initSound.co_name = new Sk.builtins['str']('__init__');
initSound.co_varnames = ['self', 'filename'];

//开始播放声音
var play = function (self, loops, maxtime, fade_ms) {
    // Sk.builtin.pyCheckArgs('play', arguments, 0, 4, false, false);
    if (isValid(self._sound)) {
        self._loops = 0;
        if (isValid(loops)) {
            self._loops = Sk.ffi.remapToJs(loops);//播放次数
        }
        self._maxtime = 0;
        if (isValid(maxtime)) {
            self._maxtime = Sk.ffi.remapToJs(maxtime);//播放时长毫秒
        }
        self._sound.loop = false;
        self._sound.load();
        self._sound.play();
        self._num++;
        self._sound.onended = function () {//重复次数
            if (self._num <= self._loops || self._loops < 0) {
                self._sound.play();
                self._num++;
            }
        };
        //定时器
        if (self._maxtime > 0) {
            setTimeout(function () {
                self._sound.pause();
                console.log('pause', loops, maxtime, fade_ms);
            }, self._maxtime);
        }
    }
}

play.minArgs = 0;
play.co_name = new Sk.builtins['str']('play');
play.co_varnames = ['self', 'loops', 'maxtime', 'fade_ms'];
play.$defaults = [new Sk.builtin.int_(0), new Sk.builtin.int_(0), new Sk.builtin.int_(0)];

//结束播放声音
var stop = function (self) {
    if (isValid(self._sound)) {
      self._sound.pause();
    }
}

stop.co_name = new Sk.builtins['str']('stop');
stop.co_varnames = ['self'];

//淡出结束播放声音
var fadeout = function (self) {
    if (isValid(self._sound)) {
      self._sound.pause();
    }
}

fadeout.co_name = new Sk.builtins['str']('fadeout');
fadeout.co_varnames = ['self'];

//设置此声音的播放音量
var set_volume = function (self, value) {
    if (isValid(self._sound)) {
        if (isValid(value)) {
          Volume = Sk.ffi.remapToJs(value);
        }
        self._sound.volume = Volume;
        self._sound.load();
    }
}

set_volume.co_name = new Sk.builtins['str']('set_volume');
set_volume.co_varnames = ['self', 'value'];

//获取播放音量
var get_volume = function (self) {
    var Volume = 0;
    if (isValid(self._sound)) {
        Volume = self._sound.volume;
    }
    return Sk.ffi.remapToPy(Volume);
}

get_volume.co_name = new Sk.builtins['str']('get_volume');
get_volume.co_varnames = ['self'];

//计算此声音播放的次数
var get_num_channels = function (self) {
    return Sk.ffi.remapToPy(self._num);
}

get_num_channels.co_name = new Sk.builtins['str']('get_num_channels');
get_num_channels.co_varnames = ['self'];

var sound$1 = function $Sound$class_outer(gbl, loc) {
    loc.__init__ = new Sk.builtins.function(initSound, gbl);
    loc.play = new Sk.builtins.function(play, gbl);
    loc.stop = new Sk.builtins.function(stop, gbl);
    loc.fadeout = new Sk.builtins.function(fadeout, gbl);
    loc.set_volume = new Sk.builtins.function(set_volume, gbl);
    loc.get_volume = new Sk.builtins.function(get_volume, gbl);
    loc.get_num_channels = new Sk.builtins.function(get_num_channels, gbl);
    return;
};
sound$1.co_name = new Sk.builtins['str']('Sound');

//创建一个Channel类
var ChannelClass = function (gbl) {
    return Sk.misceval.buildClass(gbl, channel$1, 'Channel', []);
};

//初始化Channel
var initChannel = function (self) {
    return Sk.builtin.none.none$;
};
initChannel.co_name = new Sk.builtins['str']('__init__');
initChannel.co_varnames = ['self'];

//开始播放声音
var play1 = function (self, loops, maxtime, fade_ms) {
}

play1.co_name = new Sk.builtins['str']('play1');
play1.co_varnames = ['self', 'loops', 'maxtime', 'fade_ms'];

//结束播放声音
var stop1 = function () {
}

stop1.co_name = new Sk.builtins['str']('stop1');
stop1.co_varnames = ['self'];

//结束播放声音
var fadeout1 = function () {
}

fadeout1.co_name = new Sk.builtins['str']('fadeout1');
fadeout1.co_varnames = ['self'];

//设置此声音的播放音量
var set_volume1 = function (value) {
}

set_volume1.co_name = new Sk.builtins['str']('set_volume1');
set_volume1.co_varnames = ['self', 'value'];

//获取播放音量
var get_volume1 = function () {
}

get_volume1.co_name = new Sk.builtins['str']('get_volume1');
get_volume1.co_varnames = ['self'];

var channel$1 = function $Channel$class_outer(gbl, loc) {
    loc.__init__ = new Sk.builtins.function(initChannel, gbl);
    loc.play = new Sk.builtins.function(play1, gbl);
    loc.stop = new Sk.builtins.function(stop1, gbl);
    loc.fadeout = new Sk.builtins.function(fadeout1, gbl);
    loc.set_volume = new Sk.builtins.function(set_volume1, gbl);
    loc.get_volume = new Sk.builtins.function(get_volume1, gbl);
    loc.get_num_channels = new Sk.builtins.function(get_num_channels, gbl);
    return;
};
channel$1.co_name = new Sk.builtins['str']('Channel');

var mixer_locs = {
    '__package__': Sk.builtin.none.none$,
    '__doc__': 'pygame 用于播放音效',
    '__name__': 'pygame.mixer',
    //初始化混音器模块
    init: function () {
    },
    //预设混音器初始化参数
    pre_init: function (frequency, size, channels, buffer) {
    },
    //未初始化混音器
    quit: function () {
    },
    //测试混音器是否初始化
    get_init: function () {
        return Sk.ffi.remapToPy(true);
    },
    //停止播放所有声道
    stop: function () {
    },
    //暂时停止播放所有声道
    pause: function () {
    },
    //恢复暂停播放声道
    unpause: function () {
    },
    //停止前淡出所有声音的音量
    fadeout: function (time) {
    },
    //设置播放频道的总数
    set_num_channels: function (count) {
    },
    //获取播放频道的总数
    get_num_channels: function () {
    },
    //测试是否混合了任何声音
    get_busy: function () {
    },

    music: remapInner(music),

    '_PYGAME_C_API': notImplemented
};
