import os
import toml
import logging
from pathlib import Path


class ConfigManager:
    _cfg_file = None
    _cfg = dict()


    def __init__(self, cfg_file):
        # Read initial configuration
        if os.path.exists(cfg_file):
            self._cfg_file = cfg_file
            self._read_cfg()
        else:
            err = f"Can't read '{self._cfg_file}'"
            logging.error(err)


    def _read_cfg(self):
        """ Read the toml configuration file """
        try:
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
