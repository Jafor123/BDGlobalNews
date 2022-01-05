/**
 * Viral Pro Custom JS
 *
 * @package Viral Pro
 *
 * Distributed under the MIT license - http://opensource.org/licenses/MIT
 */

jQuery(function ($) {
    if (navigator.userAgent.indexOf('Mac') > 0) {
        $('body').addClass('ht-mac-os');
    }
    
    /*---------Preloader---------*/
    $(window).load(function () {
        $('#ht-preloader-wrap').fadeOut('slow');
    });

    /*---------Maintenance Slider---------*/
    if ($('.ht-maintenance-slider .ht-maintenance-slide').length > 0) {
        $('.ht-maintenance-slider').owlCarousel({
            rtl: JSON.parse(viral_pro_options.rtl),
            items: 1,
            loop: true,
            mouseDrag: false,
            nav: false,
            dots: false,
            autoplayTimeout: parseInt($('.ht-maintenance-slider').attr('data-timeout')),
            autoplay: true,
            smartSpeed: 600,
            animateOut: 'fadeOut'
        });
    }

    /*---------Maintenance Video---------*/
    if ($('.ht-maintenance-video[data-property]').length > 0) {
        $(".ht-maintenance-video[data-property]").YTPlayer({
            showControls: false,
            containment: 'self',
            mute: true,
            addRaster: false,
            useOnMobile: false,
            playOnlyIfVisible: true,
            anchor: 'center,center',
            showYTLogo: false,
            loop: true,
            optimizeDisplay: true,
            quality: 'hd720'
        });
    }

    $(document).on('click', '.product .viral-pro-product-actions a.compare:not(.added)', function (e) {
        var $button = $(this);
        setTimeout(function () {
            $button.html('<i class="icofont-random"></i><span class="woo-button-tooltip">Added</span>');
        }, 3000);
    });

    /*---------scroll To Top---------*/
    $(window).scroll(function () {
        if ($(window).scrollTop() > 300) {
            $('#back-to-top').addClass('ht-show');
        } else {
            $('#back-to-top').removeClass('ht-show');
        }
    });

    $('#back-to-top').click(function (e) {
        e.preventDefault();
        $('html,body').animate({
            scrollTop: 0
        }, 800);
    });

    /*---------Blog Isotope---------*/
    $('.viral-pro-blog-layout6-wrap').isotope({
        itemSelector: '.viral-pro-hentry',
        //percentPosition: true,
        masonry: {
            // use outer width of grid-sizer for columnWidth
            //scolumnWidth: '.grid-sizer'
        }
    })

    /*---------Single Post Gallery Slider---------*/
    $('.single-entry-gallery .owl-carousel').owlCarousel({
        rtl: JSON.parse(viral_pro_options.rtl),
        items: 1,
        loop: true,
        mouseDrag: false,
        autoplay: true,
        autoplayTimeout: 6000,
        nav: true,
        dots: false,
        navText: ['<i class="mdi mdi-chevron-left"></i>', '<i class="mdi mdi-chevron-right"></i>']
    });

    /*---------Related Thumb---------*/
    $('.viral-pro-related-post.style3 .viral-pro-related-post-wrap').owlCarousel({
        rtl: JSON.parse(viral_pro_options.rtl),
        items: 3,
        margin: 30,
        loop: true,
        mouseDrag: false,
        autoplay: true,
        autoplayTimeout: 6000,
        nav: true,
        dots: false,
        navText: ['<i class="mdi mdi-chevron-left"></i>', '<i class="mdi mdi-chevron-right"></i>'],
        responsive: {
            0: {
                items: 1
            },
            480: {
                items: 2
            },
            680: {
                items: 3
            },
            768: {
                items: 2
            },
            1000: {
                items: 3
            }
        }
    });

    /*---------Popup Search---------*/
    $('.ht-search-button a').click(function () {
        $('.ht-search-wrapper').addClass('ht-search-triggered');
        setTimeout(function () {
            $('.ht-search-wrapper .search-field').focus();
        }, 1000);
    });

    $('.ht-search-close').click(function () {
        $('.ht-search-wrapper').removeClass('ht-search-triggered');
    });

    $(document).keydown(function (e) {
        // ESCAPE key pressed
        if (e.keyCode == 27 && $('.ht-search-wrapper').hasClass('ht-search-triggered')) {
            $('.ht-search-wrapper').removeClass('ht-search-triggered');
        }
    });

    /*---------OffCanvas Sidebar---------*/
    $('.ht-offcanvas-nav a').click(function () {
        $('body').addClass('ht-offcanvas-opened');
    });

    $('.ht-offcanvas-close, .ht-offcanvas-sidebar-modal').click(function () {
        $('body').removeClass('ht-offcanvas-opened');
    });

    $('.ht-offcanvas-sidebar .widget_nav_menu .menu-item-has-children > a').append('<span class="ht-dropdown"></span>');

    $('.ht-dropdown').on('click', function () {
        $(this).parent('a').next('ul').slideToggle();
        $(this).toggleClass('ht-opened');
        return false;
    })

    $(document).keydown(function (e) {
        // ESCAPE key pressed
        if (e.keyCode == 27 && $('body').hasClass('ht-offcanvas-opened')) {
            $('body').removeClass('ht-offcanvas-opened');
        }
    });

    /*---------Header Time---------*/
    startTime();

    /*---------Main Menu Dropdown---------*/
    $('.ht-menu > ul').superfish({
        delay: 500,
        animation: {
            opacity: 'show'
        },
        speed: 'fast'
    });

    $('#ht-mobile-menu .menu-collapser').on('click', function () {
        $(this).next('ul').slideToggle();
    });

    $('#ht-responsive-menu .dropdown-nav').on('click', function () {
        $(this).parents('a').siblings('ul').slideToggle();
        $(this).toggleClass('ht-opened');
        return false;
    })

    /*---------Drop Down---------*/
    var $dropdowns = $('.ht-menu > ul > .menu-item.menu-item-has-children:not(.menu-item-megamenu) > .sub-menu');
    if ($dropdowns.length > 0) {
        var $container = $($dropdowns[0]).closest('.ht-container');
        if ($container.length > 0) {
            var container_right_max = $container.offset().left + $container.outerWidth();
            var window_width = $(window).width();
            $dropdowns.each(function () {
                var $dropdown = $(this);
                var $li = $(this).parent();
                if (viral_pro_megamenu.rtl == 'true') {
                    if (((window_width - $li.offset().left) + $dropdown.outerWidth()) > container_right_max) {
                        $dropdown.css({
                            'right': 'auto',
                            'left': 0
                        });
                    }

                    if (((window_width - $li.offset().left) + $dropdown.outerWidth() * 2) > container_right_max) {
                        $dropdown.find('.sub-menu').css({
                            'right': 'auto',
                            'left': '100%'
                        });
                    }
                } else {
                    if ($li.offset().left + $dropdown.outerWidth() > container_right_max) {
                        $dropdown.css({
                            'left': 'auto',
                            'right': 0
                        });
                    }

                    if (($li.offset().left + $dropdown.outerWidth() * 2) > container_right_max) {
                        $dropdown.find('.sub-menu').css({
                            'left': 'auto',
                            'right': '100%'
                        });
                    }
                }
            });
        }
    }

    /*---------MegaMenu---------*/
    viral_pro_build_mega_menu();

    /*---------Sticky Header---------*/
    var hHeight = 0;
    var adminbarHeight = 0;

    if ($('body').hasClass('admin-bar')) {
        adminbarHeight = 32;
    }

    var $stickyHeader = $('.ht-header');

    if ($('.ht-sticky-header').length > 0 && $stickyHeader.length > 0) {
        hHeight = $stickyHeader.outerHeight();

        if ($('body').hasClass('ht-header-style4')) {
            hHeight = hHeight + 38
        }
        var hOffset = $stickyHeader.offset().top;

        var offset = hOffset - adminbarHeight;

        $stickyHeader.headroom({
            offset: offset,
            onTop: function () {
                $('#ht-content').css({
                    paddingTop: 0
                });
            },
            onNotTop: function () {
                $('#ht-content').css({
                    paddingTop: hHeight + 'px'
                });
            }
        });

        $('.ht-sticky-sidebar .secondary-wrap').css('top', (hHeight + adminbarHeight + 40) + 'px');
    }

    /*---------One Page Nav---------*/
    $('.ht-menu').onePageNav({
        //currentClass: 'current',
        changeHash: false,
        scrollSpeed: 750,
        scrollThreshold: 0.1,
        scrollOffset: hHeight + adminbarHeight
    });

    $('#ht-responsive-menu').onePageNav({
        //currentClass: 'current',
        changeHash: false,
        scrollSpeed: 750,
        scrollThreshold: 0.1
    });

    // *only* if we have anchor on the url
    if (window.location.hash) {
        $(window).load(function () {
            var sectionid = window.location.hash;
            sectionid = sectionid.replace('/', '');
            if ($(sectionid).length > 0) {
                $('html, body').animate({
                    scrollTop: $(sectionid).offset().top - hHeight
                }, 1000);
            }
        });
    }

    $('.vl-header-ticker .owl-carousel').owlCarousel({
        rtl: JSON.parse(viral_pro_options.rtl),
        items: 1,
        margin: 10,
        loop: true,
        mouseDrag: false,
        autoplay: false,
        autoplayTimeout: 6000,
        nav: true,
        dots: false,
        animateOut: 'slideOutDown',
        animateIn: 'slideInDown',
        navText: ['<i class="mdi mdi-chevron-up"></i>', '<i class="mdi mdi-chevron-down"></i>']
    });

    /*---------Woocommerce Cart---------*/
    $('.menu-item-ht-cart .woocommerce-mini-cart').mCustomScrollbar({
        axis: "y",
        scrollbarPosition: "outside"
    });

    $('img.vl-lazy').Lazy();

    /*---------Widgets---------*/
    $('.ht-single-open-accordian .ht-accordion-box').accordion({
        'transitionSpeed': 400,
        'singleOpen': true
    });

    $('.ht-all-open-accordian .ht-accordion-box').accordion({
        'transitionSpeed': 400,
        'singleOpen': false
    });

    $('.widget_viral_pro_counter .ht-counter-widget').waypoint(function () {
        $('.ht-counter').each(function (index) {
            var counter_time = parseInt(index * 500 + 300);
            var $odometer = $(this).find('.odometer');
            setTimeout(function () {
                $odometer.html($odometer.data('count'));
            }, counter_time);
        });
        this.destroy();
    }, {
        offset: '90%'
    });

    $('.ht-progress-bar').each(function (index) {
        var $this = $(this);
        var delay_time = parseInt(index * 100 + 300);
        $this.waypoint(function () {
            setTimeout(function () {
                $this.find('.ht-progress-bar-length').animate({
                    width: $this.attr("data-width") + '%'
                }, 1000, function () {
                    $this.find("span").animate({
                        opacity: 1
                    }, 500);
                });
            }, delay_time);
            this.destroy();
        }, {
            offset: '90%',
        });
    });

    $('.ht-post-tab').each(function (index) {
        $(this).find('.ht-pt-header .ht-pt-tab:first').addClass('ht-pt-active');
        $(this).find('.ht-pt-content-wrap .ht-pt-content:first').show();
    });

    $('.ht-pt-tab').on('click', function () {
        var id = $(this).data('id');
        $(this).closest('.ht-post-tab').find('.ht-pt-tab').removeClass('ht-pt-active');
        $(this).addClass('ht-pt-active');

        $(this).closest('.ht-post-tab').find('.ht-pt-content').hide();
        $('#' + id).show();
    });

    if ($('.ht-post-carousel').length > 0) {
        $('.ht-post-carousel').owlCarousel({
            rtl: JSON.parse(viral_pro_options.rtl),
            items: 1,
            loop: true,
            mouseDrag: false,
            nav: false,
            dots: true,
            autoplayTimeout: 6000,
            autoplay: true,
            smartSpeed: 600,
            margin: 5
        });
    }


    /*---------Selective Refresh Jquery---------*/
    selectiveRefreshJquery();

    var hasSelectiveRefresh = (
            'undefined' !== typeof wp &&
            wp.customize &&
            wp.customize.selectiveRefresh &&
            wp.customize.widgetsPreview &&
            wp.customize.widgetsPreview.WidgetPartial
            );
    if (hasSelectiveRefresh) {
        wp.customize.selectiveRefresh.bind('partial-content-rendered', function (placement) {
            selectiveRefreshJquery(placement);
        });
    }

    function selectiveRefreshJquery(placement) {
        if (typeof (placement) == 'undefined') {
            var partial = 'viral_pro_all';
            var $container = $('.ht-section');
        } else {
            var partial = placement.partial.id;
            var $container = placement.container;
        }

        var section_class, section_partial;

        if (partial.indexOf('viral_pro_') !== -1) {
            var partialArr = partial.split('_');
            if (partialArr[2]) {
                if (partialArr[2] == 'all') {
                    section_class = '.ht-section';
                    section_partial = 'viral_pro_' + partialArr[2];
                } else if (partialArr[2] == 'frontpage') {
                    section_class = '.ht-' + partialArr[3] + '-section';
                    section_partial = 'viral_pro_' + partialArr[3];
                } else {
                    section_class = '.ht-' + partialArr[2] + '-section';
                    section_partial = 'viral_pro_' + partialArr[2];
                }
            }
        }

        //console.log(section_partial);
        //console.log(section_class);

        $('body').imagesLoaded(function () {
            $.stellar({
                horizontalScrolling: false,
                responsive: true,
            });
        });

        if ($container.hasClass('ht-section')) {
            if ($(section_class + '[data-motion]').length > 0) {
                $('body').imagesLoaded(function () {
                    $(section_class + '[data-motion]').each(function () {
                        var windowSpy = new $.Espy(window);
                        var element = $(this)[0];
                        var headerClouds = new Motio(element, {
                            fps: 30,
                            speedX: 60
                        });
                        // Play only when in the viewport
                        windowSpy.add(element, function (entered) {
                            headerClouds[entered ? 'play' : 'pause']();
                        });
                    });
                });
            }

            if ($(section_class + '[data-property]').length > 0) {
                $(section_class + '[data-property]').YTPlayer({
                    showControls: false,
                    containment: 'self',
                    mute: true,
                    addRaster: false,
                    useOnMobile: false,
                    playOnlyIfVisible: true,
                    anchor: 'center,center',
                    showYTLogo: false,
                    loop: true,
                    optimizeDisplay: true,
                    quality: 'hd720'
                });
            }
        }

        if (($('.vl-ticker:not(.vl-ele-ticker)').length > 0) && ['viral_pro_all', 'viral_pro_ticker'].includes(section_partial)) {
            var ticker_parameters = $('.vl-ticker:not(.vl-ele-ticker) .owl-carousel').attr('data-params');
            var ticker_params = JSON.parse(ticker_parameters);

            var ticker_obj = {
                rtl: JSON.parse(viral_pro_options.rtl),
                items: 1,
                margin: 10,
                loop: true,
                mouseDrag: false,
                autoplay: true,
                autoplayTimeout: parseInt(ticker_params.pause) * 1000,
                nav: true,
                dots: false,
                navText: ['<i class="mdi mdi-chevron-left"></i>', '<i class="mdi mdi-chevron-right"></i>']
            }


            if (ticker_params.animation == 'top-bottom') {
                ticker_obj.animateOut = 'slideOutDown';
                ticker_obj.animateIn = 'slideInDown';
            } else if (ticker_params.animation == 'flip-top-bottom') {
                ticker_obj.animateOut = 'slideOutDown';
                ticker_obj.animateIn = 'flipInX';
            }

            $('.vl-ticker:not(.vl-ele-ticker) .owl-carousel').owlCarousel(ticker_obj);
        }

        if ($('.vl-slider-wrap:not(.vl-ele-slider-wrap)').length > 0 && ['viral_pro_all', 'viral_pro_slider1', 'viral_pro_slider2'].includes(section_partial)) {
            $('.vl-slider-wrap:not(.vl-ele-slider-wrap)').owlCarousel({
                rtl: JSON.parse(viral_pro_options.rtl),
                items: 1,
                margin: 0,
                loop: true,
                mouseDrag: true,
                autoplay: true,
                nav: true,
                dots: false,
                navText: ['<i class="mdi mdi-chevron-left"></i>', '<i class="mdi mdi-chevron-right"></i>']
            });
        }

        if ($('.vl-fwcarousel-block').length > 0 && ['viral_pro_all', 'viral_pro_fwcarousel'].includes(section_partial)) {
            var fwc_parameters = $('.vl-fwcarousel-block .owl-carousel').attr('data-params');
            var fwc_params = JSON.parse(fwc_parameters);

            if (parseInt(fwc_params.items) === 2) {
                var fwc_params_item_480 = 1;
            } else {
                var fwc_params_item_480 = parseInt(fwc_params.items) - 2;
            }

            $('.vl-fwcarousel-block .owl-carousel').owlCarousel({
                rtl: JSON.parse(viral_pro_options.rtl),
                items: parseInt(fwc_params.items),
                margin: 0,
                loop: true,
                mouseDrag: true,
                autoplay: JSON.parse(fwc_params.autoplay),
                autoplayTimeout: parseInt(fwc_params.pause) * 1000,
                nav: true,
                dots: false,
                navText: ['<i class="mdi mdi-chevron-left"></i>', '<i class="mdi mdi-chevron-right"></i>'],
                responsive: {
                    0: {
                        items: 1
                    },
                    480: {
                        items: fwc_params_item_480
                    },
                    768: {
                        items: parseInt(fwc_params.items) - 1
                    },
                    1000: {
                        items: parseInt(fwc_params.items)
                    }
                }
            });
        }

        if ($('.vl-carousel-wrap:not(.vl-ele-carousel-wrap)').length > 0 && ['viral_pro_all', 'viral_pro_carousel1', 'viral_pro_carousel2'].includes(section_partial)) {
            $('.vl-carousel-wrap:not(.vl-ele-carousel-wrap)').each(function () {
                var c_parameters = $(this).find('.owl-carousel').attr('data-params');
                var c_params = JSON.parse(c_parameters);

                if (parseInt(c_params.items) === 2) {
                    var c_params_item_480 = 1;
                } else {
                    var c_params_item_480 = parseInt(c_params.items) - 2;
                }

                $(this).find('.owl-carousel').owlCarousel({
                    rtl: JSON.parse(viral_pro_options.rtl),
                    items: parseInt(c_params.items),
                    margin: parseInt(c_params.margin),
                    loop: true,
                    mouseDrag: true,
                    autoplay: JSON.parse(c_params.autoplay),
                    autoplayTimeout: parseInt(c_params.pause) * 1000,
                    nav: true,
                    dots: false,
                    navText: ['<i class="mdi mdi-chevron-left"></i>', '<i class="mdi mdi-chevron-right"></i>'],
                    responsive: {
                        0: {
                            items: 1
                        },
                        480: {
                            items: c_params_item_480
                        },
                        768: {
                            items: parseInt(c_params.items) - 1
                        },
                        1000: {
                            items: parseInt(c_params.items)
                        }
                    }
                });
            });
        }

        if ($('.vl-mininews-block:not(.vl-row)').length > 0 && ['viral_pro_all', 'viral_pro_mininews'].includes(section_partial)) {
            var sliderGallery = function () {

                /*** Vars ***/
                var gallery = '.vl-mininews-block:not(.vl-row)',
                        slider = false;

                /*** Init ***/
                var init = function () {

                    manage(); // On load (1*)

                    $(window).on('resize', function () { // On resize (2*)
                        manage();
                    });

                };

                /*** Manage slider ***/
                var manage = function () {

                    if (!slider && ($(window).width() < 1000)) { // If mobile and slider not built yet = build
                        build();
                        slider = true;
                    } else if (slider && ($(window).width() > 1000)) { // Not mobile but slider built = destroy
                        destroy();
                        slider = false;
                    }

                };

                /*** Build slider ***/
                var build = function () {
                    var item900 = 3;
                    var item768 = 2;
                    var item580 = 2;
                    var item0 = 1;

                    if ($(gallery).hasClass('style2')) {
                        item900 = 5;
                        item768 = 4;
                        item580 = 3;
                        item0 = 2;
                    }

                    slider = $(gallery).addClass('owl-carousel'); // Add owl slider class (3*)
                    slider.owlCarousel({
                        rtl: JSON.parse(viral_pro_options.rtl),
                        items: $(gallery).attr('data-count'),
                        loop: true,
                        margin: 10,
                        mouseDrag: true,
                        autoplay: false,
                        autoplayTimeout: 6000,
                        dots: true,
                        lazyLoad: true,
                        responsive: {
                            0: {
                                items: item0
                            },
                            580: {
                                items: item580
                            },
                            768: {
                                items: item768
                            },
                            900: {
                                items: item900
                            }
                        }
                    });

                };

                /*** Destroy slider ***/
                var destroy = function () {
                    $(gallery).trigger('destroy.owl.carousel'); // Trigger destroy event (4*) 
                    $(gallery).removeClass('owl-carousel'); // Remove owl slider class (3*)
                };

                /*** Public methods***/
                return {
                    init: init
                };

            }();

            sliderGallery.init();
        }

        /*---------Youtube Video Playlist---------*/
        if ($('#vl-video-playlist').length > 0 && ['viral_pro_all', 'viral_pro_video'].includes(section_partial)) {
            $(".vl-video-thumbnails").mCustomScrollbar({
                axis: "y",
                scrollbarPosition: "outside"
            });

            youtube_videoplaylist_class();

            $(window).on('resize', function () {
                setTimeout(youtube_videoplaylist_class, 500);
            });
        }


        var hHeight = 0;
        var adminbarHeight = 0;

        if ($('body').hasClass('admin-bar')) {
            adminbarHeight = 32;
        }
        var $stickyHeader = $('.ht-header');

        if ($('.ht-sticky-header').length > 0 && $stickyHeader.length > 0) {
            hHeight = $stickyHeader.outerHeight();

            if ($('body').hasClass('ht-header-style4')) {
                hHeight = hHeight + 38
            }
        }

        /*---------Sticky Sidebar---------*/
        $('.ht-sticky-sidebar #secondary').theiaStickySidebar({
            additionalMarginTop: hHeight + adminbarHeight + 40,
            additionalMarginBottom: 40
        });

        /*---------Sticky Sidebar---------*/
        $('.ht-enable-sticky-sidebar .ht-leftnews-container .secondary, .ht-enable-sticky-sidebar .ht-rightnews-container .secondary').theiaStickySidebar({
            additionalMarginTop: hHeight + adminbarHeight + 40,
            additionalMarginBottom: 40
        });
    } //selectiveRefreshJquery Ends

    //add and remove the class on video playlist according to its width
    function youtube_videoplaylist_class() {
        $('#vl-video-playlist').each(function () {
            var playlistWidth = $(this).outerWidth();
            if (playlistWidth < 788) {
                $(this).addClass('shrink-playlist');
            } else if (playlistWidth > 789) {
                $(this).removeClass('shrink-playlist');
            }
        });
    }

    function checkTime(i) {
        return (i < 10) ? "0" + i : i;
    }

    function startTime() {
        var today = new Date(),
                h = checkTime(today.getHours()),
                m = checkTime(today.getMinutes()),
                s = checkTime(today.getSeconds());
        $('.vl-time').html(h + ":" + m + ":" + s);
        t = setTimeout(function () {
            startTime()
        }, 500);
    }

    /*---------GDPR---------*/
    if (viral_pro_options.customizer_gdpr_settings && typeof (Cookies) !== 'undefined') {
        var issetPrivacypolicy = Cookies.get('viral_pro_cookies');

        if (typeof (issetPrivacypolicy) == 'undefined' && !JSON.parse(viral_pro_options.customize_preview)) {
            $('.viral-pro-privacy-policy').show();
        }

        $('#viral-pro-confirm').on('click', function () {
            $('.viral-pro-privacy-policy').fadeOut('fast');
            //var inFifteenMinutes = new Date(new Date().getTime() + 15 * 60 * 1000);
            Cookies.set('viral_pro_cookies', 'yes', {
                expires: 1,
                path: '/'
            });
            return false;
        })
    }
});