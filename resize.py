from PIL import Image
import sys
import os
import re
import argparse

parser = argparse.ArgumentParser(description='Resize images.')
parser.add_argument('--input_path', type=str, default="datasets/mgan-dataset/", help='Path to a dataset.')
parser.add_argument('--output_path', type=str, default="datasets/resized_images/", help='Path to resized images.')
args = parser.parse_args()

input_path = args.input_path
output_path = args.output_path
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
    background.save(os.path.join(output_path,  os.path.splitext(file)[0] + ".jpg"))
  elif file[-4:] == ".jpg":
    # jpgの時は読み込んでそのままリサイズすればいい
    image = Image.open(os.path.join(input_path, file))
    image = image.resize((64, 64))
    image.save(os.path.join(output_path, os.path.splitext(file)[0] + ".jpg"))
    count = count + 1