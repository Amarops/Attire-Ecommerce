// init Isotope
var $grid = $('.collection-list').isotope({
  // options
});
// filter items on button click
$('.filter-button-group').on( 'click', 'button', function() {
  var filterValue = $(this).attr('data-filter');
  resetFilterBtns();
  $(this).addClass('active-filter-btn');
  $grid.isotope({ filter: filterValue });
});

var filterBtns = $('.filter-button-group').find('button');
function resetFilterBtns(){
  filterBtns.each(function(){
    $(this).removeClass('active-filter-btn');
  });
}
const readmoreBtn = document.getElementById('readmoreBtn');
const cardContainer = document.getElementById('cardContainer');
const closeBtn = document.getElementById('closeBtn');

readmoreBtn.addEventListener('click', function() {
  cardContainer.style.display = 'block';
});

closeBtn.addEventListener('click', function() {
  cardContainer.style.display = 'none';
});

//NEWSLETTER
$(document).ready(function() {
  $('#emailInput').on('input', function() {
    var email = $(this).val();
    var isValid = validateEmail(email);
    var messageDiv = $('#message');
    
    if (isValid) {
      messageDiv.text('Enviado correctamente').removeClass('error').addClass('success');
    } else {
      messageDiv.text('Formato incorrecto').removeClass('success').addClass('error');
    }
  });
  
  function validateEmail(email) {
    var re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
  }
});

