$(document).ready(function () {

    function changeChevronDirection() {
        if ($('.chevron').hasClass('fa-chevron-down')) {
            $('.chevron').addClass('fa-chevron-up').removeClass('fa-chevron-down');
        } else {
            $('.chevron').addClass('fa-chevron-down').removeClass('fa-chevron-up');
        }
    }
})