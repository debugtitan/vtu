import os
import logging
import toml
from pathlib import Path


BASE_DIR = Path(__file__).resolve(strict=True).parent


class ConfigManager:

    def __init__(self, file_name: str) -> None:
        FILE_DIR = os.path.join(BASE_DIR, "localization", file_name)
        self._cfg = toml.load(FILE_DIR)

    def get(self, *keys):
        """get value of the given key(s) from configuration file"""

        if not keys:
            return self._cfg

        value = self._cfg

        try:
            for key in keys:
                value = value[key]
        except Exception as e:
            logging.debug(e)
            return None

        return value
