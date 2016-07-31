;$(function()
{
    'use strict';
    var sidebar=$('#sidebar'),
        sidebar_trigger = $('#sidebar_trigger');
    
    function hideSideBar()
    {
        alert('a');
    }
    function showSideBar()
    {
        alert('a');
        sidebar.css('left',0);//== sidebar.css('right',0);sidebar.animate({'right':0});
    }
    sidebar_trigger.on('click',hideSideBar)





})