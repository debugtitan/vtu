from __future__ import absolute_import
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent

INSTALLED_APPS = ["database"]


# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "mirk.sqlite3",
    }
}
