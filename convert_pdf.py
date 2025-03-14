from pdf2image import convert_from_path

# 将 PDF 转换为图片
images = convert_from_path("image_new/real_world_new.pdf", dpi=300)

# 保存图片
for i, image in enumerate(images):
    image.save(f"page_{i+1}.png", "PNG")
