$(document).ready(function () {
 console.log('js ready');
    /**
     * Changes direction of chevron when clicked
     */
    $('.chevron').click(function () {
        changeChevronDirection();
    });

    function changeChevronDirection() {
        if ($('.chevron').hasClass('fa-chevron-down')) {
            $('.chevron').addClass('fa-chevron-up').removeClass('fa-chevron-down');
        } else {
            $('.chevron').addClass('fa-chevron-down').removeClass('fa-chevron-up');
        }
    }


    checkCompetitionDate();

    function checkCompetitionDate() {
        console.log('checkCompetitionDate activated');
        var submitBtn = document.getElementById('SubmitCompetition'),
        x = new Date(),
        today = new Date();

        x.setFullYear(2020,6,25);

        if (today > x) {
            submitBtn.style.visibility = 'hidden';  
        } else {
            submitBtn.style.visibility = 'visible';
        }
    }
});