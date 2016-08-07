(function($)
{
    var privateFun = function(){
        //
    }
    var PageSwitch = (function(){
        function PageSwitch(element,options){
            this.settings =$.extend(true,$.fn.PageSwitch.defualt,options||{});
            this.element = element;
        }
        PageSwitch.prototype ={
            init:function(){
                var me = this;
                me.selectors = me.settings.selectors;
                me.sections = me.selectorss.sections;
                me.section = me.selectors.sections;
                
                me.direction = me.settings.direction == "vertical"? true:false;
                me.pagesCount=me.pagesCount();
                me.index = (me.settings.index>=0 && me.settings.index < me.pagesCount)?me.settings.index:0;/*pagesCount or me.pagesCount*/
                if(!me.direction){
                    me._initLayout();
                    
                }
                if(!me.settings.pagination){
                    me._initPaging();
                }
            },
            pagesCount:function(){
                return me.section.length;
            },
            switchLength:function(){},
            _initLayout : function(){
                var me = this;
                var width = (me.pagesCount*100)+"vl",
                    cellWidth=(100/me.pagesCount).toFixed(2)+"%";
                me.sections.width(width);
                me.section.width(cellWidth).css("float","left");
                
            },
            _initPaging : function(){
                var me = this,
                    pagesClass = me.selectors.page.substring(1)
                var pageHtml = "<ul class="+pagesClass+">";
                for(var i=0;i<me.pagesCount;i++)
                    {
                        pageHtml +="<li><li>";
                    }
            },
            me.element.append(pageHtml);
            var pages = me.element.find(me.selectors.page);
            _initEvent : function(){}
        };
    })
    $.fn.PageSwitch = function(options)
    {
        return this.each(function(){
            var me = $(this)，
                instance = me.data("PageSwitch");
            if(!instance)
                {
                    instance = new PageSwitch(me,options);
                    me.data("PageSwitch",instance);
                }
            if($.type(options)==='string') return instance[options]();
            $("div").PageSwitch("init");
        });
    }
    $.fn.PageSwitch.default = {
        selectors:{
            sections:".sections",
            section:".section",
            page:"pages",
            active:".active"
        },
        index:0,
        easing : "ease",
        duration: 500,
        loop: false,
        pagination : true,
        keyboard:true,
        direction:"vertical",
        callback:""
    }
    $(function(){
        $("[data-PageSwitch]").PageSwitch();
    })
})
