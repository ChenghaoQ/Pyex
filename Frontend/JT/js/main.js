;$(function()
{
    'use strict';/*严格模式*/
  
    var backbutton=$('.logo'),
        navbar=$('#navbar');

    function backback()
    {
        $('html,body').animate({
            scrollTop:0
        },800)
    }
    function hidebutton()
    {
        if($(window).scrollTop() > $(window).height())
            navbar.fadeIn();
        else
            navbar.fadeOut();
    }

    backbutton.on('click',backback)
    $(window).on('scroll',hidebutton)
    $(window).trigger('scroll');            
                
    var overview = $('li.overview');
    function hidecontent(classfrom,overview){
        
        $(".time").hover(classfrom.hover(),overview.fadeOut());
        classfrom.fadeIn();
        
    }
    function showcontent(classfrom,overview){
        classfrom.fadeOut();
        $(".time").hover(noop,overview.fadeIn());
        
    }
   
    
    $("a.y2011").hover(function(){hidecontent($("li.y2011"),overview)},function(){showcontent($("li.y2011"),overview)})
    $("a.y2012").hover(function(){hidecontent($("li.y2012"),overview)},function(){showcontent($("li.y2012"),overview)})
    $("a.y2013").hover(function(){hidecontent($("li.y2013"),overview)},function(){showcontent($("li.y2013"),overview)})
    $("a.y2014").hover(function(){hidecontent($("li.y2014"),overview)},function(){showcontent($("li.y2014"),overview)})
    $("a.y2015").hover(function(){hidecontent($("li.y2015"),overview)},function(){showcontent($("li.y2015"),overview)})
    $("a.y2016").hover(function(){hidecontent($("li.y2016"),overview)},function(){showcontent($("li.y2016"),overview)})

}) /*自动加载*/