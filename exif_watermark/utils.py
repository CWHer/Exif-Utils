import os
from typing import List

from PIL import Image, ImageDraw, ImageOps


def getImagesPath(dir_path: str, suffix: List[str] = [".jpeg", ".NEF"]) -> List[str]:
    assert os.path.exists(dir_path), f"Path {dir_path} does not exist"
    assert os.path.isdir(dir_path), f"Path {dir_path} is not a directory"

    file_list = [
        os.path.join(dir_path, file)
        for file in os.listdir(dir_path)
        if file.endswith(tuple(suffix))
    ]
    return file_list


def toAbsPath(path: str) -> str:
    if not os.path.isabs(path):
        path = os.path.abspath(path)
    return path


def concatenate_image(images, align='left'):
    """
    将多张图片拼接成一列
    :param images: 图片对象列表
    :param align: 对齐方向，left/center/right
    :return: 拼接后的图片对象
    """
    widths, heights = zip(*(i.size for i in images))

    sum_height = sum(heights)
    max_width = max(widths)

    new_img = Image.new('RGBA', (max_width, sum_height), color=TRANSPARENT)

    x_offset = 0
    y_offset = 0
    if 'left' == align:
        for img in images:
            new_img.paste(img, (0, y_offset))
            y_offset += img.height
    elif 'center' == align:
        for img in images:
            x_offset = int((max_width - img.width) / 2)
            new_img.paste(img, (x_offset, y_offset))
            y_offset += img.height
    elif 'right' == align:
        for img in images:
            x_offset = max_width - img.width  # 右对齐
            new_img.paste(img, (x_offset, y_offset))
            y_offset += img.height
    return new_img


def padding_image(image, padding_size, padding_location='tb', color=None) -> Image.Image:
    """
    在图片四周填充白色像素
    :param image: 图片对象
    :param padding_size: 填充像素大小
    :param padding_location: 填充位置，top/bottom/left/right
    :return: 填充白色像素后的图片对象
    """
    if image is None:
        return None

    total_width, total_height = image.size
    x_offset, y_offset = 0, 0
    if 't' in padding_location:
        total_height += padding_size
        y_offset += padding_size
    if 'b' in padding_location:
        total_height += padding_size
    if 'l' in padding_location:
        total_width += padding_size
        x_offset += padding_size
    if 'r' in padding_location:
        total_width += padding_size

    padding_img = Image.new('RGBA', (total_width, total_height), color=color)
    padding_img.paste(image, (x_offset, y_offset))
    return padding_img


def resize_image_with_height(image, height, auto_close=True):
    """
    按照高度对图片进行缩放
    :param image: 图片对象
    :param height: 指定高度
    :return: 按照高度缩放后的图片对象
    """
    # 获取原始图片的宽度和高度
    width, old_height = image.size

    # 计算缩放后的宽度
    scale = height / old_height
    new_width = round(width * scale)

    # 进行等比缩放
    resized_image = image.resize((new_width, height), Image.ANTIALIAS)

    # 关闭图片对象
    if auto_close:
        image.close()

    # 返回缩放后的图片对象
    return resized_image


def resize_image_with_width(image, width, auto_close=True):
    """
    按照宽度对图片进行缩放
    :param image: 图片对象
    :param width: 指定宽度
    :return: 按照宽度缩放后的图片对象
    """
    # 获取原始图片的宽度和高度
    old_width, height = image.size

    # 计算缩放后的宽度
    scale = width / old_width
    new_height = round(height * scale)

    # 进行等比缩放
    resized_image = image.resize((width, new_height), Image.ANTIALIAS)

    # 关闭图片对象
    if auto_close:
        image.close()

    # 返回缩放后的图片对象
    return resized_image


def append_image_by_side(background, images, side='left', padding=200, is_start=False):
    """
    将图片横向拼接到背景图片中
    :param background: 背景图片对象
    :param images: 图片对象列表
    :param side: 拼接方向，left/right
    :param padding: 图片之间的间距
    :param is_start: 是否在最左侧添加 padding
    :return: 拼接后的图片对象
    """
    if 'right' == side:
        if is_start:
            x_offset = background.width - padding
        else:
            x_offset = background.width
        images.reverse()
        for i in images:
            if i is None:
                continue
            i = resize_image_with_height(
                i, background.height, auto_close=False)
            x_offset -= i.width
            x_offset -= padding
            background.paste(i, (x_offset, 0))
    else:
        if is_start:
            x_offset = padding
        else:
            x_offset = 0
        for i in images:
            if i is None:
                continue
            i = resize_image_with_height(
                i, background.height, auto_close=False)
            background.paste(i, (x_offset, 0))
            x_offset += i.width
            x_offset += padding


def text_to_image(content, font, bold_font, is_bold=False, fill='black') -> Image.Image:
    """
    将文字内容转换为图片
    """
    if is_bold:
        font = bold_font
    if content == '':
        content = '   '
    text_width, text_height = font.getsize(content)
    image = Image.new('RGBA', (text_width, text_height), color=TRANSPARENT)
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), content, fill=fill, font=font)
    return image


def merge_images(images, axis=0, align=0):
    """
    拼接多张图片
    :param images: 图片对象列表
    :param axis: 0 水平拼接，1 垂直拼接
    :param align: 0 居中对齐，1 底部/右对齐，2 顶部/左对齐
    :return: 拼接后的图片对象
    """
    # 获取每张图像的 size
    widths, heights = zip(*(img.size for img in images))

    # 计算输出图像的尺寸
    if axis == 0:  # 水平拼接
        total_width = sum(widths)
        max_height = max(heights)
    else:  # 垂直拼接
        total_width = max(widths)
        max_height = sum(heights)

    # 创建输出图像
    output_image = Image.new(
        'RGBA', (total_width, max_height), color=TRANSPARENT)

    # 拼接图像
    x_offset, y_offset = 0, 0
    for img in images:
        if axis == 0:  # 水平拼接
            if align == 1:  # 底部对齐
                y_offset = max_height - img.size[1]
            elif align == 2:  # 顶部对齐
                y_offset = 0
            else:  # 居中排列
                y_offset = (max_height - img.size[1]) // 2
            output_image.paste(img, (x_offset, y_offset))
            x_offset += img.size[0]
        else:  # 垂直拼接
            if align == 1:  # 右对齐
                x_offset = total_width - img.size[0]
            elif align == 2:  # 左对齐
                x_offset = 0
            else:  # 居中排列
                x_offset = (total_width - img.size[0]) // 2
            output_image.paste(img, (x_offset, y_offset))
            y_offset += img.size[1]

    return output_image
