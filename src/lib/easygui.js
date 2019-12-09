// var globalScope = typeof window !== 'undefined' ? window : global;

var $builtinmodule = function (name) {
    var mod = {};

    mod.msgbox = new Sk.builtins.function(showmsgbox);

    mod.buttonbox = new Sk.builtins.function(showbuttonbox);

    mod.enterbox = new Sk.builtin.func(showenterbox);

    // mod.enterbox = new Sk.builtin.func(function (msg, title, _default, strip, image) {
    //   console.log('showenterbox', msg, title, _default, strip, image);
    //   // Sk.builtin.pyCheckArgs('showenterbox', arguments, 0, 5, true, false);
    //   var msgJS = "(Your message goes here)";
    //   if (isValid(msg)) {msgJS = Sk.ffi.remapToJs(msg);}
    //   var titleJS = "";
    //   if (isValid(title)) {titleJS = Sk.ffi.remapToJs(title);}
    //   var defaultJS = "";
    //   if (isValid(_default)) {defaultJS = Sk.ffi.remapToJs(_default);}
    //   var stripJS = "";
    //   if (isValid(strip)) {stripJS = Sk.ffi.remapToJs(strip);}
    //   var imgJS = "";
    //   if (isValid(image)) {imgJS = Sk.ffi.remapToJs(image);}
    //   console.log('#dialog .content', $("#dialog .content"));
    //   $("#dialog .content").text(msgJS);//弹出文本
    //   $("#dialog .imgcontent").empty();
    //   if (imgJS.length > 0){ //关联图像
    //     var path = getResImage(imgJS);
    //     $("#dialog .imgcontent").html("<img src='" + path + "' />");
    //   }
    //   $("#dialog .attach").show();
    //   $("#dialog .attach").html("<input id='usercontent' type='text' value='" + defaultJS + "'>");
    //   var sys = Sk.importModule("sys");
    //   return Sk.misceval.callsimOrSuspend(Sk.builtin.guiBox, sys["$d"]["stdin"], 2, titleJS, stripJS);
    // });

    return mod;
};

var showmsgbox = function (msg, title, ok_button, image) {
    Sk.builtin.pyCheckArgs('showmsgbox', arguments, 0, 4, true, false);
    var msgJS = "(Your message goes here)";
    if (isValid(msg)) {msgJS = Sk.ffi.remapToJs(msg);}
    var titleJS = "";
    if (isValid(title)) {titleJS = Sk.ffi.remapToJs(title);}
    var okJS = "OK";
    if (isValid(ok_button)) {okJS = Sk.ffi.remapToJs(ok_button);}
    var imgJS = "";
    if (isValid(image)) {imgJS = Sk.ffi.remapToJs(image);}
    $("#dialog .content").text(msgJS);//弹出文本
    $("#dialog .imgcontent").empty();
    if (imgJS.length > 0){ //关联图像
        var path = getResImage(imgJS);
        $("#dialog .imgcontent").html("<img src='" + path + "' />");
    }
    $("#dialog .attach").hide();
    var sys = Sk.importModule("sys");
    return Sk.misceval.callsimOrSuspend(Sk.builtin.guiBox, sys["$d"]["stdin"], 0, titleJS, okJS);
}

showmsgbox.co_name = new Sk.builtins['str']('msgbox');
showmsgbox.co_varnames = ['msg', 'title', 'ok_button', 'image'];

var showbuttonbox = function (msg, title, choices, image) {
    Sk.builtin.pyCheckArgs('showbuttonbox', arguments, 0, 4, true, false);
    var msgJS = "(Your message goes here)";
    if (isValid(msg)) {msgJS = Sk.ffi.remapToJs(msg);}
    var titleJS = "";
    if (isValid(title)) {titleJS = Sk.ffi.remapToJs(title);}
    var choicesJS = [];
    if (isValid(choices)) {choicesJS = Sk.ffi.remapToJs(choices);}
    var imgJS = "";
    if (isValid(image)) {imgJS = Sk.ffi.remapToJs(image);}
    $("#dialog .content").text(msgJS);//弹出文本
    $("#dialog .imgcontent").empty();
    if (imgJS.length > 0){ //关联图像
      var path = getResImage(imgJS);
      $("#dialog .imgcontent").html("<img src='" + path + "' />");
    }
    $("#dialog .attach").hide();
    var sys = Sk.importModule("sys");
    return Sk.misceval.callsimOrSuspend(Sk.builtin.guiBox, sys["$d"]["stdin"], 1, titleJS, choicesJS);
}

showbuttonbox.co_name = new Sk.builtins['str']('buttonbox');
showbuttonbox.co_varnames = ['msg', 'title', 'choices', 'image'];

var showenterbox = function (msg, title, _default, strip, image) {
    console.log('showenterbox', msg, title, _default, strip, image);
    Sk.builtin.pyCheckArgs('showenterbox', arguments, 0, 5, true, false);
    var msgJS = "(Your message goes here)";
    if (isValid(msg)) {msgJS = Sk.ffi.remapToJs(msg);}
    var titleJS = "";
    if (isValid(title)) {titleJS = Sk.ffi.remapToJs(title);}
    var defaultJS = "";
    if (isValid(_default)) {defaultJS = Sk.ffi.remapToJs(_default);}
    var stripJS = "";
    if (isValid(strip)) {stripJS = Sk.ffi.remapToJs(strip);}
    var imgJS = "";
    if (isValid(image)) {imgJS = Sk.ffi.remapToJs(image);}
    $("#dialog .content").text(msgJS);//弹出文本
    $("#dialog .imgcontent").empty();
    if (imgJS.length > 0){ //关联图像
      var path = getResImage(imgJS);
      $("#dialog .imgcontent").html("<img src='" + path + "' />");
    }
    $("#dialog .attach").show();
    $("#dialog .attach").html("<input id='usercontent' type='text' value='" + defaultJS + "'>");
    var sys = Sk.importModule("sys");
    var guiBox = Sk.importModule("guiBox", false, false);
    console.log('guiBox', guiBox);
    return Sk.misceval.callsimOrSuspend(guiBox, sys["$d"]["stdin"], 2, titleJS, stripJS);
}

showenterbox.co_name = new Sk.builtins['str']('enterbox');
// showenterbox.co_varnames = ['msg', 'title'];
showenterbox.co_kwargs = true;
// showenterbox.$defaults = [new Sk.builtin.str(''), new Sk.builtin.str('')];


function isValid(o) {
    if (typeof(o) != 'undefined' && o != null) {
        return true;
    } else {return false;}
}

function getResImage(picname){
    //先从资源库中寻找
    for(var i=0;i<window.ResList.length;i++){
        if (window.ResList[i].name == picname)
            {return window.ResList[i].url;}
    }
    //再从用户上传文件夹中寻找
    for (var i = 0; i < newImage.length; i++) {
        if (newImage[i].name === picname)
            {return newImage[i].url;}
    }
    //没找到就返回原字符串
    return picname;
}

// //easygui 模块
// function (global, factory) {
//     typeof exports === 'object' && typeof module !== 'undefined' ? module.exports = factory() :
//         typeof define === 'function' && define.amd ? define(factory) :
//             (global.EasyGUI = factory());
// }(this, function () {
//     "use strict";
//     var easyGUI = {
//         main: function () {//easygui主类
//             return {
//                 msgbox: new Sk.builtins.function(showmsgbox),
//                 buttonbox: new Sk.builtins.function(showbuttonbox),
//                 enterbox: new Sk.builtins.function(showenterbox)
//             };
//         }
//     };
//     return easyGUI;
// }),
