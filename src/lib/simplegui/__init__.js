var $builtinmodule = function(name) {
  var mod = {};
  Sk.simplegui = {};
  var timers = [];
  var frames = [];
  var sounds = [];
  var fontfaces = {
    serif: true,
    "sans-serif": true,
    monospace: true
  };
  // Cross-browser requestAnimationFrame
  (function() {
    var lastTime = 0;
    var vendors = ["ms", "moz", "webkit", "o"];
    for (var x = 0; x < vendors.length && !window.requestAnimationFrame; ++x) {
      window.requestAnimationFrame =
        window[vendors[x] + "RequestAnimationFrame"];
      window.cancelAnimationFrame =
        window[vendors[x] + "CancelAnimationFrame"] ||
        window[vendors[x] + "CancelRequestAnimationFrame"];
    }
    if (!window.requestAnimationFrame) {
      window.requestAnimationFrame = function(callback, element) {
        var currTime = new Date().getTime();
        var timeToCall = Math.max(0, 16 - (currTime - lastTime));
        var id = window.setTimeout(function() {
          callback(currTime + timeToCall);
        }, timeToCall);
        lastTime = currTime + timeToCall;
        return id;
      };
    }
    if (!window.cancelAnimationFrame) {
      window.cancelAnimationFrame = function(id) {
        clearTimeout(id);
      };
    }
  })();

  Sk.simplegui.cleanup = function() {
    // Cleanup the module - kill all timers, release all resources
    for (var i = 0; i < timers.length; i++) {
      // Stop the timer, if it's running
      Sk.misceval.callsim(timers[i].stop, timers[i]);
    }
    timers = [];
    for (var i = 0; i < sounds.length; i++) {
      // Stop the sound, if it's playing
      Sk.misceval.callsim(sounds[i].pause, sounds[i]);
    }
    sounds = [];
    for (i = 0; i < frames.length; i++) {
      // Close the window, if it's open
      Sk.misceval.callsim(frames[i].stop, frames[i]);
    }
    frames = [];
  };
  // goog.require(\"goog.events\");
  // goog.require(\"goog.events.KeyCodes\");
  // goog.require(\"goog.events.KeyHandler\");
  // Images
  var image = function($gbl, $loc) {
    $loc.__init__ = new Sk.builtin.func(function(self, image_file) {
      self.image = new Image();
      self.image.src = Sk.ffi.unwrapo(image_file);
      self.__class__ = mod.Image;
    });
    // $loc.wait = new Sk.builtin.func(function(self) {\n        // });
    $loc.get_width = new Sk.builtin.func(function(self) {
      Sk.builtin.pyCheckArgs("get_width", arguments, 1, 1);
      return Sk.builtin.assk$(self.image.width, Sk.builtin.nmber.int$);
    });
    $loc.get_height = new Sk.builtin.func(function(self) {
      Sk.builtin.pyCheckArgs("get_height", arguments, 1, 1);
      return Sk.builtin.assk$(self.image.height, Sk.builtin.nmber.int$);
    });
  };
  mod.Image = Sk.misceval.buildClass(mod, image, "Image", []);
  mod.load_image = new Sk.builtin.func(function(image_file) {
    Sk.builtin.pyCheckArgs("load_image", arguments, 1, 1);
    if (!Sk.builtin.checkString(image_file)) {
      throw new Sk.builtin.TypeError("expected string");
    }
    return Sk.misceval.callsim(mod.Image, image_file);
  });
  // Sounds
  var sound = function($gbl, $loc) {
    $loc.__init__ = new Sk.builtin.func(function(self, sound_file) {
      if (Sk.builtin.checkString(sound_file)) {
        sound_file = Sk.ffi.unwrapo(sound_file);
      }
      self.sound = new Audio(sound_file);
      self.__class__ = mod.Sound;
      // Store sound
      sounds.push(self);
    });
    $loc.set_volume = new Sk.builtin.func(function(self, vol) {
      Sk.builtin.pyCheckArgs("set_volume", arguments, 2, 2);
      if (!Sk.builtin.checkNumber(vol)) {
        throw new Sk.builtin.TypeError("Volume must be a number");
      }
      vol = Sk.builtin.asnum$(vol);
      if (vol >= 0 && vol <= 1) {
        self.sound.volume = vol;
      } else {
        throw new Sk.builtin.ValueError("Volume must be between 0 and 1");
      }
      return Sk.builtin.none.none$;
    });
    // $loc.wait = new Sk.builtin.func(function(self) {\n        // });
    $loc.play = new Sk.builtin.func(function(self) {
      Sk.builtin.pyCheckArgs("play", arguments, 1, 1);
      self.sound.play();
      return Sk.builtin.none.none$;
    });
    $loc.pause = new Sk.builtin.func(function(self) {
      Sk.builtin.pyCheckArgs("pause", arguments, 1, 1);
      self.sound.pause();
      return Sk.builtin.none.none$;
    });
    $loc.rewind = new Sk.builtin.func(function(self) {
      Sk.builtin.pyCheckArgs("rewind", arguments, 1, 1);
      self.sound.pause();
      if (self.sound.currentTime) {
        self.sound.currentTime = 0;
      }
      return Sk.builtin.none.none$;
    });
  };
  mod.Sound = Sk.misceval.buildClass(mod, sound, "Sound", []);
  mod.load_sound = new Sk.builtin.func(function(sound_file) {
    Sk.builtin.pyCheckArgs("load_sound", arguments, 1, 1);
    if (!Sk.builtin.checkString(sound_file)) {
      throw new Sk.builtin.TypeError("expected string");
    }
    return Sk.misceval.callsim(mod.Sound, sound_file);
  });
  function base64_encode(data) {
    // http://kevin.vanzonneveld.net
    // +   original by: Tyler Akins (http://rumkin.com)
    // +   improved by: Bayron Guevara
    // +   improved by: Thunder.m\n
    // +   improved by: Kevin van Zonneveld (http://kevin.vanzonneveld.net)
    // +   bugfixed by: Pellentesque Malesuada
    // +   improved by: Kevin van Zonneveld (http://kevin.vanzonneveld.net)
    // +   improved by: Rafa\u0142 Kukawski (http://kukawski.pl)
    // *     example 1: base64_encode('Kevin van Zonneveld');
    // *     returns 1: 'S2V2aW4gdmFuIFpvbm5ldmVsZA=='
    // mozilla has this native
    // - but breaks in 2.0.0.12!
    //if (typeof this.window['btoa'] == 'function') {
    //    return btoa(data);
    //}
    var b64 =
      "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
    var o1,
      o2,
      o3,
      h1,
      h2,
      h3,
      h4,
      bits,
      i = 0,
      ac = 0,
      enc = "",
      tmp_arr = [];
    if (!data) {
      return data;
    }
    do {
      // pack three octets into four hexets
      o1 = data[i++];
      o2 = data[i++];
      o3 = data[i++];

      bits = (o1 << 16) | (o2 << 8) | o3;
      h1 = (bits >> 18) & 0x3f;
      h2 = (bits >> 12) & 0x3f;
      h3 = (bits >> 6) & 0x3f;
      h4 = bits & 0x3f;
      // use hexets to index into b64, and append result to encoded string
      tmp_arr[ac++] =
        b64.charAt(h1) + b64.charAt(h2) + b64.charAt(h3) + b64.charAt(h4);
    } while (i < data.length);
    enc = tmp_arr.join("");
    var r = data.length % 3;
    return (r ? enc.slice(0, r - 3) : enc) + "===".slice(r || 3);
  }
  mod.create_sound = new Sk.builtin.func(function(
    sound_data,
    sample_rate,
    num_channels
  ) {
    Sk.builtin.pyCheckArgs("create_sound", arguments, 1, 3);
    if (!Sk.builtin.checkSequence(sound_data)) {
      throw new Sk.builtin.TypeError("sound_data must be a sequence");
    }
    if (sample_rate !== undefined) {
      if (!Sk.builtin.checkInt(sample_rate)) {
        throw new Sk.builtin.TypeError("sample_rate must be an integer");
      }
      sample_rate = Sk.builtin.asnum$(sample_rate);
    } else {
      sample_rate = 8000;
    }
    if (num_channels !== undefined) {
      if (!Sk.builtin.checkInt(num_channels)) {
        throw new Sk.builtin.TypeError("num_channels must be an integer");
      }
      num_channels = Sk.builtin.asnum$(num_channels);
    } else {
      num_channels = 1;
    }
    function getByte(num, b) {
      return (num >> (b * 8)) & 0xff;
    }
    var bitsPerSample = 8;
    var blockAlign = (num_channels * bitsPerSample) / 8;
    var byteRate = sample_rate * blockAlign;
    var numSamples = sound_data.sq$length() / num_channels;
    var subchunk2size = numSamples * blockAlign;
    var chunksize = 36 + subchunk2size;
    // Header
    var data = [
      0x52,
      0x49,
      0x46,
      0x46, // ChunkID: "RIFF" getByte(chunksize, 0), getByte(chunksize, 1), getByte(chunksize, 2), getByte(chunksize, 3),
      // ChunkSize: 36 + SubChunk2Size
      0x57,
      0x41,
      0x56,
      0x45, // Format: \"WAVE\"
      0x66,
      0x6d,
      0x74,
      0x20, // Subchunk1ID: \"fmt \"
      0x10,
      0x00,
      0x00,
      0x00, // Subchunk1Size: 16
      0x01,
      0x00, // AudioFormat: 1 (PCM)\n            getByte(num_channels, 0), \n            getByte(num_channels, 1), // NumChannels\n            getByte(sample_rate, 0),\n            getByte(sample_rate, 1),\n            getByte(sample_rate, 2),\n            getByte(sample_rate, 3), // SampleRate\n            getByte(byteRate, 0),\n            getByte(byteRate, 1),\n            getByte(byteRate, 2),\n            getByte(byteRate, 3),    // ByteRate
      // getByte(blockAlign, 0),\n            getByte(blockAlign, 1),
      // BlockAlign\n            getByte(bitsPerSample, 0),\n            getByte(bitsPerSample, 1),
      // BitsPerSample\n
      0x64,
      0x61,
      0x74,
      0x61 // Subchunk2ID: \"data\"\n            getByte(subchunk2size, 0), \n            getByte(subchunk2size, 1), \n            getByte(subchunk2size, 2), \n            getByte(subchunk2size, 3) // Subchunk2Size\n
    ];
    var it = sound_data.tp$iter();
    var i;
    for (i = it.tp$iternext(); i !== undefined; i = it.tp$iternext()) {
      if (!Sk.builtin.checkInt(i)) {
        throw new Sk.builtin.ValueError("sound data must be 8-bit integers");
      }
      i = Sk.builtin.asnum$(i);
      if (i < 0 || i > 255) {
        throw new Sk.builtin.ValueError("sound data must be 8-bit integers");
      }
      data.push(i);
    }
    var dataURI = "data:audio/wav;base64," + base64_encode(data);
    return Sk.misceval.callsim(mod.Sound, dataURI);
  });
  var truncate = function(number) {
    return Math[number < 0 ? "ceil" : "floor"](number);
  };
  var checkPoint = function(point) {
    // Check that it is a two element sequence
    if (!Sk.builtin.checkSequence(point) || point.sq$length() != 2) {
      return false;
    }
    // Check that each element is a number
    if (
      !Sk.builtin.checkNumber(point.mp$subscript(0)) ||
      !Sk.builtin.checkNumber(point.mp$subscript(1))
    ) {
      return false;
    }
    return true;
  };
  // Find non-printing characters
  var textRE = /[^\040-\176]/;
  // Python canvas class
  var canvas = function($gbl, $loc) {
    $loc.__init__ = new Sk.builtin.func(function(self, canvas) {
      self.canvas = canvas;
      self.context = self.canvas.getContext("2d");
      if (!self.context || !self.context.drawImage) {
        alert("Cannot draw on canvas!");
        return;
      }
      self.__class__ = mod.Canvas;
    });
    $loc.draw_text = new Sk.builtin.func(function(
      self,
      text,
      point,
      size,
      color,
      face
    ) {
      Sk.builtin.pyCheckArgs("draw_text", arguments, 5, 6);
      if (!Sk.builtin.checkString(text)) {
        throw new Sk.builtin.TypeError("text must be a string");
      }
      if (!checkPoint(point)) {
        throw new Sk.builtin.TypeError("point must be a 2 element sequence");
      }
      if (!Sk.builtin.checkNumber(size)) {
        throw new Sk.builtin.TypeError("size must be a number");
      }
      size = Sk.builtin.asnum$(size);
      if (!Sk.builtin.checkString(color)) {
        throw new Sk.builtin.TypeError("color must be a string");
      }
      if (face !== undefined) {
        if (!Sk.builtin.checkString(face)) {
          throw new Sk.builtin.TypeError("font face must be a string");
        }
        face = Sk.ffi.unwrapo(face);
        // check if face is valid
        if (fontfaces[face] !== true) {
          throw new Sk.builtin.ValueError(
            "'" + face + "' is not a valid font face"
          );
        }
      } else {
        // Default value: serif
        face = "serif";
      }
      self.context.font = size + "px " + face;
      self.context.fillStyle = Sk.ffi.unwrapo(color);
      text = Sk.ffi.unwrapo(text);
      // Disallow non-printing characters
      if (textRE.test(text)) {
        console.log("textRE.test", textRE, text);
        throw new Sk.builtin.ValueError(
          "text may not contain non-printing characters"
        );
      }
      self.context.fillText(
        text,
        Sk.builtin.asnum$(point.mp$subscript(0)),
        Sk.builtin.asnum$(point.mp$subscript(1))
      );
      return Sk.builtin.none.none$;
    });
    $loc.draw_point = new Sk.builtin.func(function(self, point, color) {
      Sk.builtin.pyCheckArgs("draw_point", arguments, 3, 3);
      if (!checkPoint(point)) {
        throw new Sk.builtin.TypeError("point must be a 2 element sequence");
      }
      if (!Sk.builtin.checkString(color)) {
        throw new Sk.builtin.TypeError("color must be a string");
      }
      self.context.fillStyle = Sk.ffi.unwrapo(color);
      self.context.fillRect(
        Sk.builtin.asnum$(point.mp$subscript(0)),
        Sk.builtin.asnum$(point.mp$subscript(1)),
        1,
        1
      );
      return Sk.builtin.none.none$;
    });
    $loc.draw_line = new Sk.builtin.func(function(
      self,
      pt1,
      pt2,
      width,
      color
    ) {
      Sk.builtin.pyCheckArgs("draw_line", arguments, 5, 5);
      if (!checkPoint(pt1)) {
        throw new Sk.builtin.TypeError("point1 must be a 2 element sequence");
      }
      if (!checkPoint(pt2)) {
        throw new Sk.builtin.TypeError("point2 must be a 2 element sequence");
      }
      if (!Sk.builtin.checkNumber(width)) {
        throw new Sk.builtin.TypeError("width must be a number");
      }
      width = Sk.builtin.asnum$(width);
      if (width <= 0) {
        throw new Sk.builtin.ValueError("width must be a positive number");
      }
      if (!Sk.builtin.checkString(color)) {
        throw new Sk.builtin.TypeError("color must be a string");
      }
      self.context.lineWidth = width;
      self.context.strokeStyle = Sk.ffi.unwrapo(color);
      self.context.beginPath();
      self.context.moveTo(
        Sk.builtin.asnum$(pt1.mp$subscript(0)),
        Sk.builtin.asnum$(pt1.mp$subscript(1))
      );
      self.context.lineTo(
        Sk.builtin.asnum$(pt2.mp$subscript(0)),
        Sk.builtin.asnum$(pt2.mp$subscript(1))
      );
      self.context.stroke();
      return Sk.builtin.none.none$;
    });
    $loc.draw_circle = new Sk.builtin.func(function(
      self,
      center,
      radius,
      linewidth,
      linecolor,
      fillcolor
    ) {
      Sk.builtin.pyCheckArgs("draw_circle", arguments, 5, 6);
      if (!checkPoint(center)) {
        throw new Sk.builtin.TypeError("center must be a 2 element sequence");
      }
      if (!Sk.builtin.checkNumber(radius)) {
        throw new Sk.builtin.TypeError("radius must be a number");
      }
      radius = Sk.builtin.asnum$(radius);
      if (radius <= 0) {
        throw new Sk.builtin.ValueError("radius must be a positive number");
      }
      if (!Sk.builtin.checkNumber(linewidth)) {
        throw new Sk.builtin.TypeError("linewidth must be a number");
      }
      linewidth = Sk.builtin.asnum$(linewidth);
      if (linewidth <= 0) {
        throw new Sk.builtin.ValueError("linewidth must be a positive number");
      }
      if (!Sk.builtin.checkString(linecolor)) {
        throw new Sk.builtin.TypeError("linecolor must be a string");
      }
      // Check if fillcolor was specified and it is not None
      if (fillcolor !== undefined && fillcolor !== Sk.builtin.none.none$) {
        if (!Sk.builtin.checkString(fillcolor)) {
          throw new Sk.builtin.TypeError("fillcolor must be a string");
        }
      } else {
        // Default value: no fill - fillcolor is None
        fillcolor = Sk.builtin.none.none$;
      }
      self.context.lineWidth = linewidth;
      self.context.strokeStyle = Sk.ffi.unwrapo(linecolor);
      if (fillcolor !== Sk.builtin.none.none$) {
        self.context.fillStyle = Sk.ffi.unwrapo(fillcolor);
      }
      self.context.beginPath();
      self.context.arc(
        Sk.builtin.asnum$(center.mp$subscript(0)),
        Sk.builtin.asnum$(center.mp$subscript(1)),
        radius,
        0,
        2 * Math.PI,
        false
      );
      if (fillcolor !== Sk.builtin.none.none$) {
        self.context.fill();
      }
      self.context.stroke();
      return Sk.builtin.none.none$;
    });
    $loc.draw_polyline = new Sk.builtin.func(function(
      self,
      points,
      width,
      color
    ) {
      Sk.builtin.pyCheckArgs("draw_polyline", arguments, 4, 4);
      if (!Sk.builtin.checkSequence(points)) {
        throw new Sk.builtin.TypeError("points must be a sequence");
      }
      if (!Sk.builtin.checkNumber(width)) {
        throw new Sk.builtin.TypeError("width must be a number");
      }
      width = Sk.builtin.asnum$(width);
      if (width <= 0) {
        throw new Sk.builtin.ValueError("width must be a positive number");
      }
      if (!Sk.builtin.checkString(color)) {
        throw new Sk.builtin.TypeError("color must be a string");
      }
      self.context.lineWidth = width;
      self.context.strokeStyle = Sk.ffi.unwrapo(color);
      self.context.beginPath();
      var point = points.mp$subscript(0);
      if (!checkPoint(point)) {
        throw new Sk.builtin.TypeError(
          "each point in points must be a 2 element sequence"
        );
      }
      self.context.moveTo(
        Sk.builtin.asnum$(point.mp$subscript(0)),
        Sk.builtin.asnum$(point.mp$subscript(1))
      );
      for (i = 1; i < points.sq$length(); i++) {
        point = points.mp$subscript(i);
        if (!checkPoint(point)) {
          throw new Sk.builtin.TypeError(
            "each point in points must be a 2 element sequence"
          );
        }
        self.context.lineTo(
          Sk.builtin.asnum$(point.mp$subscript(0)),
          Sk.builtin.asnum$(point.mp$subscript(1))
        );
      }
      self.context.stroke();
      return Sk.builtin.none.none$;
    });
    $loc.draw_polygon = new Sk.builtin.func(function(
      self,
      points,
      linewidth,
      linecolor,
      fillcolor
    ) {
      Sk.builtin.pyCheckArgs("draw_polygon", arguments, 4, 5);
      if (!Sk.builtin.checkSequence(points)) {
        throw new Sk.builtin.TypeError("points must be a sequence");
      }
      if (!Sk.builtin.checkNumber(linewidth)) {
        throw new Sk.builtin.TypeError("linewidth must be a number");
      }
      linewidth = Sk.builtin.asnum$(linewidth);
      if (linewidth <= 0) {
        throw new Sk.builtin.ValueError("linewidth must be a positive number");
      }
      if (!Sk.builtin.checkString(linecolor)) {
        throw new Sk.builtin.TypeError("linecolor must be a string");
      }
      // Check if fillcolor was specified and it is not None
      if (fillcolor !== undefined && fillcolor !== Sk.builtin.none.none$) {
        if (!Sk.builtin.checkString(fillcolor)) {
          throw new Sk.builtin.TypeError("fillcolor must be a string");
        }
      } else {
        // Default value: no fill - fillcolor is None
        fillcolor = Sk.builtin.none.none$;
      }
      self.context.lineWidth = linewidth;
      self.context.strokeStyle = Sk.ffi.unwrapo(linecolor);
      if (fillcolor !== Sk.builtin.none.none$) {
        self.context.fillStyle = Sk.ffi.unwrapo(fillcolor);
      }
      self.context.beginPath();
      var point = points.mp$subscript(0);
      var point0x = Sk.builtin.asnum$(point.mp$subscript(0));
      var point0y = Sk.builtin.asnum$(point.mp$subscript(1));
      if (!checkPoint(point)) {
        throw new Sk.builtin.TypeError(
          "each point in points must be a 2 element sequence"
        );
      }
      self.context.moveTo(point0x, point0y);
      for (i = 1; i < points.sq$length(); i++) {
        point = points.mp$subscript(i);
        if (!checkPoint(point)) {
          throw new Sk.builtin.TypeError(
            "each point in points must be a 2 element sequence"
          );
        }
        self.context.lineTo(
          Sk.builtin.asnum$(point.mp$subscript(0)),
          Sk.builtin.asnum$(point.mp$subscript(1))
        );
      }
      self.context.lineTo(point0x, point0y);
      self.context.closePath();
      if (fillcolor !== Sk.builtin.none.none$) {
        self.context.fill();
      }
      self.context.stroke();
      return Sk.builtin.none.none$;
    });
    $loc.draw_image = new Sk.builtin.func(function(
      self,
      image,
      srcpos,
      srcdim,
      dstpos,
      dstdim,
      rot
    ) {
      Sk.builtin.pyCheckArgs("draw_image", arguments, 6, 7);
      var im = null;
      if (image !== null && image.__class__ == mod.Image) {
        im = image.image;
      } else if (image !== null && image.__class__ == mod.Canvas) {
        im = image.canvas;
      } else {
        throw new Sk.builtin.TypeError("image must be an image");
      }
      if (!checkPoint(srcpos)) {
        throw new Sk.builtin.TypeError(
          "source center must be a 2 element sequence"
        );
      }
      if (!checkPoint(srcdim)) {
        throw new Sk.builtin.TypeError(
          "source dimensions must be a 2 element sequence"
        );
      }
      if (!checkPoint(dstpos)) {
        throw new Sk.builtin.TypeError(
          "destination center must be a 2 element sequence"
        );
      }
      if (!checkPoint(dstdim)) {
        throw new Sk.builtin.TypeError(
          "destination dimensions must be a 2 element sequence"
        );
      }
      if (rot !== undefined) {
        if (!Sk.builtin.checkNumber(rot)) {
          throw new Sk.builtin.TypeError("rotation must be a number");
        }
      }
      var srcx = Sk.builtin.asnum$(srcpos.mp$subscript(0));
      var srcy = Sk.builtin.asnum$(srcpos.mp$subscript(1));
      var srcw = Sk.builtin.asnum$(srcdim.mp$subscript(0));
      var srch = Sk.builtin.asnum$(srcdim.mp$subscript(1));
      var dstx = Sk.builtin.asnum$(dstpos.mp$subscript(0));
      var dsty = Sk.builtin.asnum$(dstpos.mp$subscript(1));
      var dstw = Sk.builtin.asnum$(dstdim.mp$subscript(0));
      var dsth = Sk.builtin.asnum$(dstdim.mp$subscript(1));
      if (rot === undefined) {
        rot = 0;
      }
      rot = Sk.builtin.asnum$(rot);
      if (srcw <= 0 || srch <= 0 || dstw <= 0 || dsth <= 0) {
        throw new Sk.builtin.ValueError("image dimensions must be > 0");
      }
      srcx = truncate(srcx - srcw / 2);
      srcy = truncate(srcy - srch / 2);
      var dstoffx = truncate(-dstw / 2);
      var dstoffy = truncate(-dsth / 2);
      if (srcx < 0 || srcy < 0) {
        // Do not draw anything
        return;
      }
      if (srcx + srcw > im.width || srcy + srch > im.height) {
        // Safari: Do not draw anything
        return;
      }
      self.context.save();
      self.context.translate(dstx, dsty);
      self.context.rotate(rot);
      self.context.drawImage(
        im,
        srcx,
        srcy,
        srcw,
        srch,
        dstoffx,
        dstoffy,
        dstw,
        dsth
      );
      self.context.restore();
      return Sk.builtin.none.none$;
    });
  };
  mod.Canvas = Sk.misceval.buildClass(mod, canvas, "Canvas", []);
  var create_canvas = function(win, width, height, border) {
    var canvas = win.document.createElement("canvas");
    canvas.width = width;
    canvas.height = height;
    canvas.style.border = border.toString() + "px solid black";
    canvas.style.cssFloat = "right";
    canvas.setAttribute("tabindex", "0");
    canvas.onselectstart = function() {
      // Prevent weird selection on double click
      return false;
    };
    return canvas;
  };
  mod.create_invisible_canvas = new Sk.builtin.func(function(width, height) {
    Sk.builtin.pyCheckArgs("create_invis_canvas", arguments, 2, 2);
    if (!Sk.builtin.checkInt(width)) {
      throw new Sk.builtin.TypeError("width must be an integer");
    }
    if (!Sk.builtin.checkInt(height)) {
      throw new Sk.builtin.TypeError("height must be an integer");
    }
    var canvas = create_canvas(
      window,
      Sk.builtin.asnum$(width),
      Sk.builtin.asnum$(height),
      0
    );
    var pycanvas = Sk.misceval.callsim(mod.Canvas, canvas);
    return pycanvas;
  });
  // Control class
  var control = function($gbl, $loc) {
    $loc.__init__ = new Sk.builtin.func(function(self, object) {
      self._object = object;
    });
    $loc.get_text = new Sk.builtin.func(function(self) {
      Sk.builtin.pyCheckArgs("get_text", arguments, 1, 1);
      return Sk.ffi.basicwrap(self._object.textContent);
    });
    $loc.set_text = new Sk.builtin.func(function(self, text) {
      Sk.builtin.pyCheckArgs("set_text", arguments, 2, 2);
      var s = new Sk.builtin.str(text);
      self._object.textContent = Sk.ffi.unwrapo(s);
    });
  };
  mod.Control = Sk.misceval.buildClass(mod, control, "Control", []);
  // Text Area Control class
  var textareacontrol = function($gbl, $loc) {
    $loc.__init__ = new Sk.builtin.func(function(self, object) {
      self._object = object;
    });
    $loc.get_text = new Sk.builtin.func(function(self) {
      Sk.builtin.pyCheckArgs("get_text", arguments, 1, 1);
      return Sk.ffi.basicwrap(self._object.value);
    });
    $loc.set_text = new Sk.builtin.func(function(self, text) {
      Sk.builtin.pyCheckArgs("set_text", arguments, 2, 2);
      var s = new Sk.builtin.str(text);
      self._object.value = Sk.ffi.unwrapo(s);
    });
  };
  mod.TextAreaControl = Sk.misceval.buildClass(
    mod,
    textareacontrol,
    "TextAreaControl",
    []
  );
  var statusBox = function(text, offset, width) {
    var box = document.createElement("div");
    box.textContent = text;
    box.style.width = width - 12 + "px";
    box.style.position = "absolute";
    box.style.bottom = offset + "px";
    box.style.border = "1px solid black";
    box.style.paddingLeft = "5px";
    box.style.paddingRight = "5px";
    return box;
  };
  var canvasCoords = function(canvas, evt) {
    // Get canvas position
    var curr = canvas;
    var top = 0;
    var left = 0;
    while (curr && curr.tagName != "BODY") {
      top += curr.offsetTop;
      left += curr.offsetLeft;
      curr = curr.offsetParent;
    }
    // Return relative mouse position
    return { x: evt.pageX - left, y: evt.pageY - top };
  };
  var deentify = function(html) {
    if (!html) {
      return html;
    }
    var a = html.v;
    a = a.replace(/&/g, "&amp;");
    a = a.replace(/</g, "&lt;");
    a = a.replace(/>/g, "&gt;");
    return a;
  };
  var setExecStartNow = function(a) {
    if (a || !Sk.execStart) {
      Sk.execStart = Date.now();
    }
  };
  // Key map
  mod.KEY_MAP = Sk.builtin.dict([]);
  var i;
  var code2key = {};
  // Add letters
  for (i = 65; i <= 90; i++) {
    // Lowercase
    var ch = String.fromCharCode(i + 32);
    mod.KEY_MAP.mp$ass_subscript(
      Sk.ffi.basicwrap(ch),
      Sk.builtin.assk$(i, Sk.builtin.nmber.int$)
    );
    code2key[i] = ch;
    // Uppercase
    ch = String.fromCharCode(i);
    mod.KEY_MAP.mp$ass_subscript(
      Sk.ffi.basicwrap(ch),
      Sk.builtin.assk$(i, Sk.builtin.nmber.int$)
    );
  }
  // Add numbers
  for (i = 48; i <= 57; i++) {
    var ch = String.fromCharCode(i);
    mod.KEY_MAP.mp$ass_subscript(
      Sk.ffi.basicwrap(ch),
      Sk.builtin.assk$(i, Sk.builtin.nmber.int$)
    );
    code2key[i] = ch;
  }
  // Add space
  mod.KEY_MAP.mp$ass_subscript(
    Sk.ffi.basicwrap("space"),
    Sk.builtin.assk$(32, Sk.builtin.nmber.int$)
  );
  code2key[32] = "space";
  // Add arrows
  mod.KEY_MAP.mp$ass_subscript(
    Sk.ffi.basicwrap("left"),
    Sk.builtin.assk$(37, Sk.builtin.nmber.int$)
  );
  mod.KEY_MAP.mp$ass_subscript(
    Sk.ffi.basicwrap("up"),
    Sk.builtin.assk$(38, Sk.builtin.nmber.int$)
  );
  mod.KEY_MAP.mp$ass_subscript(
    Sk.ffi.basicwrap("right"),
    Sk.builtin.assk$(39, Sk.builtin.nmber.int$)
  );
  mod.KEY_MAP.mp$ass_subscript(
    Sk.ffi.basicwrap("down"),
    Sk.builtin.assk$(40, Sk.builtin.nmber.int$)
  );
  code2key[37] = String.fromCharCode(0x2190); // \"left\";
  code2key[38] = String.fromCharCode(0x2191); // \"up\";
  code2key[39] = String.fromCharCode(0x2192); // \"right\";
  code2key[40] = String.fromCharCode(0x2193); // \"down\";
  // Python frame class\n
  var frame = function($gbl, $loc) {
    $loc.__init__ = new Sk.builtin.func(function(
      self,
      title,
      canvas_width,
      canvas_height,
      control_width
    ) {
      var framediv;
      // Save parameters
      self.title = title;
      self.width = Sk.builtin.asnum$(canvas_width);
      self.height = Sk.builtin.asnum$(canvas_height);
      if (control_width === undefined) {
        control_width = 200;
      } else {
        control_width = Sk.builtin.asnum$(control_width);
      }
      self.ctrlWidth = control_width;
      self.margin = 23;
      // Initial defaults
      self.draw_handler = new Sk.builtin.func(function(canvas) {});
      self.background = "#000000";
      // Create frame window
      var winwidth = self.width + self.ctrlWidth + self.margin * 3 + 4;
      var winheight = self.height + self.margin * 2 + 4;
      self.frame_window = window.open(
        "",
        "myframe",
        "width=" +
          winwidth +
          ",height=" +
          winheight +
          ",location=0" +
          ",menubar=0" +
          ",toolbar=0" +
          ",directories=0" +
          ",status=0" +
          ",titlebar=0" +
          ",scrollbars=0" +
          ",resizeable=1"
      );
      // Build empty document
      // Escape title
      // var jstitle = title.html$deentify();
      var jstitle = deentify(title.html);
      var framehtml =
        "<html>" +
        "<head>" +
        "<title>" +
        jstitle +
        "</title>" +
        "</head>" +
        "<body>" +
        '<div id="guiframe"></div>' +
        "</body>" +
        "</html>";

      self.frame_window.document.writeln("<!DOCTYPE html>");
      self.frame_window.document.writeln(framehtml);
      self.frame_window.document.close();
      // Build GUI areas
      var framebody = self.frame_window.document.getElementsByTagName(
        "body"
      )[0];
      framebody.style.margin = "0px";
      // Control Pane
      self.control = self.frame_window.document.createElement("div");
      // +4 to match 2px border around canvas
      self.control.style.height = self.height + 4 + "px";
      self.control.style.width = self.ctrlWidth + "px";
      self.control.style.position = "relative";
      self.control.style.cssFloat = "left";
      // Drawing Canvas
      self.canvas_border = 2;
      self.canvas = create_canvas(
        self.frame_window,
        self.width,
        self.height,
        self.canvas_border
      );
      self.animationID = null;
      // Key state
      self.keydown = {};
      self.keyuphandler = null;
      self.keydownhandler = null;
      self.canvas.onkeydown = function(evt) {
        if (!self.keydown[evt.keyCode]) {
          self.keydown[evt.keyCode] = true;
          if (self.keydownhandler) {
            var key = code2key[evt.keyCode];
            if (key === undefined) {
              key = "<" + evt.keyCode + ">";
            }
            self.keyevents.textContent = "Key: Down " + key;
            try {
              setExecStartNow(true);
              Sk.currLineNo = self.keydown_lineno;
              Sk.misceval.callsim(
                self.keydownhandler,
                Sk.builtin.assk$(evt.keyCode, Sk.builtin.nmber.int$)
              );
            } catch (e) {
              // Sk.error(e);
              throw e;
            }
          }
        }
      };
      self.canvas.onkeyup = function(evt) {
        self.keydown[evt.keyCode] = false;
        if (self.keyuphandler) {
          var key = code2key[evt.keyCode];
          if (key === undefined) {
            key = "<" + evt.keyCode + ">";
          }
          self.keyevents.textContent = "Key: Up " + key;
          try {
            setExecStartNow(true);
            Sk.currLineNo = self.keyup_lineno;
            Sk.misceval.callsim(
              self.keyuphandler,
              Sk.builtin.assk$(evt.keyCode, Sk.builtin.nmber.int$)
            );
          } catch (e) {
            throw e;
          }
        }
      };
      // Mouse
      self.mousedraghandler = null;
      var mousemove = function(evt) {
        var coords = canvasCoords(self.canvas, evt);
        // Adjust position to remove border
        var x = coords.x - self.canvas_border;
        var y = coords.y - self.canvas_border;
        if (x < 0 || x >= self.width || y < 0 || y >= self.height) {
          // move was in border
          return;
        }
        var pos = new Sk.builtins["tuple"]([
          Sk.builtin.assk$(x, Sk.builtin.nmber.int$),
          Sk.builtin.assk$(y, Sk.builtin.nmber.int$)
        ]);
        self.mouseevents.textContent = "Mouse: Move - " + x + ", " + y;
        try {
          setExecStartNow(true);
          Sk.currLineNo = self.mousedrag_lineno;
          Sk.misceval.callsim(self.mousedraghandler, pos);
        } catch (e) {
          throw e;
        }
      };
      var mousedone = function(evt) {
        self.canvas.removeEventListener("mousemove", mousemove);
        self.canvas.removeEventListener("mouseup", mousedone);
        self.canvas.removeEventListener("mouseout", mousedone);
      };
      self.canvas.onmousedown = function(evt) {
        if (self.mousedraghandler) {
          self.canvas.addEventListener("mousemove", mousemove);
          self.canvas.addEventListener("mouseup", mousedone);
          self.canvas.addEventListener("mouseout", mousedone);
        }
      };
      // Add elements to frame
      framediv = self.frame_window.document.getElementById("guiframe");
      framediv.style.width =
        self.width + self.ctrlWidth + self.margin + 4 + "px";
      framediv.style.height = self.height + 4 + "px";
      framediv.style.margin = self.margin + "px";
      // framediv.style.overflow = \"auto\";
      framediv.appendChild(self.control);
      framediv.appendChild(self.canvas);
      // These need to be added after the control area is on the page
      // Otherwise, the mouse event box's height cannot be determined
      self.mouseevents = statusBox("Mouse:", 0, self.ctrlWidth);
      self.control.appendChild(self.mouseevents);
      self.keyevents = statusBox(
        "Key:",
        self.mouseevents.offsetHeight + 5,
        self.ctrlWidth
      );
      self.control.appendChild(self.keyevents);
      // Store frame
      frames.push(self);
      // Give the canvas the focus
      self.canvas.focus();
    });
    $loc.get_canvas_textwidth = new Sk.builtin.func(function(
      self,
      text,
      size,
      face
    ) {
      Sk.builtin.pyCheckArgs("get_canvas_textwidth", arguments, 3, 4);
      if (!Sk.builtin.checkString(text)) {
        throw new Sk.builtin.TypeError("text must be a string");
      }
      if (!Sk.builtin.checkNumber(size)) {
        throw new Sk.builtin.TypeError("size must be a number");
      }
      size = Sk.builtin.asnum$(size);
      if (face !== undefined) {
        if (!Sk.builtin.checkString(face)) {
          throw new Sk.builtin.TypeError("font face must be a string");
        }
        face = Sk.ffi.unwrapo(face);
        // check if face is valid
        if (fontfaces[face] !== true) {
          throw new Sk.builtin.ValueError(
            "'" + face + "' is not a valid font face"
          );
        }
      } else {
        // Default value: serif
        face = "serif";
      }
      var context = self.canvas.getContext("2d");
      context.font = size + "px " + face;
      text = Sk.ffi.unwrapo(text);
      var metrics = context.measureText(text);
      return Sk.builtin.assk$(metrics.width | 0, Sk.builtin.nmber.int$);
    });
    $loc.set_canvas_background = new Sk.builtin.func(function(self, color) {
      Sk.builtin.pyCheckArgs("set_canvas_background", arguments, 2, 2);
      if (!Sk.builtin.checkString(color)) {
        throw new Sk.builtin.TypeError("expected string");
      }
      self.background = Sk.ffi.unwrapo(color);
      return Sk.builtin.none.none$;
    });
    $loc.get_canvas_image = new Sk.builtin.func(function(self) {
      Sk.builtin.pyCheckArgs("get_canvas_image", arguments, 1, 1);
      var imagedata = self.canvas.toDataURL();
      window.open(
        imagedata,
        "Canvas Image",
        "left=0,top=0,width=" +
          self.canvas.width +
          ",height=" +
          self.canvas.height +
          ",toolbar=0,resizeable=0"
      );
      return Sk.builtin.none.none$;
    });
    var cancelAnimation = function(frame) {
      if (frame.animationID) {
        cancelAnimationFrame(frame.animationID);
        frame.animationID = null;
      }
    };
    $loc.start = new Sk.builtin.func(function(self) {
      Sk.builtin.pyCheckArgs("start", arguments, 1, 1);
      // Make the frame visible and start the gui
      var context = self.canvas.getContext("2d");
      if (!context || !context.drawImage) {
        alert("Cannot draw on canvas!");
        return;
      }
      var canvas = Sk.misceval.callsim(mod.Canvas, self.canvas);
      // Functions for built-in browser animation callback
      var draw = function() {
        context.fillStyle = self.background;
        context.fillRect(0, 0, self.canvas.width, self.canvas.height);
        try {
          setExecStartNow(true);
          Sk.currLineNo = self.draw_lineno;
          Sk.misceval.callsim(self.draw_handler, canvas);
        } catch (e) {
          throw e;
        }
      };
      var animate = function animate() {
        self.animationID = requestAnimationFrame(animate);
        draw();
      };
      // Make sure callbacks stop when window is closed
      self.frame_window.onbeforeunload = function() {
        // Works for Chrome and FireFox
        cancelAnimation(self);
      };
      self.frame_window.onunload = function() {
        // Needed for Safari
        cancelAnimation(self);
      };
      // Request first animation frame
      self.animationID = requestAnimationFrame(animate);
      return Sk.builtin.none.none$;
    });
    $loc.stop = new Sk.builtin.func(function(self) {
      Sk.builtin.pyCheckArgs("stop", arguments, 1, 1);
      self.frame_window.close();
      cancelAnimation(self);
      return Sk.builtin.none.none$;
    });
    $loc.add_button = new Sk.builtin.func(function(self, text, handler, width) {
      Sk.builtin.pyCheckArgs("add_button", arguments, 3, 4);
      if (!Sk.builtin.checkString(text)) {
        throw new Sk.builtin.TypeError("text must be a string");
      }
      if (!Sk.builtin.checkFunction(handler)) {
        throw new Sk.builtin.TypeError("handler must be a function");
      }
      if (width !== undefined) {
        if (!Sk.builtin.checkInt(width)) {
          throw new Sk.builtin.TypeError("width must be an integer");
        }
        width = Sk.builtin.asnum$(width);
      }
      var lineno = Sk.currLineNo;
      // Make the actual button
      var button = document.createElement("button");
      var br = document.createElement("br");
      button.type = "button";
      button.textContent = Sk.ffi.unwrapo(text);
      if (width !== undefined) {
        button.style.width = width + "px";
      }
      button.onclick = function() {
        try {
          setExecStartNow(true);
          Sk.currLineNo = lineno;
          Sk.misceval.callsim(handler);
          // Give the canvas back the focus
          self.canvas.focus();
        } catch (e) {
          throw e;
        }
      };
      // Add button to control area
      self.control.appendChild(button);
      self.control.appendChild(br);
      return Sk.misceval.callsim(mod.Control, button);
    });
    $loc.add_label = new Sk.builtin.func(function(self, text, width) {
      Sk.builtin.pyCheckArgs("add_label", arguments, 2, 3);
      if (!Sk.builtin.checkString(text)) {
        throw new Sk.builtin.TypeError("text must be a string");
      }
      if (width !== undefined) {
        if (!Sk.builtin.checkInt(width)) {
          throw new Sk.builtin.TypeError("width must be an integer");
        }
        width = Sk.builtin.asnum$(width);
      }
      // Make the actual label
      var label = document.createElement("span");
      var br = document.createElement("br");
      label.textContent = Sk.ffi.unwrapo(text);
      label.style.display = "inline-block";
      if (width !== undefined) {
        label.style.width = width + "px";
      }
      // console.log(label.style);
      // Add label to control area
      self.control.appendChild(label);
      self.control.appendChild(br);
      return Sk.misceval.callsim(mod.Control, label);
    });
    $loc.add_input = new Sk.builtin.func(function(self, text, handler, width) {
      Sk.builtin.pyCheckArgs("add_input", arguments, 4, 4);
      if (!Sk.builtin.checkString(text)) {
        throw new Sk.builtin.TypeError("text must be a string");
      }
      if (!Sk.builtin.checkFunction(handler)) {
        throw new Sk.builtin.TypeError("handler must be a function");
      }
      if (!Sk.builtin.checkInt(width)) {
        throw new Sk.builtin.TypeError("width must be an integer");
      }
      width = Sk.builtin.asnum$(width);
      var lineno = Sk.currLineNo;
      // Make the actual text field
      var label = document.createElement("span");
      var textField = document.createElement("textarea");
      var br1 = document.createElement("br");
      var br2 = document.createElement("br");
      label.textContent = Sk.ffi.unwrapo(text);
      textField.rows = 1;
      textField.style.resize = "none";
      textField.style.width = width + "px";
      // Keypress handler to trap \"enter\" key
      textField.onkeypress = function(evt) {
        // Call Python handler when \"enter\" is pressed
        if (evt.keyCode == 13) {
          // Don't let the text box contain multiple lines
          evt.preventDefault();
          try {
            var txt = Sk.ffi.basicwrap(textField.value);
            setExecStartNow(true);
            Sk.currLineNo = lineno;
            Sk.misceval.callsim(handler, txt);
            // Give the canvas back the focus
            self.canvas.focus();
          } catch (e) {
            throw e;
          }
        }
      };
      // Add text field to control area
      self.control.appendChild(label);
      self.control.appendChild(br1);
      self.control.appendChild(textField);
      self.control.appendChild(br2);
      return Sk.misceval.callsim(mod.TextAreaControl, textField);
    });
    $loc.set_keyup_handler = new Sk.builtin.func(function(self, handler) {
      Sk.builtin.pyCheckArgs("set_keyup_handler", arguments, 2, 2);
      if (!Sk.builtin.checkFunction(handler)) {
        throw new Sk.builtin.TypeError("handler must be a function");
      }
      self.keyuphandler = handler;
      self.keyup_lineno = Sk.currLineNo;
      return Sk.builtin.none.none$;
    });
    $loc.set_keydown_handler = new Sk.builtin.func(function(self, handler) {
      Sk.builtin.pyCheckArgs("set_keydown_handler", arguments, 2, 2);
      if (!Sk.builtin.checkFunction(handler)) {
        throw new Sk.builtin.TypeError("handler must be a function");
      }
      self.keydownhandler = handler;
      self.keydown_lineno = Sk.currLineNo;
      return Sk.builtin.none.none$;
    });
    $loc.set_mouseclick_handler = new Sk.builtin.func(function(self, handler) {
      Sk.builtin.pyCheckArgs("set_mouseclick_handler", arguments, 2, 2);
      if (!Sk.builtin.checkFunction(handler)) {
        throw new Sk.builtin.TypeError("handler must be a function");
      }
      var lineno = Sk.currLineNo;
      self.canvas.onclick = function(evt) {
        var coords = canvasCoords(self.canvas, evt);
        // Adjust position to remove border
        var x = coords.x - self.canvas_border;
        var y = coords.y - self.canvas_border;
        if (x < 0 || x >= self.width || y < 0 || y >= self.height) {
          // Click was in border
          return;
        }
        var pos = new Sk.builtins["tuple"]([
          Sk.builtin.assk$(x, Sk.builtin.nmber.int$),
          Sk.builtin.assk$(y, Sk.builtin.nmber.int$)
        ]);
        self.mouseevents.textContent = "Mouse: Click " + x + ", " + y;
        try {
          setExecStartNow(true);
          Sk.currLineNo = lineno;
          Sk.misceval.callsim(handler, pos);
        } catch (e) {
          throw e;
        }
      };
      return Sk.builtin.none.none$;
    });
    $loc.set_mousedrag_handler = new Sk.builtin.func(function(self, handler) {
      Sk.builtin.pyCheckArgs("set_mousedrag_handler", arguments, 2, 2);
      if (!Sk.builtin.checkFunction(handler)) {
        throw new Sk.builtin.TypeError("handler must be a function");
      }
      self.mousedraghandler = handler;
      self.mousedrag_lineno = Sk.currLineNo;
      return Sk.builtin.none.none$;
    });
    $loc.set_draw_handler = new Sk.builtin.func(function(self, handler) {
      Sk.builtin.pyCheckArgs("set_draw_handler", arguments, 2, 2);
      if (!Sk.builtin.checkFunction(handler)) {
        throw new Sk.builtin.TypeError("handler must be a function");
      }
      self.draw_handler = handler;
      self.draw_lineno = Sk.currLineNo;
      return Sk.builtin.none.none$;
    });
  };
  mod.Frame = Sk.misceval.buildClass(mod, frame, "Frame", []);
  mod.create_frame = new Sk.builtin.func(function(
    title,
    canvas_width,
    canvas_height,
    control_width
  ) {
    Sk.builtin.pyCheckArgs("create_frame", arguments, 3, 4);
    if (!Sk.builtin.checkString(title)) {
      throw new Sk.builtin.TypeError("title must be a string");
    }
    if (!Sk.builtin.checkNumber(canvas_width)) {
      throw new Sk.builtin.TypeError("canvas width must be a number");
    }
    if (!Sk.builtin.checkNumber(canvas_height)) {
      throw new Sk.builtin.TypeError("canvas height must be a number");
    }
    if (control_width !== undefined) {
      if (!Sk.builtin.checkNumber(control_width)) {
        throw new Sk.builtin.TypeError("control width must be a number");
      }
      if (Sk.builtin.asnum$(control_width) < 0) {
        throw new Sk.builtin.ValueError("control width must be >= 0");
      }
    }
    if (Sk.builtin.asnum$(canvas_width) < 0) {
      throw new Sk.builtin.ValueError("canvas width must be >= 0");
    }
    if (Sk.builtin.asnum$(canvas_height) < 0) {
      throw new Sk.builtin.ValueError("canvas height must be >= 0");
    }
    return Sk.misceval.callsim(
      mod.Frame,
      title,
      canvas_width,
      canvas_height,
      control_width
    );
  });
  // Python timer class
  var timer = function($gbl, $loc) {
    $loc.__init__ = new Sk.builtin.func(function(self, interval, handler) {
      // Initialize
      self.interval = interval;
      self.handler = handler;
      self._timer = null;
      self.lineno = Sk.currLineNo;
      // Store timer
      timers.push(self);
    });
    $loc.start = new Sk.builtin.func(function(self) {
      Sk.builtin.pyCheckArgs("start", arguments, 1, 1);
      if (self._timer) {
        // Already running, ignore
        return;
      }
      // Create new Javascript timer which calls the Python handler
      self._timer = setInterval(function() {
        try {
          // Sk.setExecStartNow(true);
          setExecStartNow(true);
          Sk.currLineNo = self.lineno;
          Sk.misceval.callsim(self.handler);
        } catch (e) {
          clearInterval(self._timer);
          self._timer = null;
          throw e;
        }
      }, Sk.builtin.asnum$(self.interval));
      return Sk.builtin.none.none$;
    });
    $loc.stop = new Sk.builtin.func(function(self) {
      Sk.builtin.pyCheckArgs("stop", arguments, 1, 1);
      // If a Javascript timer exists, stop it and delete it
      if (self._timer) {
        clearInterval(self._timer);
        self._timer = null;
      }
      return Sk.builtin.none.none$;
    });
    $loc.get_interval = new Sk.builtin.func(function(self) {
      Sk.builtin.pyCheckArgs("get_interval", arguments, 1, 1);
      return self.interval;
    });
    $loc.is_running = new Sk.builtin.func(function(self) {
      Sk.builtin.pyCheckArgs("is_running", arguments, 1, 1);
      if (self._timer) {
        return Sk.builtin.bool.true$;
      } else {
        return Sk.builtin.bool.false$;
      }
    });
  };
  mod.Timer = Sk.misceval.buildClass(mod, timer, "Timer", []);
  mod.create_timer = new Sk.builtin.func(function(interval, handler) {
    Sk.builtin.pyCheckArgs("create_timer", arguments, 2, 2);
    if (!Sk.builtin.checkNumber(interval)) {
      throw new Sk.builtin.TypeError("interval must be a number");
    }
    if (!Sk.builtin.checkFunction(handler)) {
      throw new Sk.builtin.TypeError("handler must be a function");
    }
    if (Sk.builtin.asnum$(interval) <= 0) {
      throw new Sk.builtin.ValueError("interval must be > 0");
    }
    return Sk.misceval.callsim(mod.Timer, interval, handler);
  });
  return mod;
};
