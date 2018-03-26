
jQuery(function($) {
    var sidebar = $('#sidebar'),
        mobile = sidebar.css('display') === 'none',
        yolo_logo = $('#yolo-logo');
    if (mobile) {
        sidebar.appendTo('#main-container')
            .attr('class', 'col-xs-12')
            .show();
        yolo_logo.prependTo(yolo_logo.parent());
    }
});