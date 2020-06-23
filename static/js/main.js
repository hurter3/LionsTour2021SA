$(document).ready(function () {

    function changeChevronDirection() {
        if ($('.chevron').hasClass('fa-chevron-down')) {
            $('.chevron').addClass('fa-chevron-up').removeClass('fa-chevron-down');
        } else {
            $('.chevron').addClass('fa-chevron-down').removeClass('fa-chevron-up');
        }
    }
})

// Get the modal
var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}