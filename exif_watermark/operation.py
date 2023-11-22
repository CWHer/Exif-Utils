import abc
from typing import Tuple

from PIL import Image


class Op(abs.ABC):
    @abc.abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def forward(self, *arg, **kwargs) -> Image.Image:
        pass

# Nullary operation


class ExifMark(Op):
    def __init__(self):
        raise NotImplementedError

    def forward(self) -> Image.Image:
        raise NotImplementedError


class Identity(Op):
    def __init__(self, img: Image.Image):
        self.img = img

    def forward(self) -> Image.Image:
        return self.img


# Unary operation
class Resize(Op):
    def __init__(self, size: Tuple[int, int]):
        self.size = size

    def forward(self, img: Image.Image) -> Image.Image:
        raise NotImplementedError


class Margin(Op):
    def __init__(self, margin_size: int, margin_color: str):
        self.margin_size = margin_size
        self.margin_color = margin_color

    def forward(self, img: Image.Image) -> Image.Image:
        raise NotImplementedError


class Shadow(Op):
    def __init__(self, shadow_size: int, shadow_color: str):
        self.shadow_size = shadow_size
        self.shadow_color = shadow_color

    def forward(self, img: Image.Image) -> Image.Image:
        raise NotImplementedError

# Binary operation


class Concat(Op):
    """
    Concatenate two images
    """

    def __init__(self, method: str):
        assert method in ["horizontal", "vertical"]
        self.method = method

    def forward(self, img0: Image.Image, img1: Image.Image) -> Image.Image:
        raise NotImplementedError


class Merge(Op):
    """
    Merge image0 into image1, requires image0 to be smaller than image1
    """

    def __init__(self, position: Tuple[int, int]):
        self.position = position

    def forward(self, img0: Image.Image, img1: Image.Image) -> Image.Image:
        raise NotImplementedError
