PROJECT_NAME="Exif-Watermark"
SRC_DIR="exif_watermark"
TEST_DIR="tests"

test:
	python3 -m unittest discover -s $(TEST_DIR) -p "*_test.py"
