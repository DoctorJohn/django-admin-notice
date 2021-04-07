from django.conf import settings


def notice(request):
    return {
        "ADMIN_NOTICE_TEXT": getattr(settings, "ADMIN_NOTICE_TEXT", None),
        "ADMIN_NOTICE_TEXT_COLOR": getattr(
            settings, "ADMIN_NOTICE_TEXT_COLOR", "white"
        ),
        "ADMIN_NOTICE_BACKGROUND": getattr(settings, "ADMIN_NOTICE_BACKGROUND", "red"),
    }
