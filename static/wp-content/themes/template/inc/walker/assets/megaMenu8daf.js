function viral_pro_build_mega_menu() {
    var $container = jQuery('.ht-header .ht-container');

    jQuery('.ht-menu .menu-item-megamenu.megamenu-full-width').hover(function () {
        var $menuWidth = $container.outerWidth(),
                $menuPosition = $container.offset(),
                $menuItemPosition = jQuery(this).offset(),
                $PositionLeft = $menuItemPosition.left - $menuPosition.left;

        jQuery(this).find('.megamenu').css({
            'left': '-' + $PositionLeft + 'px',
            'width': $menuWidth
        });
    });

    // Megamenu auto width
    jQuery('.ht-menu .menu-item-megamenu.megamenu-auto-width .megamenu').each(function () {
        var $li = jQuery(this).parent(),
                $window_width = jQuery(window).width(),
                $container = jQuery('.ht-header .ht-container'),
                $containerWidth = $container.outerWidth(),
                $containerOffset = $container.offset().left,
                $liOffset = $li.offset().left,
                $liWidth = $li.outerWidth(),
                $dropdownWidth = jQuery(this).outerWidth();
        if (viral_pro_megamenu.rtl == 'true') {
            if ($dropdownWidth < $liOffset + $liWidth - $containerOffset) {
                jQuery(this).css({
                    'right': 0,
                    'left': 'auto'
                });
            } else {
                var $excessWidth = $dropdownWidth - ($liOffset + $liWidth - $containerOffset)
                jQuery(this).css({
                    'right': -$excessWidth,
                    'left': 'auto',
                });
            }
        } else {
            if ($dropdownWidth < $containerOffset + $containerWidth - $liOffset) {
                jQuery(this).css({
                    'left': 0,
                    'right': 'auto'
                });
            } else {
                if ($dropdownWidth < $liOffset + $liWidth - $containerOffset) {
                    jQuery(this).css({
                        'right': 0,
                        'left': 'auto'
                    });
                } else {
                    var $excessWidth = $dropdownWidth - ($containerOffset + $containerWidth - $liOffset);
                    jQuery(this).css({
                        'left': -$excessWidth,
                        'right': 'auto',
                    });

                }
            }
        }
    });

    jQuery('li.heading-yes > a').on('click', function () {
        return false;
    });

    jQuery('.cat-megamenu-tab > div:first').addClass('active-tab');

    jQuery('.cat-megamenu-tab > div').hoverIntent(function () {
        var $this = jQuery(this);
        if ($this.hasClass('active-tab')) {
            return;
        }

        $this.siblings().removeClass('active-tab');
        $this.addClass('active-tab');
        var activeCat = $this.data('catid');
        $this.closest('.megamenu').find('.cat-megamenu-content > ul').hide();
        $this.closest('.megamenu').find('#' + activeCat).fadeIn('fast');
    });
}