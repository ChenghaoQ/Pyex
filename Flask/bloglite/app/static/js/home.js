;$(function()
{
    'use strict';
    var sidebar =$('#sidebar'),
        sidebar_trigger = $('#sidebar-trigger'),
        backbutton=$('.back-to-top'),
        main_page=$('#main-page');
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
    function showSideBar()
    {
        
        sidebar.css('left',0);
        /*main_page.css('margin-left',sidebar.width());*/
        main_page.animate({'margin-left':sidebar.width()})
        sidebar_trigger.text("☰");
    }
    function hideSideBar()
    {
        sidebar.css('left',-sidebar.width());
        main_page.animate({'margin-left':0})
        sidebar_trigger.text("➤");
    }
    function showhideSideBar()
    {
            if(sidebar.css('left')=='0px')
                hideSideBar();
            else  
                showSideBar();
    }
    sidebar_trigger.on('click',showhideSideBar)
    backbutton.on('click',backback)
    $(window).on('scroll',hidebutton)
    $(window).trigger('scroll')
    
    /*sidebar_trigger.on('click',showSideBar)*/
})