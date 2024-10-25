import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# --------------------------- pandas -----------------------------
with open("data.csv", "a", encoding='utf-8') as file:
    for i in range(1, 10):
        file.write(f"{str(i * 2)}, ")
df = pd.read_csv("data.csv")
print(df.head())
print(df.describe())

# ------------------------- matplotlib ----------------------------
from random import randint

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = []
for k in range(1, 11):
    y.append(randint(1, 10))
plt.plot(x, y)
plt.ylabel("Y-axis")
plt.title("Line Plot")
plt.savefig("line_plot.png")
plt.show()

# --------------------------- pillow -----------------------------
import os


def resize_image(image_path):
    image = Image.open(image_path)
    image = image.resize((800, 600))
    image.save(image_path)


for i in range(1, 6):
    image_path = f"./images/{i}.jpg"
    resize_image(image_path)

image_dir = "./images"
images = []
for filename in os.listdir(image_dir):
    if filename.endswith(".jpg"):
        image_path = os.path.join(image_dir, filename)
        image = Image.open(image_path)
        images.append(image)
    # Создание слайд-шоу
images[0].save("slideshow.gif", save_all=True, append_images=images[1:], loop=0, duration=2000)
