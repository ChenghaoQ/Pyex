;$(function()
{
    'use strict';
    var sidebar =$('#sidebar'),
        sidebar_trigger = $('#sidebar-trigger'),
        main_page=$('#main-page');
    function showSideBar()
    {
        
        sidebar.css('left',0);
        /*main_page.css('margin-left',sidebar.width());*/
        main_page.animate({'margin-left':sidebar.width()})
    }
    function hideSideBar()
    {
        sidebar.css('left',-sidebar.width());
        main_page.css('margin-left',0);
    }
    function showhideSideBar()
    {
            if(sidebar.css('left')=='0px')
                hideSideBar();
            else  
                showSideBar();
    }
    sidebar_trigger.on('click',showhideSideBar)

    
    /*sidebar_trigger.on('click',showSideBar)*/
})