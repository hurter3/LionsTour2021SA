$(document).ready(function () {

   
    /**
     
     */
    $('.detail-img-thumbnail').click(function() {
        let url = $(this).css('background-image').replace(/^url\(['"]?/,'').replace(/['"]?\)$/,'');
        $('#detail-img-main').attr("src", url);
    });

});