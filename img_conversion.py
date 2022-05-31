from dct import my_dct2, my_idct2
from scipy.fftpack import dct, idct
from PIL import Image
import numpy as np
import io
import itertools
from PIL import ImageFile


def img_conv(F, d, img):
    # Converting the image to a numpy array
    if img.mode != "L":
        img = img.convert("L")
    img_arr = np.array(img)
    res_arr = np.zeros((img_arr.shape[0] - img_arr.shape[0] % F,
                        img_arr.shape[1] - img_arr.shape[1] % F))

    # Section 1
    # Separating F X F blocks
    coord = [(x, y) for x in range(0, img_arr.shape[0]-F+1, F)
             for y in range(0, img_arr.shape[1]-F+1, F)]
    blocks = []
    for (x, y) in coord:
        blocks.append(np.copy(img_arr[x:x+F, y:y+F]))

    # Section 2
    for (f, (x, y)) in zip(blocks, coord):
        # Section 2.1
        # Applying DCT2
        c = dct(dct(f, axis=0, norm='ortho'), axis=1, norm='ortho')

        # Section 2.2
        # Cutting frequencies (with threshold d)
        for k in range(0, F):
            for l in range(0, F):
                if k+l >= d:
                    c[k][l] = 0.0
                    
        # Section 2.3
        # Applying I-DCT2
        res_f = idct(idct(c, axis=1, norm='ortho'), axis=0, norm='ortho')
        
        # Section 2.4
        # Bounding to [0, 255] and
        # mapping the block in the converted array
        res_f = res_f.astype('int')
        res_f = np.maximum(res_f, 0)
        res_f = np.minimum(res_f, 255)
        res_arr[x:x+F, y:y+F] = res_f   

    # Converting the array to an image
    res = Image.fromarray(res_arr.astype('uint8'))
    res = res.convert("L")
    return res

def open_img(path):
    return Image.open(path)

def save_img(img, path):
    img.save(path)

def img_dct(F, d, load_path, save_path):
    # Opening the image
    img = open_img(load_path)
    conv_img = img_conv(F, d, img)
    save_img(conv_img, save_path)
    return

def main():
    img_dct(20, 5, "Immagini/bridge1.bmp", "result.bmp")

if __name__ == "__main__":
    main()
        
                
