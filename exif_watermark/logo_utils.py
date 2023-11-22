import json
import os
from typing import Dict


class LogoManager:
    def __init__(self) -> None:
        self.dir_path: str
        self.logo_map: Dict[str, str]

    def setup(self, dir_path: str):
        self.dir_path = dir_path if os.path.isabs(dir_path) else os.path.abspath(dir_path)
        assert os.path.exists(self.dir_path), f"Path {self.dir_path} does not exist"
        config_path = os.path.join(self.dir_path, "config.json")
        assert os.path.exists(config_path), f"Path {config_path} does not exist"

        with open(config_path, "r", encoding="utf-8") as f:
            self.logo_map = json.load(f)

    def select(self, logo_name: str):
        for k, v in self.logo_map.items():
            if k in logo_name:
                return os.path.join(self.dir_path, v)
        raise ValueError(f"Logo {logo_name} not found")


logo_manager = LogoManager()
