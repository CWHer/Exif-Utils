import os
from typing import List


def getImagesPath(dir_path: str, suffix: List[str] = [".jpeg", ".NEF"]) -> List[str]:
    assert os.path.exists(dir_path), f"Path {dir_path} does not exist"
    assert os.path.isdir(dir_path), f"Path {dir_path} is not a directory"

    file_list = [
        os.path.join(dir_path, file)
        for file in os.listdir(dir_path)
        if file.endswith(tuple(suffix))
    ]
    return file_list
