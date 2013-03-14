/*global jQuery, document */

(function (global, $) {
    "use strict";
    $(document).ready(function () {
        // some global things
        $('#search-user').submit(function (e) {
            e.preventDefault();
            document.location.pathname = '/user/' + encodeURIComponent($('#search-user').find('input').val());
        });
        $('#search-artist').submit(function (e) {
            e.preventDefault();
            document.location.pathname = '/artist/' + encodeURIComponent($('#search-artist').find('input').val());
        });
        $('a[rel=external]').on('click touchstart', function (e) {
            e.preventDefault();
            var $target = $(e.target);
            global.open($target.attr('href'));
        });
    });
}(this, jQuery));