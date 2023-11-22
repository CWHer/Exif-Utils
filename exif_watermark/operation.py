import abc


class Op(abs.ABC):
    @abc.abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def run(self, img):
        pass

class AddMargin(Op):
    def __init__(self, margin_size, margin_color):
        self.margin_size = margin_size
        self.margin_color = margin_color

    def run(self, img):
        return add_margin(img, self.margin_size, self.margin_color)
    
class AddPadding(Op):
    def __init__(self, padding_size, padding_color, padding_location):
        self.padding_size = padding_size
        self.padding_color = padding_color
        self.padding_location = padding_location

    def run(self, img):
        return add_padding(img, self.padding_size, self.padding_color, self.padding_location)
    
class AddShadow(Op):
    def __init__(self, shadow_size, shadow_color, shadow_position):
        self.shadow_size = shadow_size
        self.shadow_color = shadow_color
        self.shadow_position = shadow_position

    def run(self, img):
        return add_shadow(img, self.shadow_size, self.shadow_color, self.shadow_position)
    

class AddExif(Op):
    def __init__(self, exif_text, exif_font, exif_color, exif_position):
        self.exif_text = exif_text
        self.exif_font = exif_font
        self.exif_color = exif_color
        self.exif_position = exif_position

    def run(self, img):
        return add_exif(img, self.exif_text, self.exif_font, self.exif_color, self.exif_position)


class AddBackground(Op):
    def __init__(self, background_color):
        self.background_color = background_color

    def run(self, img):
        return add_background(img, self.background_color)
