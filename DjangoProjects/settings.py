
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Configure installed apps (Preparation for Task 1)
INSTALLED_APPS = [
    ...
    'apps.bookmodule',
    'apps.usermodule',
    ...
]

# Template directory setup (Task 4)
TEMPLATE_DIR = os.path.join(BASE_DIR, "apps/templates")
TEMPLATES = [
    {
        ...
        'DIRS': [TEMPLATE_DIR],  # Add template directory to settings
        ...
    }
]
