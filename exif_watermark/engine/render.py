
class Render:
    def __init__(self, image, text, font, color, position):
        self.image = image
        self.text = text
        self.font = font
        self.color = color
        self.position = position

    def render(self):
        draw = ImageDraw.Draw(self.image)
        draw.text(self.position, self.text, self.color, self.font)
        return self.image