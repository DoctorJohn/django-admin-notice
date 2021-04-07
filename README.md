# Django Admin Notice

[![PyPI](https://img.shields.io/pypi/v/django-admin-notice)](https://pypi.org/project/django-admin-notice/)
[![PyPI - License](https://img.shields.io/pypi/l/django-admin-notice)](https://github.com/DoctorJohn/django-admin-notice/blob/master/LICENSE)

Show a floating notice banner above the Django admin interface.
Particularly useful for indicating the current deployment environment.

## Installation

Install django-admin-notice via the Python Package Index (PyPI):

`pip install django-admin-notice`

Add `admin_notice` to your `INSTALLED_APPS` somewhere before `django.contrib.admin`.

```python
INSTALLED_APPS = [
    "admin_notice",  # <-- Add this somewhere before "django.contrib.admin"
    "django.contrib.admin",
    # ... other apps
]
```

Add `admin_notice.context_processors.notice` to the templates `context_processors`.
Having `django.template.context_processors.request` is required as well.

```python
TEMPLATES = [
    {
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",  # <-- have this
                "admin_notice.context_processors.notice",  # <-- Add this
                # ... other context processors
            ]
        },
    },
]
```

## Settings

Set the `ADMIN_NOTICE_TEXT` to the text you want to show above the admin interface.
No message is shown if this setting is missing or empty.

```python
ADMIN_NOTICE_TEXT = "Production environment"
```

Optionally specify a custom text color and background for your notice.
The default text color is `white` and the default background `red`.

```python
ADMIN_NOTICE_TEXT_COLOR = "white"
ADMIN_NOTICE_BACKGROUND = "red"
```

### Tips

It's a common use case to indicate the projects deployment environment.
The following configuration shows how to obtain the `django-admin-notice`
configuration from environment variables and how to configure a fallback.

```python
from os import environ

ADMIN_NOTICE_TEXT = environ.get("ADMIN_NOTICE_TEXT", "Local environment")
ADMIN_NOTICE_TEXT_COLOR = environ.get("ADMIN_NOTICE_TEXT_COLOR", "white")
ADMIN_NOTICE_BACKGROUND = environ.get("ADMIN_NOTICE_BACKGROUND", "green")
```

## Example

Run `python manage.py runserver` after following the *Installation* section
to see a fully working example project.

## Contributing

### Setup

1. Clone the repository and enter the cloned folder
2. (optional) Create and activate a dedicated Python virtual environment
3. Run `pip install -e ".[dev]"` to install the projects requirements
4. (optional) Run `pre-commit install` to install the pre-commit hook

### Pre-commit hook

Our pre-commit hook formats and lints the code.

### Formatting and linting

- Run `black admin_notice tests` to format the code
- Run `flake8 admin_notice tests` to lint the code

### Testing

- Run `py.test --cov admin_notice tests` to run the tests in the current Python env
- Run `tox` to run the tests in all supported Python and Django environments

### Makefile

All commands listed above have shortcut make recipes.
Take a look at the `Makefile` to learn more.
