var $builtinmodule = function (name) {
    //精灵对象的简单基类
    sprite_locs.Sprite = SpriteClass(sprite_locs);
    sprite_locs.Sprite.$isclass = true;
    //用于保存和管理多个Sprite对象的容器类
    sprite_locs.Group = GroupClass(sprite_locs);
    sprite_locs.Group.$isclass = true;
    //初始化所有容器
    allGroups = [];
    return sprite_locs;
};

var allGroups = [];//所有的精灵组(全局)


var notImplemented = new Sk.builtin.func(function () {
    throw new Sk.builtin.NotImplementedError("Not yet implemented");
});

//添加数组，去重复
function addArray(_arr, _obj) {
    var id = getIndex(_arr, _obj);
    if (id < 0) {//如果没有才可以添加
        return _arr.push(_obj);
    }
    return -1;
}
//获取数据索引
function getIndex(_arr, _obj) {
    if (!$.isArray(_arr)) {return -1;}
    var len = _arr.length;
    for (var i = 0; i < len; i++) {
        if (_arr[i] == _obj) {
            return parseInt(i);
        }
    }
    return -1;
}

//删除数组元素
function removeArray(_arr, _obj) {
    if (!$.isArray(_arr)) {return -1;}
    var length = _arr.length;
    for (var i = 0; i < length; i++) {
        if (_arr[i] == _obj) {
            if (i == 0) {
                _arr.shift(); //删除并返回数组的第一个元素
                return _arr;
            } else if (i == length - 1) {
                _arr.pop();  //删除并返回数组的最后一个元素
                return _arr;
            } else {
                _arr.splice(i, 1); //删除下标为i的元素
                return _arr;
            }
        }
    }
}
//数组切片
var slicedToArray = function () {
    function sliceIterator(arr, i) {
        var _arr = [];
        var _n = true;
        var _d = false;
        var _e = undefined;
        try {
            for (var _i = arr[Symbol.iterator](), _s; !(_n = (_s = _i.next()).done); _n = true) {
                _arr.push(_s.value);
                if (i && _arr.length === i) {break;}
            }
        } catch (err) {
            _d = true;
            _e = err;
        } finally {
            try {
                if (!_n && _i["return"]) {_i["return"]();}
            } finally {
                if (_d) {throw _e;}
            }
        }
        return _arr;
    }

    return function (arr, i) {
        if (Array.isArray(arr)) {
            return arr;
        } else if (Symbol.iterator in Object(arr)) {
            return sliceIterator(arr, i);
        } else {
            throw new TypeError("无效尝试解构非可迭代实例");
        }
    };
}();

//创建一个sprite类
var SpriteClass = function (gbl) {
    return Sk.misceval.buildClass(gbl, sprite$1, 'Sprite', []);
};

//初始化Sprite
var initSprite = function (self) {
    self.offscreen_canvas = document.createElement('canvas');
    self.context2d = self.offscreen_canvas.getContext("2d");

    self.offscreen_canvas.width = self.width;
    self.offscreen_canvas.height = self.height;

    return Sk.builtin.none.none$;
};
initSprite.co_name = new Sk.builtins['str']('__init__');
initSprite.co_varnames = ['self'];

//串行化Sprite
var reprSprite = function (self) {
    try {
        var spriteRect = Sk.builtin.getattr(self, Sk.ffi.remapToPy("rect"));
        return Sk.ffi.remapToPy('<Sprite(' +
            Sk.ffi.remapToJs(spriteRect.left) + "," +
            Sk.ffi.remapToJs(spriteRect.top) + "," +
            Sk.ffi.remapToJs(spriteRect.width) + "," +
            Sk.ffi.remapToJs(spriteRect.height) +
            ')>');
    } catch (error) {
        return Sk.ffi.remapToPy('<Sprite()>');
    }
};
reprSprite.co_name = new Sk.builtins['str']('__repr__');
reprSprite.co_varnames = ['self'];

//控制精灵行为的方法(空操作等待覆盖)
function update(self, args) {
    return Sk.builtin.none.none$;
}

update.co_name = new Sk.builtins['str']('update');
update.co_varnames = ['self', 'args'];

//将精灵添加到这些组
function add(self, groups) {
    if (!Sk.builtin.checkIterable(groups)) {
        if (!isVaild(groups.spritelist)) {groups.spritelist = [];}
        addArray(groups.spritelist, self);
    } else {
        var it, i;
        for (it = Sk.abstr.iter(groups), i = it.tp$iternext();
             i !== undefined; i = it.tp$iternext()) {
            if (!isVaild(i.spritelist)) {i.spritelist = [];}
            addArray(i.spritelist, self);
        }
    }
}

add.co_name = new Sk.builtins['str']('add');
add.co_varnames = ['self', 'groups'];

//从这些组内删除精灵
function remove(self, groups) {
    if (!Sk.builtin.checkIterable(groups)) {
        removeArray(groups.spritelist, self);
    } else {
        var it, i;
        for (it = Sk.abstr.iter(groups), i = it.tp$iternext();
             i !== undefined; i = it.tp$iternext()) {
            removeArray(i.spritelist, self);
        }
    }
}

remove.co_name = new Sk.builtins['str']('remove');
remove.co_varnames = ['self', 'groups'];

//从所有组中删除精灵
function kill(self) {
    allGroups.forEach(function (group) {
        removeArray(group.spritelist, self);
    });
}

kill.co_name = new Sk.builtins['str']('kill');
kill.co_varnames = ['self'];

//判断精灵是否存在于任何组内
function alive(self) {
    var result = false;
    allGroups.forEach(function (group) {
        if (getIndex(group.spritelist, self) > -1)
            {result = true;}
    });
    return Sk.ffi.remapToPy(result);
}

alive.co_name = new Sk.builtins['str']('alive');
alive.co_varnames = ['self'];

//包含此Sprite的组列表
function groups(self) {
    var result = [];
    allGroups.forEach(function (group) {
        if (getIndex(group.spritelist, self) > -1)
            {result.push(group);}
    });
    return Sk.ffi.remapToPy(result);
}

groups.co_name = new Sk.builtins['str']('groups');
groups.co_varnames = ['self'];

var sprite$1 = function $SpriteType$class_outer(gbl, loc) {
    loc.__init__ = new Sk.builtins.function(initSprite, gbl);
    loc.__repr__ = new Sk.builtins.function(reprSprite, gbl);
    loc.update = new Sk.builtins.function(update, gbl);
    loc.add = new Sk.builtins.function(add, gbl);
    loc.remove = new Sk.builtins.function(remove, gbl);
    loc.kill = new Sk.builtins.function(kill, gbl);
    loc.alive = new Sk.builtins.function(alive, gbl);
    loc.groups = new Sk.builtins.function(groups, gbl);

    var rect_getter = new Sk.builtin.func(function(self) {
      return self["rect"];
    });
    var rect_setter = new Sk.builtin.func(function(self, val) {
      self["rect"] = val;
    });
    loc.rect = Sk.misceval.callsimOrSuspend(Sk.builtins.property, rect_getter, rect_setter);

    var image_getter = new Sk.builtin.func(function(self) {
      return self["image"];
    });
    var image_setter = new Sk.builtin.func(function(self, val) {
      self["image"] = val;
    });
    loc.image = Sk.misceval.callsimOrSuspend(Sk.builtins.property, image_getter, image_setter);

    var canvas_getter = new Sk.builtin.func(function(self) {
      return self["canvas"];
    });
    var canvas_setter = new Sk.builtin.func(function(self, val) {
      self["canvas"] = val;
    });
    loc.canvas = Sk.misceval.callsimOrSuspend(Sk.builtins.property, canvas_getter, canvas_setter);

    return;
};
sprite$1.co_name = new Sk.builtins['str']('Sprite');

//py创建一个Group类
var GroupClass = function (gbl) {
    return Sk.misceval.buildClass(gbl, group$1, 'Group', []);
};

//初始化
var initGroup = function (self) {
    allGroups.push(self);
    self.spritelist = [];
};
initGroup.co_name = new Sk.builtins['str']('__init__');
initGroup.co_varnames = ['self'];

//字串
var reprGroup = function (self) {
    return Sk.ffi.remapToPy('<Group(' + self.spritelist.length + ')>');
};
reprGroup.co_name = new Sk.builtins['str']('__repr__');
reprGroup.co_varnames = ['self'];

//此组包含的精灵列表
function sprites(self) {
    return Sk.ffi.remapToPy(self.spritelist);
}

sprites.co_name = new Sk.builtins['str']('sprites');
sprites.co_varnames = ['self'];

//复制本组
function copy(self) {
    var newGroup = Sk.misceval.callsim(sprite_locs.Group);
    newGroup.spritelist = self.spritelist;
    return newGroup;
}

copy.co_name = new Sk.builtins['str']('copy');
copy.co_varnames = ['self'];

//将精灵添加到组
function addgroup(self, sprites) {
    if (!Sk.builtin.checkIterable(sprites)) {
        addArray(self.spritelist, sprites);
    } else {
        var it, i;
        for (it = Sk.abstr.iter(sprites), i = it.tp$iternext();
             i !== undefined; i = it.tp$iternext()) {
            addArray(self.spritelist, i);
        }
    }
}

addgroup.co_name = new Sk.builtins['str']('add');
addgroup.co_varnames = ['self', 'sprites'];

//从组中删除精灵
function removegroup(self, sprites) {
    if (!Sk.builtin.checkIterable(sprites)) {
        removeArray(self.spritelist, sprites);
    } else {
        var it, i;
        for (it = Sk.abstr.iter(sprites), i = it.tp$iternext();
             i !== undefined; i = it.tp$iternext()) {
            removeArray(self.spritelist, i);
        }
    }
}

removegroup.co_name = new Sk.builtins['str']('remove');
removegroup.co_varnames = ['self', 'sprites'];

//轮流循环精灵的update方法
function updategroup(self,args) {
self.spritelist.forEach(function (sprite) {
if(Sk.builtin.checkCallable(sprite.update))
	{Sk.misceval.callsim(sprite.update,sprite,args);}
})
}
updategroup.co_name = new Sk.builtins['str']('update');
updategroup.co_varnames = ['self', 'args'];

//判断组内是否包含精灵
function has(self, sprites) {
    var result = false;
    if (!Sk.builtin.checkIterable(sprites)) {
        if (getIndex(self.spritelist, sprites) > -1)
            {result = true;}
    } else {
        var it, i;
        for (it = Sk.abstr.iter(sprites), i = it.tp$iternext();
             i !== undefined; i = it.tp$iternext()) {
            if (getIndex(self.spritelist, i) > -1)
                {result = true;}
        }
    }
    return Sk.ffi.remapToPy(result);
}

has.co_name = new Sk.builtins['str']('has');
has.co_varnames = ['self', 'sprites'];

//绘制精灵图像
function drawgroup(self, Surface) {
    // var ctx = Surface.canvas.getContext("2d");
    // var ctx = Sk.main_canvas.getContext("2d");
    var ctx = Surface.offscreen_canvas.getContext("2d");

    self.spritelist.forEach(function (sprite) {
        var img = sprite.image;
        // console.log('sprite.image', sprite.image);
        // var t = Sk.builtin.tuple([img.width, img.height]);
        // var s = Sk.misceval.callsim(PygameLib.SurfaceType, t);
        // var ctx = s.offscreen_canvas.getContext("2d");
        // var rect = Sk.abstr.gattr(sprite, 'rect', false);
        // var image = Sk.abstr.gattr(sprite, 'image', false);
        var rect = sprite.rect;
        // console.log('drawgroup', rect);

        var sx = Sk.ffi.remapToJs(rect.left);
        var sy = Sk.ffi.remapToJs(rect.top);
        var swidth = Sk.ffi.remapToJs(rect.width);
        var sheight = Sk.ffi.remapToJs(rect.height);
        // ctx.drawImage(sprite.canvas, sx, sy, swidth, sheight);
        // ctx.drawImage(Sk.main_canvas, sx, sy, swidth, sheight);
        ctx.drawImage(img.offscreen_canvas, sx, sy, swidth, sheight);
        // ctx.drawImage(img.main_canvas, sx, sy, swidth, sheight);
    });
}

drawgroup.co_name = new Sk.builtins['str']('draw');
drawgroup.co_varnames = ['self', 'Surface'];

//绘制精灵背景
function clear(self, background) {
    //解析传入的颜色
    var color_Js = Sk.ffi.remapToJs(background);
    var color_Js3 = slicedToArray(color_Js, 3);
    var r = color_Js3[0];
    var g = color_Js3[1];
    var b = color_Js3[2];
    //获取将要被绘制的画布并绘制
    // var ctx = self.image.canvas.getContext("2d");
    var ctx = self.image.offscreen_canvas.getContext("2d");
    ctx.fillStyle = 'rgb(' + r + ',' + g + ',' + b + ')';
    self.spritelist.forEach(function (sprite) {
        var left = Sk.ffi.remapToJs(sprite.rect.left);
        var top = Sk.ffi.remapToJs(sprite.rect.top);
        var width = Sk.ffi.remapToJs(sprite.rect.width);
        var height = Sk.ffi.remapToJs(sprite.rect.height);
        ctx.fillRect(left, top, width, height);
    });
}

clear.co_name = new Sk.builtins['str']('clear');
clear.co_varnames = ['self', 'background'];

//从组中删除所有精灵
function empty(self) {
    self.spritelist = [];
}

empty.co_name = new Sk.builtins['str']('empty');
empty.co_varnames = ['self'];

var group$1 = function $SpriteType$class_outer(gbl, loc) {
    loc.__init__ = new Sk.builtins.function(initGroup, gbl);
    loc.__repr__ = new Sk.builtins.function(reprGroup, gbl);
    loc.sprites = new Sk.builtins.function(sprites, gbl);
    loc.copy = new Sk.builtins.function(copy, gbl);
    loc.update = new Sk.builtins.function(updategroup, gbl);
    loc.add = new Sk.builtins.function(addgroup, gbl);
    loc.remove = new Sk.builtins.function(removegroup, gbl);
    loc.has = new Sk.builtins.function(has, gbl);
    loc.draw = new Sk.builtins.function(drawgroup, gbl);
    loc.clear = new Sk.builtins.function(clear, gbl);
    loc.empty = new Sk.builtins.function(empty, gbl);
    return;
};
group$1.co_name = new Sk.builtins['str']('Group');

var sprite_locs = {
    '__package__': Sk.builtin.none.none$,
    '__doc__': 'pygame 用于显示动画精灵',
    '__name__': 'pygame.sprite',

    collide_rect : function(left, right){
        var maxX,maxY,minX,minY;
        var rect1 = {};
        var rect2 = {};
        var leftRect = Sk.builtin.getattr(left,Sk.ffi.remapToPy("rect"));
        var rightRect = Sk.builtin.getattr(right,Sk.ffi.remapToPy("rect"));
         rect1.x = Sk.ffi.remapToJs(leftRect.left);
        rect1.y = Sk.ffi.remapToJs(leftRect.top);
        rect1.width = Sk.ffi.remapToJs(leftRect.width);
        rect1.height = Sk.ffi.remapToJs(leftRect.height);
        rect2.x = Sk.ffi.remapToJs(rightRect.left);
        rect2.y = Sk.ffi.remapToJs(rightRect.top);
        rect2.width = Sk.ffi.remapToJs(rightRect.width);
        rect2.height = Sk.ffi.remapToJs(rightRect.height);
      maxX = rect1.x+rect1.width >= rect2.x+rect2.width ? rect1.x+rect1.width : rect2.x+rect2.width;
      maxY = rect1.y+rect1.height >= rect2.y+rect2.height ? rect1.y+rect1.height : rect2.y+rect2.height;
      minX = rect1.x <= rect2.x ? rect1.x : rect2.x;
      minY = rect1.y <= rect2.y ? rect1.y : rect2.y;
      if(maxX - minX <= rect1.width+rect2.width && maxY - minY <= rect1.height+rect2.height){
            return Sk.ffi.remapToPy(true);
      }else{
            return Sk.ffi.remapToPy(false);
        }
    },

    //精灵之间的碰撞检测，使用圆形
    collide_circle : function(left, right){
        var rect1 = {};
        var rect2 = {};
        var leftRect = Sk.builtin.getattr(left,Sk.ffi.remapToPy("rect"));
        var rightRect = Sk.builtin.getattr(right,Sk.ffi.remapToPy("rect"));
        rect1.x = Sk.ffi.remapToJs(leftRect.left);
        rect1.y = Sk.ffi.remapToJs(leftRect.top);
        rect1.width = Sk.ffi.remapToJs(leftRect.width);
        rect1.height = Sk.ffi.remapToJs(leftRect.height);
        rect2.x = Sk.ffi.remapToJs(rightRect.left);
        rect2.y = Sk.ffi.remapToJs(rightRect.top);
        rect2.width = Sk.ffi.remapToJs(rightRect.width);
        rect2.height = Sk.ffi.remapToJs(rightRect.height);
        if(!isVaild(left.radius)) {left.radius = parseInt(rect1.width/2);}
        if(!isVaild(right.radius)) {right.radius = parseInt(rect2.width/2);}
        if(Math.sqrt(Math.pow(rect1.x-rect2.x, 2) + Math.pow(rect1.y-rect2.y, 2)) <= (left.radius+right.radius)){
            return Sk.ffi.remapToPy(true);
        }else{
            return Sk.ffi.remapToPy(false);
        }
    },

    //精灵之间的碰撞检测掩码
    collide_mask : function(left, right){
        var maxX,maxY,minX,minY;
        var rect1 = {};
        var rect2 = {};
        var leftRect = Sk.builtin.getattr(left,Sk.ffi.remapToPy("rect"));
        var rightRect = Sk.builtin.getattr(right,Sk.ffi.remapToPy("rect"));
         rect1.x = Sk.ffi.remapToJs(leftRect.left);
        rect1.y = Sk.ffi.remapToJs(leftRect.top);
        rect1.width = Sk.ffi.remapToJs(leftRect.width);
        rect1.height = Sk.ffi.remapToJs(leftRect.height);
        rect2.x = Sk.ffi.remapToJs(rightRect.left);
        rect2.y = Sk.ffi.remapToJs(rightRect.top);
        rect2.width = Sk.ffi.remapToJs(rightRect.width);
        rect2.height = Sk.ffi.remapToJs(rightRect.height);
      maxX = rect1.x+rect1.width >= rect2.x+rect2.width ? rect1.x+rect1.width : rect2.x+rect2.width;
      maxY = rect1.y+rect1.height >= rect2.y+rect2.height ? rect1.y+rect1.height : rect2.y+rect2.height;
      minX = rect1.x <= rect2.x ? rect1.x : rect2.x;
      minY = rect1.y <= rect2.y ? rect1.y : rect2.y;
      if(maxX - minX <= rect1.width+rect2.width && maxY - minY <= rect1.height+rect2.height){
            return Sk.ffi.remapToPy(true);
      }else{
            return Sk.ffi.remapToPy(false);
        }
    },

    //在与另一个精灵相交的组中查找精灵
    spritecollide : function(sprite,group,dokill,collided){

        var maxX,maxY,minX,minY;
        var rect1={};
        var spriteRect = Sk.builtin.getattr(sprite,Sk.ffi.remapToPy("rect"));
        rect1.x = Sk.ffi.remapToJs(spriteRect.left);
        rect1.y = Sk.ffi.remapToJs(spriteRect.top);
        rect1.width = Sk.ffi.remapToJs(spriteRect.width);
        rect1.height = Sk.ffi.remapToJs(spriteRect.height);
        var Iskill = Sk.ffi.remapToJs(dokill);
        var result =[];

        var rectlist = group.spritelist;
        for(var i= rectlist.length-1;i>=0;i--){
            var rect2={};
            var spriteRect2 = Sk.builtin.getattr(rectlist[i],Sk.ffi.remapToPy("rect"));
            rect2.x = Sk.ffi.remapToJs(spriteRect2.left);
            rect2.y = Sk.ffi.remapToJs(spriteRect2.top);
            rect2.width = Sk.ffi.remapToJs(spriteRect2.width);
            rect2.height = Sk.ffi.remapToJs(spriteRect2.height);
          maxX = rect1.x+rect1.width >= rect2.x+rect2.width ? rect1.x+rect1.width : rect2.x+rect2.width;
          maxY = rect1.y+rect1.height >= rect2.y+rect2.height ? rect1.y+rect1.height : rect2.y+rect2.height;
          minX = rect1.x <= rect2.x ? rect1.x : rect2.x;
          minY = rect1.y <= rect2.y ? rect1.y : rect2.y;
          if(maxX - minX <= rect1.width+rect2.width && maxY - minY <= rect1.height+rect2.height){
                result.push(rectlist[i]);
                if(Iskill) {rectlist.splice(i, 1);}
          }
        }
        return Sk.ffi.remapToPy(result);
    },

    //发现两个组内所有的精灵碰撞
    groupcollide : function(group1,group2,dokill1,dokill2,collided){

        var maxX,maxY,minX,minY;
        var Iskill1 = Sk.ffi.remapToJs(dokill1);
        var Iskill2 = Sk.ffi.remapToJs(dokill2);
        var rectlist1 = group1.spritelist;
        var rectlist2 = group2.spritelist;
        var result = [];

        for(var i1= rectlist1.length-1;i1>=0;i1--){
            for(var i2= rectlist2.length-1;i2>=0;i2--){
                var rect1={};
                var spriteRect1 = Sk.builtin.getattr(rectlist1[i1],Sk.ffi.remapToPy("rect"));
                rect1.x = Sk.ffi.remapToJs(spriteRect1.left);
                rect1.y = Sk.ffi.remapToJs(spriteRect1.top);
                rect1.width = Sk.ffi.remapToJs(spriteRect1.width);
                rect1.height = Sk.ffi.remapToJs(spriteRect1.height);
                var rect2={};
                var spriteRect2 = Sk.builtin.getattr(rectlist2[i2],Sk.ffi.remapToPy("rect"));
                rect2.x = Sk.ffi.remapToJs(spriteRect2.left);
                rect2.y = Sk.ffi.remapToJs(spriteRect2.top);
                rect2.width = Sk.ffi.remapToJs(spriteRect2.width);
                rect2.height = Sk.ffi.remapToJs(spriteRect2.height);
                maxX = rect1.x+rect1.width >= rect2.x+rect2.width ? rect1.x+rect1.width : rect2.x+rect2.width;
                maxY = rect1.y+rect1.height >= rect2.y+rect2.height ? rect1.y+rect1.height : rect2.y+rect2.height;
                minX = rect1.x <= rect2.x ? rect1.x : rect2.x;
                minY = rect1.y <= rect2.y ? rect1.y : rect2.y;
                if(maxX - minX <= rect1.width+rect2.width && maxY - minY <= rect1.height+rect2.height){
                    result.push(rectlist1[i1]);
                    result.push(rectlist2[i2]);
                    if(Iskill2) {rectlist2.splice(i2, 1);}
                    if(Iskill1) {
                        rectlist1.splice(i1, 1);
                        return new Sk.builtin.dict(result);
                    }
                }
            }
        }
        return new Sk.builtin.dict(result);
    },

    //在与另一个精灵相交的组中查找精灵(找到立即返回)
    spritecollideany : function(sprite,group){
        var maxX,maxY,minX,minY;
        var rect1={};
        var spriteRect = Sk.builtin.getattr(sprite,Sk.ffi.remapToPy("rect"));
        rect1.x = Sk.ffi.remapToJs(spriteRect.left);
        rect1.y = Sk.ffi.remapToJs(spriteRect.top);
        rect1.width = Sk.ffi.remapToJs(spriteRect.width);
        rect1.height = Sk.ffi.remapToJs(spriteRect.height);

        var rectlist = group.spritelist;
        for(var i=0;i<rectlist.length;i++){
            var rect2={};
            var spriteRect2 = Sk.builtin.getattr(rectlist[i],Sk.ffi.remapToPy("rect"));
            rect2.x = Sk.ffi.remapToJs(spriteRect2.left);
            rect2.y = Sk.ffi.remapToJs(spriteRect2.top);
            rect2.width = Sk.ffi.remapToJs(spriteRect2.width);
            rect2.height = Sk.ffi.remapToJs(spriteRect2.height);
          maxX = rect1.x+rect1.width >= rect2.x+rect2.width ? rect1.x+rect1.width : rect2.x+rect2.width;
          maxY = rect1.y+rect1.height >= rect2.y+rect2.height ? rect1.y+rect1.height : rect2.y+rect2.height;
          minX = rect1.x <= rect2.x ? rect1.x : rect2.x;
          minY = rect1.y <= rect2.y ? rect1.y : rect2.y;
          if(maxX - minX <= rect1.width+rect2.width && maxY - minY <= rect1.height+rect2.height){
                return rectlist[i];
          }
        }
        return Sk.builtin.none.none$;
    },

    //精灵之间的碰撞检测，使用矩形比例
    collide_rect_ratio : notImplemented,
    //精灵之间的碰撞检测，使用圆形比例
    collide_circle_ratio : notImplemented,
    'SpriteType': notImplemented,
    '_PYGAME_C_API': notImplemented
};
