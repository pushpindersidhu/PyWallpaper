import json
from json.decoder import JSONDecodeError
import logging
import settings
from logger import log
import os


class Config:
    def __init__(self, file=settings.CONFIG) -> None:
        self.file = file
        self.logger = log(name=__name__, filename=settings.LOGS)

        try:
            with open(self.file, "r") as f:
                self.config = json.load(f)
            self.logger.info("Config file loaded successfully.")
        except IOError:
            self.logger.error("Config file file not found.")
            self.config = {}
        except JSONDecodeError:
            self.logger.error("Failed to load config file.")
            self.config = {}

    def save(self):
        try:
            with open(self.file, "w") as file:
                json.dump(self.config, fp=file, indent=4)
            self.logger.info("Config file saved successfully.")
        except IOError:
            self.logger.error("Failed to save config file.")

    def set(self, key, value):
        self.config[key] = value
        self.logger.debug(f"Config set - ({ key } : { value })")

    def get(self, key):
        try:
            value = self.config[key]
            self.logger.debug(f"get({ key }) -> { value }")
            return self.config[key]
        except KeyError:
            self.logger.debug(f"get({ key }) -> Not Found")
            return None

    def refresh(self):
        try:
            with open(self.file, "r") as f:
                self.config = json.load(f)
            self.logger.info("Config file loaded successfully.")
        except IOError:
            self.logger.error("Config file file not found.")
            self.config = {}
        except JSONDecodeError:
            self.logger.error("Failed to load config file.")
            self.config = {}


if __name__ == "__main__":
    config = Config()
    config.set("test", "test")
    config.get("key")
    config.save()
