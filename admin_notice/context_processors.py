from admin_notice.conf import settings


def notice(request):
    return {
        "ADMIN_NOTICE_TEXT": settings.text,
        "ADMIN_NOTICE_TEXT_COLOR": settings.text_color,
        "ADMIN_NOTICE_TEXT_COLOR_DARK": settings.text_color_dark,
        "ADMIN_NOTICE_BACKGROUND": settings.background,
        "ADMIN_NOTICE_BACKGROUND_DARK": settings.background_dark,
    }
