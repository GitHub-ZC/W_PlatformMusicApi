##  jQuery

#### jquery 方法

1. filter			过滤  对已经获取的网页元素进行过滤

2. not              filter反义词

3. has              拥有，直接判定子节点中是否有符合条件的元素

4. prev            查找当前兄弟节点中的上一个节点

5. next            查找当前兄弟节点中的下一个节点

6. find             查找子节点

7. index          获取当前节点在兄弟节点中的下标

8. eq                通过下标获取指定的元素节点

   ```javascript
   $('li').eq(3).css('backgroundColor', 'red');
   $('li:eq(3)').css('backgroundColor', 'red');
   ```

9. attr             用来设置和修改元素行间属性，取值赋值一体化(jQuery特性)

   ```javascript
   $('#div').attr('id');		//获取元素的属性
   $('#div').attr('class', 'box');		//修改元素的属性
   $('#div').attr({
       title: 'world',
       class: 'box'
   })						//一次性修改添加多个属性
   ```

10. addClass   removeClass    操作class属性

    ```javascript
    $('#div').addClass('box1 box2');	//自动去重
    $('#div').removeClass('box1 box2')  //即使class没有，自动判断，去重，只删除存在的class属性
    ```

11. 获取元素宽度的四个方法：

    - ```javascript
      $('div').css('width');	//value = 100px
      ```

    - ```javascript
      $('div').width();	//width
      ```

    - ```javascript
      $('div').innerWidth();	//width + padding
      ```

    - ```javascript
      $('div').outerWidth();	//width + padding + border
      ```

    - ```javascript
      $('div').outerWidth(true);	//width + padding + border + margin
      ```

12. 获取元素高度的四个方法：___同上面的width四种方式相对应，举一反三___

13. 节点操作的几种方法：

    > 1\.   insertBefore()  将node1插入到node2之前	before()
    >
    > ```javascript
    > $('div1').insertBefore($('div2'));
    > $('div2').before($('div1'));
    > /*两种方法对于jQuery的链式操作主体不同，主题都是第一种元素，这两种方法就是交换了主语而已*/
    > //下面的后续函数同上一样（都是主语不同，功能相同）
    > ```

    > 2\.   insertAfter()    将node1插入到node2之后    after()
    >
    > ```javascript
    > $('div1').insertAfter($('div2'));
    > ```

    > 3\.   appendTo()     将node插入到子节点末尾    append()
    >
    > ```javascript
    > $('span').appendTo($('div'));
    > ```

    > 4\.   prependTo()    将node插入到子节点首位	prepend()
    >
    > ```javascript
    > $('span').prependTo($('div'));
    > ```

    > 5\.   remove()          将node删除
    >
    > ```javascript
    > $('div').remove();
    > ```

14. jquery事件__底层采用事件监听器添加__可以添加多个事件

15. on 和 off 

    > 1\.   给一个事件添加一个函数
    >
    > ```javascript
    > $('div').on('click', function(){
    >  alert('hello');
    > })
    > ```

    > 2\.   同时给多个事件添加一个函数，多个事件之间可以用空格隔开
    >
    > ```javascript
    > $('div').on('click mouseover', function() {
    >  alert('hello');
    > })
    > ```

    > 3\.   给不同的事件添加不同的函数
    >
    > ```javascript
    > $('div').on({
    >  click: function() {},
    >  mouseover: function() {}
    > })
    > ```

    > 1\.   $('div').off();    取消所有事件上的所有函数
    >
    > 2\.   $('div').off('click')   取消某一个事件下的所有函数
    >
    > 3\.   $('div').off('click', show);   取消某一个事件下的指定函数

16. $(document).scrollTop()         获取当前页面的滚动高度

17. __在jQuery中拿到的任何对象都是兼容后的，不需要考虑兼容性__

18. 事件对象.stopPropagation()      防止事件冒泡

19. 事件对象.preventDefault()         阻止默认事件

    > 当然也可以直接在事件函数中       return  false， 代表上面两种同时作用

20. witch：

    > 鼠标事件： 相当于原生JS的   __button__       0  1  2   鼠标按钮的值
    >
    > keydown：   keyCode    键码       因为keyCode只在keydown、up支持
    >
    > keypress：   charCode   字符码       同理

21. 定位方法：

    > offset()      直接获取当前元素，距离最左边的距离，margin不算
    >
    > position()   直接获取，当前元素，距离第一个有定位元素父节点的距离，margin算数
    >
    > offsetParent()    查找第一个有定位的父节点，最终会定位到body

22. val()

    > 获取/设置单标签元素的值
    >
    > JQ取值只能取第一个符合条件元素的值
    >
    > JQ赋值批量操作，会对所有获取到的标签进行赋值

23. size()、length

    > 获取节点的长度

24. each       jquery的循环

    > ```javascript
    > $('divs').each(function (index, item) {
    >  alert(item + ',' + index);
    > })   /* 注意item是js节点对象，JQ使用需要转换 */
    > ```

25. hover      移入移出效果

    > ```javascript
    > $('div').hover(function(){
    >  //移入
    > }, function() {
    >  //移出
    > })
    > ```

26. 隐藏、显示

    > hide()    隐藏
    >
    > ```javascript
    > $(div).hide();    //参数1：  动画执行的毫秒数；   参数2： 回调函数
    > ```
    >
    > show()   显示
    >
    > ```javascript
    > $(div).show();	  //参数1：   动画执行的毫秒数    参数2： 回调函数
    > ```
    >
    > > 动画从左上角开始，左上角结束

    > slideDown()   
    >
    > ```javascript
    > //同上
    > ```
    >
    > slideUp()
    >
    > ```javascript
    > //同上
    > ```
    >
    > > 动画效果  ‘卷间效果’

    > fadeIn()   淡入
    >
    > fadeOut()   淡出
    >
    > fadeTo(动画持续时间，透明度0-1，回调函数)

27. 动画

    > __animate()__
    >
    > > animate(object，duration，运动形式)
    > >
    > > ```javascript
    > > $('div').stop(true).animate({
    > >                  opacity: 0.5,
    > >                  width: 300
    > >              }, 2000, 'linear')
    > > ```
    >
    > > 默认的运动形式是    慢快慢
    > >
    > > - 匀速    “linear”
    > > - 慢快慢   “swing”
    > > - ___jquery-ui___    是 jQuery的动画扩展库(现在用的比较少，基本被淘汰了)
    >
    > > $().stop()       停止第一个动画，当时后续动画正常运动
    > >
    > > $().stop(true)     停止所有动画
    > >
    > > $().stop(true, true)   停止所有动画，并且将当前正在进行的动画直接到达目的值
    > >
    > > $().finish()            停止所有动画，并且将所有动画都到达目的值
    >
    > delay()     用来延迟动画时间

28. 删除节点

    > ​	remove()   删除节点
    >
    > + 并不会保留这个节点上之前的事件和行为
    >
    > ​    detach()    删除节点
    >
    > + 会保留这个节点上之前的事件和行为

29. > ```javascript
    > $(function () {
    >  //相当于$(document).ready(function() {})
    >  //早于window.onload()执行
    > })
    > ```

30. - jQuery   标签间的内容   html()  相当于innerHTML        可以解析
    - jQuery   标签间纯文本   text()    相当于innerText           不会解析

31. 节点操作方法

    > __[注]:__ 下述所有的方法的参数都是选择器

    > siblings()     获取除当前节点外，所有的兄弟节点
    >
    > nextAll()      获取除当前节点外，下面的所有兄弟节点
    >
    > prevAll()      获取除当前节点外，上面的所有兄弟节点
    >
    > nextUntil("node")      当前节点下面到node的所有兄弟节点
    >
    > prevUntil("node")      当前节点上面到node的所有兄弟节点
    >
    > parentsUntil('node')  当前节点到node的父节点，不包括父节点node

32. > - parent()    获取父节点
    >
    > - parents()   获取父节点们，  参数是选择器
    > - closest()    必须传入参数，  参数是选择器 ，  只获取第一个符合条件的元素

33. 元素节点包装

    > node.wrap()          每一个节点都单独包装     外部包装
    >
    > node.wrapAll()     将所有节点整体包装         外部包装
    >
    > node.wrapInner()   每个节点都单独包装      内部包装
    >
    > node.unwrap()      删除上面一层包装，不包括body节点，没有参数

34. 克隆节点

    > clone()     默认只会克隆节点本身，并不会克隆元素节点的行为和事件
    >
    > clone(true)   即会克隆节点本身，并且克隆元素节点的行为和事件

35. add()    将多个选择器拼接在一起

    > 同分组选择器相似

36. slice()   获取指定范围的元素节点    [1,3)   前开后闭

37. serialize()     将表单的数据拼接成querystring

38. serializeArray()    将表单数据转化成数组

39. 事件、触发对象

    > trigger()          主动触发事件
    >
    > e.target        （兼容后的触发对象）
    >
    > e.type             输出事件类型
    >
    > e.data             jQuery支持事件函数传参，需要配合on函数使用
    >
    > ```javascript
    > $('button').on("click", {username: 'name', age: 18}, function() {
    >  alert(e.data);   //参数对象
    >  alert(e.data.username);   //拿到相关参数
    > });
    > ```
    >
    > trigger()    除了可以主动触发官方事件，还可以触发自定义事件
    >
    > ```javascript
    > $('#play').on('play', function() {
    >  //函数体
    > })
    > 
    > $('#play').trigger('play');   主动触发
    > ```

40. jquery工具方法

    > $.noConflict()    给jQuery起别名
    >
    > $.type()               查询元素类型，比原生js的typeof更加的细化
    >
    > $.inArray()           相对于indexOf()
    >
    > $.parseJSON()      相当于JSON.parse()
    >
    > $.makeArray()       将伪数组转为数组    Array.from()
    >
    > $.proxy()              相当于bind
    >
    > $.trim()                 trim()
    >
    > [注]：基本都是官方引进jQuery方法

41. jquery扩展自己的方法

    > $.extend()       扩展工具方法
    >
    > $.fn.extend()    扩展jq对象方法

42. 
