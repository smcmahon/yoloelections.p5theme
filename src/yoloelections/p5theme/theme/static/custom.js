
jQuery(function($) {
    var backtop_button = $("#backtop-link");

    if (backtop_button) {
        $(window).scroll(function(event){
            if (document.body.scrollTop > 400 || document.documentElement.scrollTop > 400) {
                backtop_button.show();
            } else {
                backtop_button.hide();
            }
        });

        backtop_button.on('click', function( event ){
            event.preventDefault();
            document.body.scrollTop = 0;
            document.documentElement.scrollTop = 0;
            backtop_button.hide();
        });
    }
});

