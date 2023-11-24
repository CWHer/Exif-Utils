import os
import unittest

from exif_watermark.utils import (ExifData, config_manager, getImagesPath,
                                  loadExifData, logo_manager)


class TestUtils(unittest.TestCase):
    def testConfigManager(self):
        config_manager.setup("exif_watermark/config.yaml")

    def testLogoManager(self):
        logo_manager.setup("assets/logos")
        path = logo_manager.select("NIKON CORPORATION")
        self.assertTrue("nikon.png" in path)
        self.assertTrue(os.path.exists(path))
        self.assertTrue(os.path.isfile(path))

    def testPathUtils(self):
        path = os.path.abspath("assets/images")
        file_list = getImagesPath(path, suffix=[".jpeg"])
        self.assertTrue(len(file_list) == 6)

    def testExifReader(self):
        exif_data = loadExifData("assets/images/right-margin.jpeg")
        self.assertTrue(isinstance(exif_data, ExifData))
        self.assertTrue(exif_data.camera_make == "NIKON CORPORATION")
        self.assertTrue(exif_data.camera_model == "NIKON Z 7_2")
        self.assertTrue(exif_data.lens_make == "NIKON")
        self.assertTrue(exif_data.lens_model == "NIKKOR Z 24-70mm f/4 S")
        self.assertTrue(exif_data.exposure_time == "1/800")
        self.assertTrue(exif_data.f_number == "ƒ/4.0")
        self.assertTrue(exif_data.focal_length == "70mm")
        self.assertTrue(exif_data.iso_speed_ratings == "ISO250")


if __name__ == "__main__":
    unittest.main()
