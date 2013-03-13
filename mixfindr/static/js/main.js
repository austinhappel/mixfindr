/*global jQuery, document */

(function ($) {
    "use strict";
    $(document).ready(function () {
        $('#search-user').submit(function (e) {
            e.preventDefault();
            document.location.pathname = '/user/' + encodeURIComponent($('#search-user').find('input').val());
        });
        $('#search-artist').submit(function (e) {
            e.preventDefault();
            document.location.pathname = '/artist/' + encodeURIComponent($('#search-artist').find('input').val());
        });
    });
}(jQuery));