Sk.builtin.guiBox = function(self,type,title,arg) {
    var x, susp;
    if (type == 0) {
      x = showMsgBox(title, arg);
    } else if (type == 1) {
      x = showButtonBox(title, arg);
    } else if (type == 2) {
      x = showEnterBox(title, arg);
    } else {
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
    this.__class__ = Sk.builtin.guiBox;
};

Sk.abstr.setUpInheritance("guiBox", Sk.builtin.guiBox, Sk.builtin.object);

function showMsgBox(ltitle,lok){
	return new Promise(function (resolve, reject) {
      $("#dialog").dialog({
        autoOpen: true,
        title: ltitle,
        buttons: {
          OK: function() {
            $(this).dialog("close");
            resolve();
          }
        },
        modal: true
      });
      $(".ui-dialog-buttonset .ui-button").text(lok); //按钮文本
      $(".ui-dialog-titlebar-close").click(function() {
        reject();
      });
	})
}

function showButtonBox(ltitle,lchoices){
	return new Promise(function (resolve, reject) {
      $("#dialog").dialog({
        autoOpen: true,
        title: ltitle,
        modal: true
      });
      var btnlist = {};
      for (var i = 0; i < lchoices.length; i++) {
        btnlist["" + lchoices[i] + ""] = function(self) {
          $(this).dialog("close");
          resolve($(self.target).text());
        };
      }
      $("#dialog").dialog("option", "buttons", btnlist);
      $(".ui-dialog-titlebar-close").click(function() {
        reject();
      });
	})
}

function showEnterBox(ltitle,lstrip){
	return new Promise(function (resolve, reject) {
		$("#dialog").dialog({
			autoOpen : true,
			title : ltitle,
			buttons: {
          "确定": function() {
              $(this).dialog("close");
              var txt = $("#dialog #usercontent").val();
              if (lstrip) {
                txt = $.trim(txt);
              }
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
