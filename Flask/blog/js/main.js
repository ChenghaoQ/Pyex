;$(function()
{
    'use strict';/*严格模式*/
    
    
    
    var sidebar = $('#sidebar'),//选择侧栏
        backbutton=$('.back-to-top'),
        mask = $('.mask'),
        sidebar_trigger = $('#sidebar_trigger');
    function backback()
    {
        $('html,body').animate({
            scrollTop:0
        },800)
    }
    function hidebutton()
    {
        if($(window).scrollTop() > $(window).height())
            backbutton.fadeIn();
        else
            backbutton.fadeOut();
    }
    function hideSideBar()
    {
        mask.fadeOut();
        sidebar.css('right',-sidebar.width())
    }
    function showSideBar()
    {
        mask.fadeIn();
        sidebar.css('right',0);//== sidebar.css('right',0);sidebar.animate({'right':0});
    }
    
    sidebar_trigger.on('click',showSideBar) //对sidebar_trigger 类进行点击-->点击侧栏
    mask.on('click',hideSideBar)//对mask 类进行点击-->点击mask部分
    backbutton.on('click',backback)
    $(window).on('scroll',hidebutton)
    $(window).trigger('scroll');            
                
                
}) /*自动加载*/