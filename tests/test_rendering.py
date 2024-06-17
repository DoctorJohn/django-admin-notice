from faker import Faker

fake = Faker()
RENDER_INDICATOR = "<!-- django-admin-notice -->"


def test_does_not_render_without_required_settings(settings, admin_client):
    del settings.ADMIN_NOTICE_TEXT
    response = admin_client.get("/admin/")
    assert RENDER_INDICATOR not in response.content.decode()


def test_renders_configured_text(settings, admin_client):
    text = fake.sentence()
    settings.ADMIN_NOTICE_TEXT = text

    response = admin_client.get("/admin/")
    assert RENDER_INDICATOR in response.content.decode()
    assert text in response.content.decode()


def test_renders_configured_text_color(settings, admin_client):
    color = fake.rgb_css_color()
    settings.ADMIN_NOTICE_TEXT_COLOR = color

    response = admin_client.get("/admin/")
    assert RENDER_INDICATOR in response.content.decode()
    assert f"color: {color}" in response.content.decode()


def test_renders_configured_dark_text_color(settings, admin_client):
    color = fake.rgb_css_color()
    settings.ADMIN_NOTICE_TEXT_COLOR_DARK = color

    response = admin_client.get("/admin/")
    assert RENDER_INDICATOR in response.content.decode()
    assert f"color: {color}" in response.content.decode()


def test_renders_configured_background(settings, admin_client):
    color = fake.rgb_css_color()
    settings.ADMIN_NOTICE_BACKGROUND = color

    response = admin_client.get("/admin/")
    assert RENDER_INDICATOR in response.content.decode()
    assert f"background: {color}" in response.content.decode()


def test_renders_configured_dark_background(settings, admin_client):
    color = fake.rgb_css_color()
    settings.ADMIN_NOTICE_BACKGROUND_DARK = color

    response = admin_client.get("/admin/")
    assert RENDER_INDICATOR in response.content.decode()
    assert f"background: {color}" in response.content.decode()


def test_renders_fallback_if_no_text_color_is_configured(settings, admin_client):
    del settings.ADMIN_NOTICE_TEXT_COLOR

    response = admin_client.get("/admin/")
    assert RENDER_INDICATOR in response.content.decode()
    assert "color: white" in response.content.decode()


def test_renders_fallback_if_no_dark_text_color_is_configured(settings, admin_client):
    del settings.ADMIN_NOTICE_TEXT_COLOR_DARK
    color = fake.rgb_css_color()
    settings.ADMIN_NOTICE_TEXT_COLOR = color

    response = admin_client.get("/admin/")
    assert RENDER_INDICATOR in response.content.decode()
    assert f"color: {color}" in response.content.decode()


def test_renders_fallback_if_not_background_is_configured(settings, admin_client):
    del settings.ADMIN_NOTICE_BACKGROUND

    response = admin_client.get("/admin/")
    assert RENDER_INDICATOR in response.content.decode()
    assert "background: red" in response.content.decode()


def test_renders_fallback_if_not_dark_background_is_configured(settings, admin_client):
    del settings.ADMIN_NOTICE_BACKGROUND_DARK
    color = fake.rgb_css_color()
    settings.ADMIN_NOTICE_BACKGROUND = color

    response = admin_client.get("/admin/")
    assert RENDER_INDICATOR in response.content.decode()
    assert f"background: {color}" in response.content.decode()


def test_renders_only_when_authenticated(settings, client, admin_client):
    text = fake.sentence()
    settings.ADMIN_NOTICE_TEXT = text

    response = client.get("/admin/login/")
    assert RENDER_INDICATOR not in response.content.decode()
    assert text not in response.content.decode()

    response = admin_client.get("/admin/")
    assert RENDER_INDICATOR in response.content.decode()
    assert text in response.content.decode()
