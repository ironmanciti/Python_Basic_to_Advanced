$(function() {
  // Auto play modal video
  $(".video").click(function () {
    var theModal = $(this).data("target"),
    videoSRC = $(this).attr("data-video"),
    videoSRCauto = videoSRC + "?modestbranding=1&rel=0&controls=0&showinfo=0&html5=1&autoplay=1";
    $(theModal + ' iframe').attr('src', videoSRCauto);
    $(theModal + ' button.close').click(function () {
      $(theModal + ' iframe').attr('src', videoSRC);
    });
  });
});

$(document).on('click', '[data-toggle="lightbox"]', function(event){
  event.preventDefault();
  $(this).ekkoLightbox();
});

$(document).ready(function() {

var offset = 250;

var duration = 300;

$(window).scroll(function() {

if ($(this).scrollTop() > offset) {

$(".back-to-top").fadeIn(duration);

} else {

$(".back-to-top").fadeOut(duration);

}

});
$(".back-to-top").click(function(event) {

event.preventDefault();

$("html, body").animate({scrollTop: 0}, duration);

return false;

})

});
