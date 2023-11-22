# Exif-Utils

[![license](https://img.shields.io/github/license/CWHer/Exif-Utils)](https://github.com/CWHer/Exif-Utils/blob/master/LICENSE) ![language](https://img.shields.io/github/languages/top/CWHer/Exif-Utils?color=orange)

**This is a tool for adding Exif watermarks to photos, manipulating photo pixel ratios, image color and quality.**

## Illustration

|                             |                             |                             |
| --------------------------- | --------------------------- | --------------------------- |
| ![](./assets/images/1.jpeg) | ![](./assets/images/2.jpeg) | ![](./assets/images/3.jpeg) |
| ![](./assets/images/4.jpeg) | ![](./assets/images/5.jpeg) | ![](./assets/images/6.jpeg) |
| ![](./assets/images/7.jpeg) | ![](./assets/images/8.jpeg) | ![](./assets/images/9.jpeg) |

## Usage

- [ ] TODO

## Settings

- [ ] TODO

<!-- 通过 `config.yaml` 配置。

<details>
<summary>点击展开</summary>

```yaml
base:
  alternative_bold_font: ./fonts/Roboto-Medium.ttf
  alternative_font: ./fonts/Roboto-Regular.ttf
  # 粗体
  bold_font: ./fonts/AlibabaPuHuiTi-2-85-Bold.otf
  # 粗体字体大小
  bold_font_size: 1
  # 常规字体
  font: ./fonts/AlibabaPuHuiTi-2-45-Light.otf
  # 常规字体大小
  font_size: 1
  # 输入文件夹
  input_dir: ./input
  # 输出文件夹
  output_dir: ./output
  # 输出图片质量，如果你觉得输出图片的体积过大，比如一张20M的图片，处理后变成了40M，那么你可以通过适当降低输出质量来减小图片体积
  quality: 100
global: # 全局设置，你可以在命令行中通过【更多设置】来修改这些设置
  focal_length:
    # 是否使用等效焦距
    use_equivalent_focal_length: false
  padding_with_original_ratio:
    # 是否使用原始图片的宽高比来填充白边
    enable: false
  shadow:
    # 是否使用阴影
    enable: false
  white_margin:
    # 是否使用白边
    enable: true
    # 白边宽度
    width: 3
layout:
  # 背景颜色，仅在布局为 normal（自定义）时有效
  background_color: "#ffffff"
  elements:
    # 左下角元素
    left_bottom:
      # 左下角文字颜色，仅在布局为 normal（自定义）时有效
      color: "#757575"
      # 是否使用粗体，仅在布局为 normal（自定义）时有效
      is_bold: false
      # 左下角文字内容，可选项参考下表
      name: Model
    # 下面三个元素的设置和上面是类似的
    left_top:
      color: "#212121"
      is_bold: true
      name: LensModel
    right_bottom:
      color: "#757575"
      is_bold: false
      name: Datetime
      value: Photo by NONE
    right_top:
      color: "#212121"
      is_bold: true
      name: Param
  # 是否使用 Logo，仅在布局为 normal（自定义）时有效，可选项为 true、false
  logo_enable: false
  # Logo 位置，仅在布局为 normal（自定义）时有效，可选项为 left、right
  logo_position: left
  # 布局类型，可选项参考下表，你可以在命令行中通过【布局】来修改它
  type: watermark_right_logo
logo:
  makes:
    canon: # 标识，用户自定义，不要重复
      id: Canon # 厂商名称，从 exif 信息中获取，和 exif 信息中的 Make 字段一致即可
      path: ./logos/canon.png # Logo 路径
    # 下同
    fujifilm:
      id: FUJIFILM
      path: ./logos/fujifilm.png
    hasselblad:
      id: HASSELBLAD
      path: ./logos/hasselblad.png
    huawei:
      id: HUAWEI
      path: ./logos/xmage.jpg
    leica:
      id: leica
      path: ./logos/leica_logo.png
    nikon:
      id: NIKON
      path: ./logos/nikon.png
    olympus:
      id: Olympus
      path: ./logos/olympus_blue_gold.png
    panasonic:
      id: Panasonic
      path: ./logos/panasonic.png
    pentax:
      id: PENTAX
      path: ./logos/pentax.png
    ricoh:
      id: RICOH
      path: ./logos/ricoh.png
    sony:
      id: SONY
      path: ./logos/sony.png
```

### Layout.Element.Name 可选项

| 可选项                 | 描述                                                 |
| ---------------------- | ---------------------------------------------------- |
| Model                  | 相机型号(eg. Nikon Z7)                               |
| Make                   | 相机厂商(eg. Nikon)                                  |
| LensModel              | 镜头型号(eg. Nikkor 24-70 f/2.8)                     |
| Param                  | 拍摄参数(eg. 50mm f/1.8 1/1000s ISO 100)             |
| Datetime               | 拍摄时间(eg. 2023-01-01 12:00)                       |
| Date                   | 拍摄日期(eg. 2023-01-01)                             |
| Custom                 | 自定义                                               |
| None                   | 无                                                   |
| LensMake_LensModel     | 镜头厂商 + 镜头型号(eg. Nikon Nikkor 24-70 f/2.8)    |
| CameraModel_LensModel  | 相机型号 + 镜头型号(eg. Nikon Z7 Nikkor 24-70 f/2.8) |
| TotalPixel             | 总像素(MP)                                           |
| CameraMake_CameraModel | 相机厂商 + 相机型号(eg. DJI FC123)                   |

### Layout.Type 可选项

| 可选项                            | 描述                        | 效果                |
| --------------------------------- | --------------------------- | ------------------- |
| watermark_left_logo               | normal                      | ![1](images/1.jpeg) |
| watermark_right_logo              | normal(Logo 居右)           | ![2](images/2.jpeg) |
| dark_watermark_left_logo          | normal(黑红配色)            | ![3](images/3.jpeg) |
| dark_watermark_right_logo         | normal(黑红配色，Logo 居右) | ![4](images/4.jpeg) |
| custom_watermark                  | normal(自定义配置)          | ![5](images/5.jpeg) |
| square                            | 1:1 填充                    | ![6](images/6.jpeg) |
| simple                            | 简洁                        | ![7](images/7.jpeg) |
| background_blur                   | 背景模糊                    | ![8](images/8.jpeg) |
| background_blur_with_white_border | 背景模糊+白框               | ![9](images/9.jpeg) |

</details> -->
