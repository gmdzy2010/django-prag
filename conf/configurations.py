"""
This file contains all of the settings for this package.
"""

import os


# Package name

PACKAGE_NAME = "realbio_prag"

PACKAGE_ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Data source initial settings

DATA_SOURCE = {
    "db": {
        "host": "",
        "port": 0000,
        "database": "",
        "user": "",
        "password": "",
    },
    "file": {
        "path": "",
    },
    "stdout": {
        "info": "This function hadn't been developed, please wait for updating"
                "in next version",
        "command": "ps aux|grep test",
    },
    "django": {
        "info": "This function hadn't been developed, please wait for updating"
                "in next version",
    },
}


# Path settings

LOGGING_FILE_PATH = os.path.join(PACKAGE_ROOT_PATH, "logs")

TEMPLATE_PATH = os.path.join(PACKAGE_ROOT_PATH, "templates")

TEMPLATE_PATH_RENDERED = os.path.join(PACKAGE_ROOT_PATH, "rendered_file")
