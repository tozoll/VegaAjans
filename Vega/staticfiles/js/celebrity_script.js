$(document).ready(function() {
  $(".owl-one").owlCarousel({
    items: 1,
    stagePadding: 0,
    loop: true,
    margin: 10,
    nav: true,
    navText: [
      "<i class='fa fa-caret-left'></i>",
      "<i class='fa fa-caret-right'></i>"
    ],
    responsive: {
      0: {
        items: 2,
        nav: true
      },
      700: {
        items: 4,
        nav: false
      },
      1000: {
        items: 6,
        nav: true,
        loop: false
      }
    }
  });

  $(".owl-two").owlCarousel({
    items: 3,
    merge: true,
    loop: true,
    margin: 10,
    video: true,
    lazyLoad: true,
    responsive: {
      0: {
        items: 1,
        nav: true,
        center: true
      },
      700: {
        items: 3,
        nav: false
      },
      1000: {
        items: 3,
        nav: true,
        loop: false
      }
    }
  });

  $(".swipebox").swipebox({
    useCSS: true, // false will force the use of jQuery for animations
    useSVG: true, // false to force the use of png for buttons
    initialIndexOnArray: 0, // which image index to init when a array is passed
    hideCloseButtonOnMobile: false, // true will hide the close button on mobile devices
    removeBarsOnMobile: true, // false will show top bar on mobile devices
    videoMaxWidth: 1140, // videos max width
    loopAtEnd: true, // true will return to the first image after the last image is reached
    hideBarsDelay: 0 // You can set this this value throught Easy SwipeBox Settings page
  });
});
