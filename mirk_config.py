import os
import toml
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent

class ConfigManager:
    _cfg_file = os.path.join(BASE_DIR, "config", "config.toml")
    _cfg = dict()


    def __init__(self):
        # Read initial configuration
        self._read_cfg()


    def _read_cfg(self):
        """ Read the toml configuration file """
        try:
            if os.path.exists(self._cfg_file):
                self._cfg = toml.load(self._cfg_file)
        except Exception as e:
            err = f"Can't read '{self._cfg_file}'"
            logging.error(f"{repr(e)} - {err}")


    def get(self, *keys):
        """ get value of the given key(s) from configuration file """
        if not self._cfg:
            self._read_cfg()

        if not keys:
            return self._cfg

        value = self._cfg

        try:
            for key in keys:
                value = value[key]
        except Exception as e:
            err = f"Can't get '{keys}' from '{self._cfg_file}'"
            logging.debug(f"{repr(e)} - {err}")
            return None

        return value
