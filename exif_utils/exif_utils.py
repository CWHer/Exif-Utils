import dataclasses
import datetime
import logging
import os
from typing import Optional

import exifread


@dataclasses.dataclass
class ExifData:
    date_time: Optional[str] = None

    camera_make: Optional[str] = None
    camera_model: Optional[str] = None
    lens_make: Optional[str] = None
    lens_model: Optional[str] = None

    exposure_time: Optional[str] = None
    f_number: Optional[str] = None
    focal_length: Optional[str] = None
    iso_speed_ratings: Optional[str] = None


EXIF_KEY_MAP = {
    "EXIF DateTimeOriginal": "date_time",
    "Image Make": "camera_make",
    "Image Model": "camera_model",
    "EXIF LensMake": "lens_make",
    "EXIF LensModel": "lens_model",
    "EXIF ExposureTime": "exposure_time",
    "EXIF FNumber": "f_number",
    "EXIF FocalLength": "focal_length",
    "EXIF ISOSpeedRatings": "iso_speed_ratings",
}

EXIF_TRANSFORM_MAP = {
    "date_time": [
        lambda v: datetime.datetime.strptime(v, "%Y:%m:%d %H:%M:%S").strftime("%Y-%m-%d %H:%M"),
    ],
    "f_number": [lambda v: f"ƒ/{eval(v):.1f}"],
    "focal_length": [lambda v: f"{eval(v):.0f}mm"],
    "iso_speed_ratings": [lambda v: f"ISO{v}"],
}


def loadExifData(file_path: str):
    assert os.path.exists(file_path), f"Path {file_path} does not exist"
    assert os.path.isfile(file_path), f"Path {file_path} is not a file"

    with open(file_path, "rb") as f:
        exif_tags = exifread.process_file(f, details=False)

    exif_data = ExifData()
    for key, value in exif_tags.items():
        if key in EXIF_KEY_MAP:
            setattr(exif_data, EXIF_KEY_MAP[key], str(value))

    for field in dataclasses.fields(exif_data):
        if getattr(exif_data, field.name) is None:
            logging.warning(f"File {file_path}, Missing exif field: {field.name}")

    for k, fns in EXIF_TRANSFORM_MAP.items():
        v = getattr(exif_data, k)
        assert v is not None, f"Missing exif field: {k}"
        for fn in fns:
            v = fn(v)
        setattr(exif_data, k, v)

    return exif_data
