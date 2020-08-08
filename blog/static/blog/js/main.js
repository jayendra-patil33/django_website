$(function () {
  $(document).scroll(function () {
    var $nav = $(".navbar");
    $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
  });
});

$(function () {
$(document).scroll(function () {
  var $nav= $(".nav-link.customName");
  $nav.toggleClass('trail', $(this).scrollTop() > $nav.height());
});
});
