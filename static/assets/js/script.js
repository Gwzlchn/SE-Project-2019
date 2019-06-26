(function($) {
	'use strict';
	jQuery(document).on('ready', function(){
        // Header Sticky
        $(window).on('scroll',function() {
            if ($(this).scrollTop() >170){  
                $('.header-sticky').addClass("is-sticky");
            }
            else{
                $('.header-sticky').removeClass("is-sticky");
            }
        }); 
        
        // Hover dropdown menu JS
        $( '.dropdown-menu a.dropdown-toggle' ).on( 'click', function ( e ) {
            var $el = $( this );
            var $parent = $( this ).offsetParent( ".dropdown-menu" );
            if ( !$( this ).next().hasClass( 'show' ) ) {
                $( this ).parents( '.dropdown-menu' ).first().find( '.show' ).removeClass( "show" );
            }
            var $subMenu = $( this ).next( ".dropdown-menu" );
            $subMenu.toggleClass( 'show' );

            $( this ).parent( "li" ).toggleClass( 'show' );

            $( this ).parents( 'li.nav-item.dropdown.show' ).on( 'hidden.bs.dropdown', function ( e ) {
                $( '.dropdown-menu .show' ).removeClass( "show" );
            } );

            if ( !$parent.parent().hasClass( 'navbar-nav' ) ) {
                $el.next().css( { "top": $el[0].offsetTop, "left": $parent.outerWidth() - 4 } );
            }
            return false;
        });
      
        // HOME SLIDER
        $('.hero-slider').owlCarousel({
            items:1,
            loop:true,
            nav:true,
            animateOut: 'slideOutUp',
            animateIn: 'slideInUp',
            mouseDrag: false,
            autoplayTimeout:6000,
            smartSpeed:4000,
            responsiveClass:true,
            navText: [
                "<i class='icofont-swoosh-left'></i>",
                "<i class='icofont-swoosh-right'></i>"
            ],
            responsive:{
                0:{
                    autoplay:false,
                    autoplayHoverPause: true,
                },
                600:{
                    autoplay:false,
                    autoplayHoverPause: true,
                },
                1024:{
                    autoplay:true,
                    autoplayHoverPause: true,
                }
            }
        });
        
        // HOME SLIDER TWO
        $('.hero-slider2').owlCarousel({
            items:1,
            loop:true,
            nav:true,
            animateOut: 'slideOutUp',
            animateIn: 'slideInUp',
            mouseDrag: false,
            autoplayTimeout:6000,
            smartSpeed:4000,
            responsiveClass:true,
            navText: [
                "<i class='icofont-long-arrow-left'></i>",
                "<i class='icofont-long-arrow-right'></i>"
            ],
            responsive:{
                0:{
                    autoplay:false,
                    autoplayHoverPause: true,
                },
                600:{
                    autoplay:false,
                    autoplayHoverPause: true,
                },
                1024:{
                    autoplay:true,
                    autoplayHoverPause: true,
                }
            }
        });
        
        // Popular course carosel JS
        $('.popular-course-carosel').owlCarousel({
            loop:true,
            nav:true,
            autoplay:true,
            autoplayHoverPause: true,
            mouseDrag: false,
            dots: false,
            margin: 30,
            responsiveClass:true,
            navText: [
                "<i class='icofont-swoosh-left'></i>",
                "<i class='icofont-swoosh-right'></i>"
            ],
            responsive:{
                0:{
                    items:1,
                    autoplay:false,
                },
                768:{
                    items:2,
                    autoplay:false,
                },
                1000:{
                    items:3
                }
            }
        });
        
        // Events carosel JS
        $('.events-carosel').owlCarousel({
            loop:true,
            nav:true,
            autoplay:true,
            autoplayHoverPause: true,
            mouseDrag: false,
            dots: false,
            margin: 30,
            navText: [
                "<i class='icofont-swoosh-left'></i>",
                "<i class='icofont-swoosh-right'></i>"
            ],
            responsive:{
                0:{
                    items:1
                },
                768:{
                    items:2
                },
                1024:{
                    items:3
                },
                1100:{
                    items:3
                }
            }
        });
        
        // MagnificPopup Video JS
        $('.popup-youtube, .popup-vimeo, .attrachment-video').magnificPopup({
            disableOn: 300,
            type: 'iframe',
            mainClass: 'mfp-fade',
            removalDelay: 160,
            preloader: false,
            fixedContentPos: false
        });
        
        // Counter Up Number JS
        $('.counter').counterUp({
            delay: 20,
            time: 5000
        });
		
        //Public methods
        $.fn.tilt.destroy = function() {
            $(this).each(function () {
                $(this).find('.js-tilt-glare').remove();
                $(this).css({'will-change': '', 'transform': ''});
                $(this).off('mousemove mouseenter mouseleave');
            });
        };

        $.fn.tilt.getValues = function() {
            const results = [];
            $(this).each(function () {
                this.mousePositions = getMousePositions.call(this);
                results.push(getValues.call(this));
            });
            return results;
        };

        $.fn.tilt.reset = function() {
            $(this).each(function () {
                this.mousePositions = getMousePositions.call(this);
                this.settings = $(this).data('settings');
                mouseLeave.call(this);
                setTimeout(() => {
                    this.reset = false;
                }, this.settings.transition);
            });
        };
        // Publication carosel JS
        $('.publication-carosel').owlCarousel({
            loop:true,
            nav:true,
            autoplay:true,
            autoplayHoverPause: true,
            mouseDrag: false,
            dots: false,
            margin: 30,
            navText: [
                "<i class='icofont-swoosh-left'></i>",
                "<i class='icofont-swoosh-right'></i>"
            ],
            responsive:{
                0:{
                    items:1
                },
                576:{
                    items:2
                },
                768:{
                    items:3
                },
                1000:{
                    items:4
                }
            }
        });
        
        // News carosel JS
        $('.news-carosel').owlCarousel({
            loop:true,
            nav:true,
            autoplay:true,
            autoplayHoverPause: true,
            mouseDrag: false,
            dots: false,
            margin: 30,
            navText: [
                "<i class='icofont-swoosh-left'></i>",
                "<i class='icofont-swoosh-right'></i>"
            ],
            responsive:{
                0:{
                    items:1
                },
                768:{
                    items:2
                },
                1000:{
                    items:3
                }
            }
        });
        
        // Feedback carosel JS
        $('.feedback-carosel').owlCarousel({
            loop:true,
            nav:true,
            autoplay:true,
            autoplayHoverPause: true,
            mouseDrag: false,
            dots: false,
            margin: 30,
            navText: [
                "<i class='icofont-swoosh-left'></i>",
                "<i class='icofont-swoosh-right'></i>"
            ],
            responsive:{
                0:{
                    items:1,
                    autoplay:false
                },
                768:{
                    items:2,
                    autoplay:false
                },
                1000:{
                    items:3
                }
            }
        });
        
        // Partner carosel JS
        $('.partner-carosel').owlCarousel({
            loop:true,
            nav:false,
            autoplay:true,
            autoplayHoverPause: true,
            mouseDrag: true,
            dots: false,
            margin: 50,
            responsive:{
                0:{
                    items:3,
                    margin: 30
                },
                576:{
                    items:4,
                    margin: 30
                },
                768:{
                    items:5,
                    margin: 30
                },
                1000:{
                    items:5
                }
            }
        });
        
        // Partner carosel JS
        $('.categorie-slider').owlCarousel({
            loop:true,
            nav:true,
            autoplay:true,
            autoplayHoverPause: true,
            mouseDrag: true,
            dots: false,
            margin: 30,
            navText: [
                "<i class='icofont-thin-left'></i>",
                "<i class='icofont-thin-right'></i>"
            ],
            responsive:{
                0:{
                    items:2,
                    margin: 15
                },
                600:{
                    items:3
                },
                1000:{
                    items:4
                }
            }
        });
        
        // Course Accordion JS
        $('.course-accordion > .course-accordion-list:eq(0) .ca-section-title').addClass('active').next().slideDown();

        $('.course-accordion .ca-section-title').on('click', function(j) {
            var dropDown = $(this).closest('.course-accordion-list').find('.course-accordion-content');
            
            $(this).closest('.course-accordion').find('.course-accordion-content').not(dropDown).slideUp();
            
            if ($(this).hasClass('active')) {
                $(this).removeClass('active');
            } else {
                $(this).closest('.course-accordion').find('.ca-section-title.active').removeClass('active');
                $(this).addClass('active');
            }
            dropDown.stop(false, true).slideToggle();
            j.preventDefault();
        });
     
        // ScrollTop JS
        $('body').append('<div id="toTop"><i class="icofont-rounded-up"></i></div>');
        $(window).on('scroll', function () {
            if ($(this).scrollTop() != 0) {
                $('#toTop').fadeIn();
            } else {
                $('#toTop').fadeOut();
            }
        }); 
        $('#toTop').on('click', function(){
            $("html, body").animate({ scrollTop: 0 }, 600);
            return false;
        });

        // Preloader JS
        jQuery(window).on('load', function() {
            $('.preloader').fadeOut();
        });
        
        // Zoom effect image popup JS
        $('.zoom-gallery').magnificPopup({
            delegate: 'a',
            type: 'image',
            closeOnContentClick: false,
            closeBtnInside: false,
            mainClass: 'mfp-with-zoom mfp-img-mobile',

            gallery: {
                enabled: true
            },
            zoom: {
                enabled: true,
                duration: 500, // don't foget to change the duration also in CSS
                opener: function(element) {
                    return element.find('img');
                }
            }
        });
    }); 	
})(jQuery);