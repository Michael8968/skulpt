// var globalScope = typeof window !== 'undefined' ? window : global;

var $builtinmodule = function (name) {
    var mod = {};

    mod.msgbox = new Sk.builtin.func(showmsgbox);

    mod.buttonbox = new Sk.builtin.func(showbuttonbox);

    mod.enterbox = new Sk.builtin.func(showenterbox);

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
    // return Sk.misceval.callsimOrSuspend(guiBox, sys["$d"]["stdin"], 0, titleJS, okJS);
    return guiBox(sys["$d"]["stdin"], 0, titleJS, okJS);

}

showmsgbox.co_name = new Sk.builtins['str']('msgbox');
showmsgbox.co_varnames = ['msg', 'title', 'ok_button', 'image'];
showmsgbox.$defaults = [new Sk.builtin.str(''), new Sk.builtin.str(''), new Sk.builtin.str('确定'), new Sk.builtin.str('')];

var showbuttonbox = function (msg, title, choices, image) {
    console.log('showbuttonbox', msg, title, choices, image);
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
    // return Sk.misceval.callsimOrSuspend(guiBox, sys["$d"]["stdin"], 1, titleJS, choicesJS);
    // self,type,title,arg
    return guiBox(sys["$d"]["stdin"], 1, titleJS, choicesJS);
}

showbuttonbox.co_name = new Sk.builtins['str']('buttonbox');
showbuttonbox.co_varnames = ['msg', 'title', 'choices', 'image'];
showbuttonbox.$defaults = [new Sk.builtin.str(''), new Sk.builtin.str(''), new Sk.builtin.str(''), new Sk.builtin.str('')];

var showenterbox = function (params) {
    // console.log('showenterbox', msg, title, _default, strip, image);
    Sk.builtin.pyCheckArgs('showenterbox', arguments, 0, 5, true, false);
    var msgJS = "(Your message goes here)";
    if (isValid(params[1])) {msgJS = Sk.ffi.remapToJs(params[1].v);}
    var titleJS = "";
    if (isValid(params[3])) {titleJS = Sk.ffi.remapToJs(params[3].v);}
    var defaultJS = "";
    if (isValid(params[5])) {defaultJS = Sk.ffi.remapToJs(params[5].v);}
    var stripJS = "";
    if (isValid(params[7])) {stripJS = Sk.ffi.remapToJs(params[7].v);}
    var imgJS = "";
    if (isValid(params[9])) {imgJS = Sk.ffi.remapToJs(params[9].v);}
    $("#dialog .content").text(msgJS);//弹出文本
    $("#dialog .imgcontent").empty();
    if (imgJS.length > 0){ //关联图像
      var path = getResImage(imgJS);
      $("#dialog .imgcontent").html("<img src='" + path + "' />");
    }
    $("#dialog .attach").show();
    $("#dialog .attach").html("<input id='usercontent' type='text' value='" + defaultJS + "'>");
    var sys = Sk.importModule("sys");
    // var guiBox = Sk.importModule("guiBox", false, false);
    // return Sk.misceval.callsimOrSuspend(guiBox, sys["$d"]["stdin"], 2, titleJS, stripJS);
    return guiBox(sys["$d"]["stdin"], 2, titleJS, stripJS);
}

showenterbox.co_name = new Sk.builtins['str']('enterbox');
showenterbox.co_kwargs = true;

function isValid(o) {
    if (typeof(o) != 'undefined' && o != null) {
        return true;
    } else {return false;}
}

function getResImage(filename){
    var jsFilename = Sk.ffi.remapToJs(filename);
    var imagePath = jsFilename.includes(window.location.protocol) ?  jsFilename : Sk.imgPath + jsFilename;
    return imagePath;
}

//===============================================
var guiBox = function(self,type,title,arg) {
  console.log('guiBox', type,title,arg);
  var x, susp;
  if(type == 0){
    x = showMsgBox(title,arg);
  }else if(type ==1){
    x = showButtonBox(title,arg);
  }else if(type ==2){
    x = showEnterBox(title,arg);
  }else{
    return Sk.builtin.none.none$;
  }
    if (x instanceof Promise) {//返回的是一个回调对象
        susp = new Sk.misceval.Suspension();//中断处理
        susp.resume = function() {//恢复处理
            if (susp.data.error) {
                throw susp.data.error;
            }
            return new Sk.builtin.str(susp.data.result);//返回得到的结果
        };
        susp.data = {//定义promise对象
            type: "Sk.promise",
            promise: x
        };
        return susp;
    } else {
        return new Sk.builtin.str(x);//如果得到一个字符串则立即返回
    }
};

function showMsgBox(ltitle,lok){
	return new Promise(function (resolve, reject) {
    	$("#dialog").dialog({
    		autoOpen : true,
    		title : ltitle,
    		buttons: {
		        OK: function() {
		          $( this ).dialog( "close" );
		          resolve();
		        }
		    },
    		modal: true
    	});
    	$(".ui-dialog-buttonset .ui-button").text(lok);//按钮文本
    	$(".ui-dialog-titlebar-close").click(function(){
    		 reject();
    	})
	})
}

function showButtonBox(ltitle,lchoices){
	return new Promise(function (resolve, reject) {
    	$("#dialog").dialog({
    		autoOpen : true,
    		title : ltitle,
    		modal: true
    	});
    	var btnlist = {};
    	for(var i=0;i<lchoices.length;i++){
    		btnlist[""+lchoices[i]+""] = function(self) {
	        $( this ).dialog( "close" );
	        resolve($(self.target).text());
	      }
    	}
    	$("#dialog").dialog('option', 'buttons',btnlist);
    	$(".ui-dialog-titlebar-close").click(function(){
    		 reject();
    	})
	})
}

function showEnterBox(ltitle,lstrip){
  console.log('showEnterBox', ltitle,lstrip);
	return new Promise(function (resolve, reject) {
		$("#dialog").dialog({
			autoOpen : true,
			title : ltitle,
			buttons: {
		        "确定": function() {
		          $( this ).dialog( "close" );
		          var txt = $("#dialog #usercontent").val();
		          if(lstrip) {txt = $.trim(txt);}
		          resolve(txt);
		        },
		         "取消": function() {
		          $( this ).dialog( "close" );
		          reject();
		        }
		    },
			modal: true
		});
		$(".ui-dialog-titlebar-close").click(function(){
    		 reject();
    	})
	})
}
