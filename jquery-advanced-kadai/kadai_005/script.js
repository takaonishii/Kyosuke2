$(function(){
    $('.button-more').on('mouseover',function(){
        $(this).animate({
            opacity:0.5,
            marginLeft:20,
        },100);
    });
});

$('.carousel').slick({
    autoplay:true,
    dots:true,
    infinite:true,
    autoplaySpeed: 2000,
    arrows: false,
})
