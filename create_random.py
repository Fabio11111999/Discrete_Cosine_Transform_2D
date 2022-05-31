from PIL import Image
import random


def main():
    width = height = 512
    img = Image.new(mode='L', size=(width, height))
    pixels = img.load()
    for i in range(width):
        for j in range(height):
            pixels[i, j] = random.randint(0, 255)
    img.save('random.bmp')



if __name__ == '__main__':
    main()
