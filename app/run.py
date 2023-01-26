import io
import requests
import json
import time
from PIL import Image
import os

volcanicforecard = requests.get('https://api.met.no/weatherapi/volcanicashforecast/0.1/')
volcanicforecardJson = json.loads(volcanicforecard.content)

xyz = volcanicforecardJson["layergroups"][0]["layers"][0]


def AttemtToDownload(downloadurl, name):
    img_data = requests.get(downloadurl).content
    time.sleep(1)
    image1 = Image.open(io.BytesIO(img_data))
    imagebg = Image.open("background.png")
    new_image = Image.new("RGB", (image1.width, image1.height))
    imagebg = imagebg.resize((image1.width, image1.height))
    new_image.paste(imagebg, (0, 0))
    new_image.paste(image1, (0,0), image1.convert('RGBA'))
    new_image.save("output/"+str(name)+'.png')


countr = 0
for asddasx in xyz["timesteps"]:
    xxxxxxx = ("https://api.met.no/weatherapi/volcanicashforecast/0.1"+(asddasx["url"][1:]))
    print("Downloading: "+str(countr))
    AttemtToDownload(xxxxxxx, countr)
    countr = countr+1




def extract_integer(filename):
    return int(filename.split('.')[0])

# Create an empty list to store the frames
frames = []


imgcounter = 0

# Iterate through all files in the subfolder
for file in sorted(os.listdir("output"), key=extract_integer):
    print(file)
    # Open the image file
    im = Image.open(os.path.join("output", file))
    # Append the image to the list of frames
    frames.append(im.resize((816,683)))
    imgcounter = imgcounter+1

# Save the frames as an animated GIF
frames[0].save("animation.gif", save_all=True, append_images=frames[1:], optimize=True, duration=50, loop=0)