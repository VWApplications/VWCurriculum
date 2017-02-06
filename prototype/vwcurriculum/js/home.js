$(document).ready(function(){
  $('.modal').modal({
    dismissible: true,
    opacity: .5,
    in_duration: 300,
    out_duration: 200,
  });
  $('.parallax').parallax();
  $('.materialboxed').materialbox();
  $('.slider').slider({full_width: true});
  $('.tooltipped').tooltip({delay: 50});
  $('.button-collapse').sideNav({
    menuWidth: 300,
    edge: 'left',
  });
});
