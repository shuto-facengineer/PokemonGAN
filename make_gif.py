from PIL import Image
import glob

files = sorted(glob.glob("results/00000-stylegan2-tf_images-1gpu-config-f/fakes0*.png"))
print(files)
images = list(map(lambda file: Image.open(file), files))
images[0].save('results/00000-stylegan2-tf_images-1gpu-config-f/000000-000288.gif', save_all=True, append_images=images[1:], duration=400, loop=0)