from django.conf import settings as django_settings


class Settings:
    @property
    def text(self) -> str:
        return getattr(django_settings, "ADMIN_NOTICE_TEXT", None)

    @property
    def text_color(self) -> str:
        return getattr(django_settings, "ADMIN_NOTICE_TEXT_COLOR", "white")

    @property
    def text_color_dark(self) -> str:
        return getattr(django_settings, "ADMIN_NOTICE_TEXT_COLOR_DARK", self.text_color)

    @property
    def background(self) -> str:
        return getattr(django_settings, "ADMIN_NOTICE_BACKGROUND", "red")

    @property
    def background_dark(self) -> str:
        return getattr(django_settings, "ADMIN_NOTICE_BACKGROUND_DARK", self.background)


settings = Settings()
