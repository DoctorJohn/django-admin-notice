from django.test import TestCase
from django.contrib.auth import get_user_model
from django.conf import settings
from faker import Faker


fake = Faker()
RENDER_INDICATOR = "<!-- django-admin-notice -->"


class AuthenticatedRenderingTestCase(TestCase):
    def setUp(self) -> None:
        super().setUp()
        superuser = get_user_model().objects.create_superuser(
            username="admin", email=fake.email(), password=fake.password()
        )
        self.client.force_login(superuser)

    def test_does_not_render_without_required_settings(self):
        with self.settings():
            del settings.ADMIN_NOTICE_TEXT
            response = self.client.get("/admin/")
            self.assertNotContains(response, RENDER_INDICATOR)

    def test_renders_configured_text(self):
        text = fake.sentence()
        with self.settings(ADMIN_NOTICE_TEXT=text):
            response = self.client.get("/admin/")
            self.assertContains(response, RENDER_INDICATOR)
            self.assertContains(response, text)

    def test_renders_configured_text_color(self):
        color = fake.rgb_css_color()
        with self.settings(ADMIN_NOTICE_TEXT="Test", ADMIN_NOTICE_TEXT_COLOR=color):
            response = self.client.get("/admin/")
            self.assertContains(response, RENDER_INDICATOR)
            self.assertContains(response, f"color: {color}")

    def test_renders_configured_background(self):
        color = fake.rgb_css_color()
        with self.settings(ADMIN_NOTICE_TEXT="Test", ADMIN_NOTICE_BACKGROUND=color):
            response = self.client.get("/admin/")
            self.assertContains(response, RENDER_INDICATOR)
            self.assertContains(response, f"background: {color}")

    def test_renders_fallback_if_no_text_color_is_configured(self):
        with self.settings():
            del settings.ADMIN_NOTICE_TEXT_COLOR
            response = self.client.get("/admin/")
            self.assertContains(response, RENDER_INDICATOR)
            self.assertContains(response, "color: white")

    def test_renders_fallback_if_not_background_is_configured(self):
        with self.settings():
            del settings.ADMIN_NOTICE_BACKGROUND
            response = self.client.get("/admin/")
            self.assertContains(response, RENDER_INDICATOR)
            self.assertContains(response, "background: red")


class UnauthenticatedRenderingTestCase(TestCase):
    def test_renders_only_when_authenticated(self):
        with self.settings(ADMIN_NOTICE_TEXT=fake.sentence()):
            response = self.client.get("/admin/login/")
            self.assertNotContains(response, RENDER_INDICATOR)

            superuser = get_user_model().objects.create_superuser(
                username="admin", email=fake.email(), password=fake.password()
            )
            self.client.force_login(superuser)

            response = self.client.get("/admin/")
            self.assertContains(response, RENDER_INDICATOR)
