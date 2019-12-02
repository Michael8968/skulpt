// Pinyin2Hanzi 拼音转汉字
var Pinyin2HanziLib = {};
var $builtinmodule = function (name) {
  var mod = {};

  // for (k in pinyinLib) {
  //     mod[k] = Sk.ffi.remapToPy(pinyinLib[k]);
  // }

  mod.Result = Sk.misceval.buildClass(mod, result_type_f, 'Result', []);
  Pinyin2HanziLib.ResultType = mod.Result;

  mod.DefaultDagParams = Sk.misceval.buildClass(mod, defaultDagParams_type_f, 'DefaultDagParams', []);
  Pinyin2HanziLib.DefaultDagParamsType = mod.DefaultDagParams;

  mod.dag = Sk.misceval.buildClass(mod, dag_type_f, 'dag', []);
  Pinyin2HanziLib.DagType = mod.dag;
  // return {
  //   DefaultDagParams : Sk.misceval.callsim(Pinyin2Hanzi.DefaultDagParams,1),
  //   dag : Sk.misceval.callsim(Pinyin2Hanzi.dag)
  // };

  return mod;
};

function result_type_f($gbl, $loc) {
  $loc.__init__ = new Sk.builtin.func(function (self, score, path) {
    // Sk.abstr.sattr(self, 'score', score, false);
    // Sk.abstr.sattr(self, 'path', path, false);
    console.log('result_type_f', score, path);
    self['score'] = Sk.ffi.remapToPy(score);
    self['path'] = Sk.ffi.remapToPy(path);
    return Sk.builtin.none.none$;
  });
  $loc.__init__.co_name = new Sk.builtins['str']('__init__');
  $loc.__init__.co_varnames = ['self', 'score', 'path'];

  $loc.__str__ = new Sk.builtin.func(function (self) {
    return Sk.ffi.remapToPy('<result>');
  });

  $loc.path = new Sk.builtin.func(function (self) {
    var path = self['path'];
    console.log('$loc.path', path, path.v[0]);
    return path.v[0];
  });

  $loc.score = new Sk.builtin.func(function (self) {
    return self['score'];
  });
};

function defaultDagParams_type_f($gbl, $loc) {
  $loc.__init__ = new Sk.builtin.func(function (self) {
    return Sk.builtin.none.none$;
  });
  $loc.__init__.co_name = new Sk.builtins['str']('__init__');
  $loc.__init__.co_varnames = ['self'];

  $loc.__call__ = new Sk.builtin.func(function (self) {
    return  Sk.ffi.remapToPy('<defaultDagParams>');
  });

  $loc.__str__ = new Sk.builtin.func(function (self) {
    return Sk.ffi.remapToPy('<defaultDagParams>');
  });
};

function dag_type_f($gbl, $loc) {
  // $loc.__init__ = new Sk.builtin.func(function (self) {
  // });
  $loc.__init__ = new Sk.builtin.func(function (self, dagParams, pinyinList, pathNum, log) {
      Sk.builtin.pyCheckArgs('__init__', arguments, 3, 5, false, false);
      // console.log('dag', dagParams);
      // console.log('dag', pinyinList);
      // console.log('dag', pathNum);
      var jsListpinyin = Sk.ffi.remapToJs(pinyinList);
      var pinyinStr = "";
      for (var i = 0; i < jsListpinyin.length; i++) {
        pinyinStr += jsListpinyin[i];
      }
      var resultList = [];
      for (var i = 0; i < Pinyin2HanziLib.pinyinLib.length; i++) {
        if (Pinyin2HanziLib.pinyinLib[i].pinyin == pinyinStr){
          for (var j = 0; j < Pinyin2HanziLib.pinyinLib[i].hanzi.length; j++) {
            var hanzi = Pinyin2HanziLib.pinyinLib[i].hanzi[j];
            var list1 = []
            for (var k = 0; k < hanzi.path.length; k++) {
              // var str1 = Sk.ffi.remapToPy(hanzi.path[k]);
              list1.push(hanzi.path[k]);
            }
            // var l1 = new Sk.builtin.list(list1);
            // console.log('hanzi.score', hanzi.score);
            // console.log('list1', list1);
            resultList.push(new Sk.misceval.callsim(Pinyin2HanziLib.ResultType, hanzi.score, list1));
          }
        }
      }

      self['results'] = new Sk.builtin.list(resultList);
      // return Sk.ffi.remapToPy(_buffer);
      // self['results'] = Sk.ffi.remapToPy(_buffer);
      // console.log('results', self['results']);
      return Sk.builtin.none.none$;
  });
  $loc.__init__.co_name = new Sk.builtins['str']('__init__');
  $loc.__init__.co_varnames = ['self', 'dagParams', 'pinyinList', 'pathNum', 'log'];

  $loc.__str__ = new Sk.builtin.func(function (self) {
      return Sk.ffi.remapToPy('<dag>');
  });

  $loc.__getitem__ = new Sk.builtin.func(function (self, k) {
      var results = self['results'];
      // var jsresults = Sk.ffi.remapToJs(results);
      var index = Sk.ffi.remapToJs(k);
      var result = results[index];
      console.log('__getitem__', index, result, results);
      return result;
  });

};

Pinyin2HanziLib.pinyinLib  = [
   {
       pinyin: "laohu",
       hanzi: [{path:['老虎'],score:1},
               {path:['老湖'],score:2},
               {path:['老胡'],score:3}]
   },{
       pinyin: "shizi",
       hanzi: [{path:['狮子'],score:1},
               {path:['师资'],score:2},
               {path:['十字'],score:3}]
   },{
       pinyin: "she",
       hanzi: [{path:['蛇'],score:1},
               {path:['设'],score:2},
               {path:['舌'],score:3}]
   },{
       pinyin: "hama",
       hanzi: [{path:['蛤蟆'],score:1},
               {path:['哈码'],score:2},
               {path:['蛤吗'],score:3}]
   },{
       pinyin: "laoshu",
       hanzi: [{path:['老鼠'],score:1},
               {path:['老叔'],score:2},
               {path:['老树'],score:3}]
   },{
       pinyin: "zhizhu",
       hanzi: [{path:['蜘蛛'],score:1},
               {path:['之主'],score:2},
               {path:['支柱'],score:3}]
   },{
       pinyin: "chou",
       hanzi: [{path:['丑'],score:1},
               {path:['抽'],score:2},
               {path:['愁'],score:3}]
   },{
       pinyin: "keai",
       hanzi: [{path:['可爱'],score:1},
               {path:['柯哀'],score:2},
               {path:['课爱'],score:3}]
   },{
       pinyin: "meili ",
       hanzi: [{path:['美丽'],score:1},
               {path:['魅力'],score:2},
               {path:['没理'],score:3}]
   },{
       pinyin: "xiongmeng",
       hanzi: [{path:['凶猛'],score:1},
               {path:['胸猛'],score:2},
               {path:['熊梦'],score:3}]
   },{
       pinyin: "qinlao",
       hanzi: [{path:['勤劳'],score:1},
               {path:['秦老'],score:2},
               {path:['亲老'],score:3}]
   },{
       pinyin: "jingjue",
       hanzi: [{path:['警觉'],score:1},
               {path:['金爵'],score:2},
               {path:['惊厥'],score:3}]
   },{
       pinyin: "tou",
       hanzi: [{path:['头'],score:1},
               {path:['偷'],score:2},
               {path:['投'],score:3}]
   },{
       pinyin: "chibang",
       hanzi: [{path:['翅膀'],score:1},
               {path:['吃邦'],score:2},
               {path:['迟棒'],score:3}]
   },{
       pinyin: "jiaozhi",
       hanzi: [{path:['脚趾'],score:1},
               {path:['交至'],score:2},
               {path:['胶纸'],score:3}]
   },{
       pinyin: "zuiba",
       hanzi: [{path:['嘴巴'],score:1},
               {path:['最拔'],score:2},
               {path:['嘴吧'],score:3}]
   },{
       pinyin: "bizi",
       hanzi: [{path:['鼻子'],score:1},
               {path:['篦子'],score:2},
               {path:['箅子'],score:3}]
   },{
       pinyin: "yanjing",
       hanzi: [{path:['眼睛'],score:1},
               {path:['眼镜'],score:2},
               {path:['燕京'],score:3}]
   },{
       pinyin: "xiaomao",
       hanzi: [{path:['小猫'],score:1},
               {path:['小毛'],score:2},
               {path:['笑毛'],score:3}]
   },{
       pinyin: "shizi",
       hanzi: [{path:['狮子'],score:1},
               {path:['师资'],score:2},
               {path:['十字'],score:3}]
   },{
       pinyin: "xiaogou",
       hanzi: [{path:['小狗'],score:1},
               {path:['小沟'],score:2},
               {path:['小勾'],score:3}]
   },{
       pinyin: "jinyu",
       hanzi: [{path:['金鱼'],score:1},
               {path:['金域'],score:2},
               {path:['金宇'],score:3}]
   },{
       pinyin: "xiongmao",
       hanzi: [{path:['熊猫'],score:1},
               {path:['胸毛'],score:2},
               {path:['熊冒'],score:3}]
   },{
       pinyin: "tuzi",
       hanzi: [{path:['兔子'],score:1},
               {path:['秃子'],score:2},
               {path:['吐字'],score:3}]
   },{
       pinyin: "yingwu",
       hanzi: [{path:['鹦鹉'],score:1},
               {path:['硬物'],score:2},
               {path:['影舞'],score:3}]
   },{
       pinyin: "lian",
       hanzi: [{path:['脸'],score:1},
               {path:['练'],score:2},
               {path:['链'],score:3}]
   },{
       pinyin: "shoubi",
       hanzi: [{path:['手臂'],score:1},
               {path:['首笔'],score:2},
               {path:['手笔'],score:3}]
   },{
       pinyin: "maofa",
       hanzi: [{path:['毛发'],score:1},
               {path:['茂发'],score:2},
               {path:['猫发'],score:3}]
   },{
       pinyin: "sizhi",
       hanzi: [{path:['四肢'],score:1},
               {path:['四只'],score:2},
               {path:['四至'],score:3}]
   },{
       pinyin: "chujiao",
       hanzi: [{path:['触角'],score:1},
               {path:['出脚'],score:2},
               {path:['初教'],score:3}]
   },{
       pinyin: "weiba",
       hanzi: [{path:['尾巴'],score:1},
               {path:['微吧'],score:2},
               {path:['唯八'],score:3}]
   },{
       pinyin: "jitui",
       hanzi: [{path:['鸡腿'],score:1},
               {path:['击退'],score:2},
               {path:['几忒'],score:3}]
   },{
       pinyin: "shupian",
       hanzi: [{path:['薯片'],score:1},
               {path:['数骗'],score:2},
               {path:['树便'],score:3}]
   },{
       pinyin: "huoguo",
       hanzi: [{path:['火锅'],score:1},
               {path:['活过'],score:2},
               {path:['获过'],score:3}]
   },{
       pinyin: "jiaozi",
       hanzi: [{path:['饺子'],score:1},
               {path:['教资'],score:2},
               {path:['娇子'],score:3}]
   },{
       pinyin: "pingguo",
       hanzi: [{path:['苹果'],score:1},
               {path:['平果'],score:2},
               {path:['平锅'],score:3}]
   },{
       pinyin: "xigua",
       hanzi: [{path:['西瓜'],score:1},
               {path:['西噶'],score:2},
               {path:['系挂'],score:3}]
   },{
       pinyin: "pao",
       hanzi: [{path:['跑'],score:1},
               {path:['泡'],score:2},
               {path:['炮'],score:3}]
   },{
       pinyin: "zou",
       hanzi: [{path:['走'],score:1},
               {path:['揍'],score:2},
               {path:['邹'],score:3}]
   },{
       pinyin: "tiao",
       hanzi: [{path:['跳'],score:1},
               {path:['调'],score:2},
               {path:['条'],score:3}]
   },{
       pinyin: "sanbu",
       hanzi: [{path:['散步'],score:1},
               {path:['三部'],score:2},
               {path:['散布'],score:3}]
   },{
       pinyin: "tangxia",
       hanzi: [{path:['躺下'],score:1},
               {path:['塘厦'],score:2},
               {path:['棠下'],score:3}]
   },{
       pinyin: "dunxia",
       hanzi: [{path:['蹲下'],score:1},
               {path:['炖虾'],score:2},
               {path:['炖下'],score:3}]
   }
 ];
