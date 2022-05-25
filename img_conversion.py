from dct import my_dct2, my_idct2
from PIL import Image
import numpy as np

def img_dct(F, d, file):
    # Opening the image
    img = Image.open(file).convert("L")
    img_arr = np.array(img)
    new_img = np.zeros(img_arr.shape)

    # Separating blocks
    coord = [(x, y) for x in range(0, img_arr.shape[0]-F+1, F)
             for y in range(0, img_arr.shape[1]-F+1, F)]
    blocks = []
    for (x, y) in coord:
        blocks.append(img_arr[x:x+F, y:y+F])
        
    for (f, (x, y)) in zip(blocks, coord):
        # Applying DCT2
        c = my_dct2(f)
        # Cutting frequencies
        for k in range(0, F):
            for l in range(0, F):
                if k+l >= d:
                    c[k][l] = 0.0
        # Applying I-DCT2
        ff = my_idct2(c)
        # Bounding to [0, 255] and
        # mapping the block in the converted array
        for k in range(0, F):
            for l in range(0, F):
                ff[k][l] = int(ff[k][l])
                ff[k][l] = max(ff[k][l], 0)
                ff[k][l] = min(ff[k][l], 255)
                new_img[k+x][l+y] = ff[k][l]

    # Saving the image
    res = Image.fromarray(new_img.astype('uint8'))
    res = res.convert("L")
    res.save("result.bmp")
    return

def main():
    img_dct(8, 3, "Immagini/prova.bmp")

if __name__ == "__main__":
    main()
        
                
