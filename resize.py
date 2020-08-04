from PIL import Image
import sys
import os
import re

input_path = "datasets/mgan-dataset/"
output_path = "datasets/resized_images/"
files = os.listdir(input_path)
count = 1

# すべてデータ量の少ないjpgに変換
for file in files:
  if file[-4:] == ".png":
    # pngの時は背景処理に注意する
    image=Image.open(os.path.join(input_path, file)).convert("RGBA")
    image.load()
    background = Image.new("RGB", image.size, (255, 255, 255))
    background.paste(image, mask=image.split()[3])
    background = background.resize((64, 64))
    background.save(output_path + os.path.splitext(file)[0] + ".jpg") 
  elif file[-4:] == ".jpg":
    # jpgの時は読み込んでそのままリサイズすればいい
    image = Image.open(os.path.join(input_path, file))
    image = image.resize((64, 64))
    image.save(output_path + os.path.splitext(file)[0] + ".jpg")
    count = count + 1