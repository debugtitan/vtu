import os
import toml
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent

class ConfigManager:
    _cfg_file = BASE_DIR / 'config'
    _cfg = dict()

    _callback = None

    def __init__(self, config_file, callback=None):
        self._cfg_file = config_file
        self._callback = callback

        # Read initial configuration
        self._read_cfg()


    def _read_cfg(self):
        """ Read the TOML content of a given configuration file """
        try:
            if os.path.isfile(self._cfg_file):
                with open(self._cfg_file) as config_file:
                    self._cfg = toml.load(config_file)
        except Exception as e:
            err = f"Can't read '{self._cfg_file}'"
            logging.error(f"{repr(e)} - {err}")

    def _write_cfg(self):
        """ Write the TOML dictionary into the given configuration file """
        try:
            if not os.path.exists(os.path.dirname(self._cfg_file)):
                os.makedirs(os.path.dirname(self._cfg_file))
            with open(self._cfg_file, "w") as config_file:
                toml.dump(self._cfg, config_file)
        except Exception as e:
            err = f"Can't write '{self._cfg_file}'"
            logging.error(f"{repr(e)} - {err}")

    def get(self, *keys):
        """ Return the value of the given key(s) from a configuration file """
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

    def set(self, value, *keys):
        """ Set a new value for the given key(s) in the configuration file.
        Will also execute the callback method if there is one """
        if not self._cfg:
            self._read_cfg()

        if not keys:
            return

        tmp_cfg = self._cfg

        try:
            for key in keys[:-1]:
                tmp_cfg = tmp_cfg.setdefault(key, {})
            tmp_cfg[keys[-1]] = value

            self._ignore = True
            self._write_cfg()

            if isinstance(self._callback, types.FunctionType):
                self._callback(self._cfg, value, *keys)
        except Exception as e:
            err = f"Can't set '{keys}' in '{self._cfg_file}'"
            logging.debug(f"{repr(e)} - {err}")

    def remove(self, *keys):
        """ Remove given key(s) from the configuration file.
        Will also execute the callback method if there is one """
        if not self._cfg:
            self._read_cfg()

        if not keys:
            return

        tmp_cfg = self._cfg

        try:
            for key in keys[:-1]:
                tmp_cfg = tmp_cfg.setdefault(key, {})
            del tmp_cfg[keys[-1]]

            self._ignore = True
            self._write_cfg()

            if isinstance(self._callback, types.FunctionType):
                self._callback(self._cfg, None, *keys)
        except KeyError as e:
            err = f"Can't remove key '{keys}' from '{self._cfg_file}'"
            logging.debug(f"{repr(e)} - {err}")
