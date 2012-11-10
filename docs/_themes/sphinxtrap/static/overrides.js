$(document).ready(function(){
    $($("ul.globaltoc > ul > *").get().reverse()).each(function(){$(this).detach().prependTo($("#gtocmenu"))})

    $($("ul.localtoc > ul > li > ul > li").get().reverse()).each(function(){
        $(this).detach().prependTo($("ul#ltocmenu"))
    })
    $("ul.localtoc > ul > li").detach().prependTo($("ul#ltocmenu"))

    $("table").each(function(){
        $(this).attr("border", "0").addClass("table").addClass("table-bordered")
    })
    /*$("p:first-child").css(
        {'-webkit-transform': 'rotate(45deg)',
         'transition': 'width 0.5s, height 2s, transform 2s',
         '-moz-transition': 'width 0.5s, height 2s, -moz-transform 2s',
         '-webkit-transition': 'width 0.5s, height 2s, -webkit-transform 2s',
         '-o-transition': 'width 0.5s, height 2s,-o-transform 2s',
         'transition-timing-function': 'ease-out',
         '-moz-transition-timing-function': 'ease-out',
         '-webkit-transition-timing-function': 'ease-out',
         '-o-transition-timing-function': 'ease-out',
         'right': '-80px',
         'width':'200px',
         'top':'103px',
         'opacity': '0.8',
         'position':'absolute'} )
    */

})
