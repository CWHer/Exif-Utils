import os
from typing import Dict

import yaml

from .logo_utils import logo_manager


class ConfigManager:
    def __init__(self):
        self.config: Dict
        # Basic config
        self.logo_dir: str
        self.font_dir: str
        self.bold_font_dir: str
        self.input_dir: str
        self.output_dir: str
        self.quality: int

        # Layout config
        self.margin_config: Dict
        self.exif_config: Dict
        self.background_config: Dict

    def setup(self, file_path: str) -> None:
        file_path = os.path.abspath(file_path)
        base_path = os.path.dirname(file_path)
        assert os.path.exists(file_path), f"{file_path} not exists"
        with open(file_path, "r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f)

        # Basic config
        self.logo_dir = os.path.join(base_path, self.config["base"]["logo_dir"])
        logo_manager.setup(self.logo_dir)
        self.font_dir = os.path.join(base_path, self.config["base"]["font"])
        assert os.path.exists(self.font_dir), f"{self.font_dir} not exists"
        self.bold_font_dir = os.path.join(base_path, self.config["base"]["bold_font"])
        assert os.path.exists(self.bold_font_dir), f"{self.bold_font_dir} not exists"
        self.input_dir = os.path.join(base_path, self.config["base"]["input_dir"])
        assert os.path.exists(self.input_dir), f"{self.input_dir} not exists"
        self.output_dir = os.path.join(base_path, self.config["base"]["output_dir"])
        assert os.path.exists(self.output_dir), f"{self.output_dir} not exists"
        self.quality = self.config["base"]["quality"]

        # Layout config
        self.margin_config = self.config["layout"]["margin"]
        self.exif_config = self.config["layout"]["exif_mark"]
        self.background_config = self.config["layout"]["background"]


config_manager = ConfigManager()
