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

//Blogs

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
  $('#submitButton').click(function() {
    var email = $('#emailInput').val();
    if (validateEmail(email)) {
      showMessage('Se ha enviado con éxito', 'success');
    } else {
      showMessage('Formato inválido', 'error');
    }
  });

  function validateEmail(email) {
    var emailRegex = /^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$/;
    return emailRegex.test(email);
  }

  function showMessage(message, messageType) {
    var messageContainer = $('#messageContainer');
    messageContainer.text(message);
    messageContainer.removeClass().addClass('message ' + messageType);
  }
});

