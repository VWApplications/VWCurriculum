$(document).ready(function(){
  $('.modal').modal({
    dismissible: true,
    opacity: .5,
    in_duration: 300,
    out_duration: 200,
  });
  $('.button-collapse').sideNav({
    menuWidth: 300,
    edge: 'left',
  });
  $('.dropdown-button').dropdown({
    hover: true,
    belowOrigin: true,
  });
  $('.parallax').parallax();
  $('.materialboxed').materialbox();
  $('.slider').slider({full_width: true});
  $('.tooltipped').tooltip({delay: 50});
});
