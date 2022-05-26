from dct import my_dct2, my_idct2
from scipy.fftpack import dct, idct
from PIL import Image
import numpy as np
import itertools

def img_dct(F, d, file):
    # Opening the image
    img = Image.open(file).convert("L")
    img_arr = np.array(img)
    new_img = np.zeros(img_arr.shape)

    # Separating FxF blocks
    coord = [(x, y) for x in range(0, img_arr.shape[0]-F+1, F)
             for y in range(0, img_arr.shape[1]-F+1, F)]
    blocks = []
    for (x, y) in coord:
        blocks.append(np.copy(img_arr[x:x+F, y:y+F]))
        
    for (f, (x, y)) in zip(blocks, coord):
        # Applying DCT2
        c = dct(dct(f, axis=0, norm='ortho'), axis=1, norm='ortho')

        # Cutting frequencies (with threshold d)
        for k in range(0, F):
            for l in range(0, F):
                if k+l >= d:
                    c[k][l] = 0.0
                    
        # Applying I-DCT2
        ff = idct(idct(c, axis=1, norm='ortho'), axis=0, norm='ortho')
        
        # Bounding to [0, 255] and
        # mapping the block in the converted array
        ff = ff.astype('int')
        ff = np.maximum(ff, 0)
        ff = np.minimum(ff, 255)
        new_img[x:x+F, y:y+F] = ff   

    # Saving the image
    res = Image.fromarray(new_img.astype('uint8'))
    res = res.convert("L")
    res.save("result.bmp")
    return

def main():
    img_dct(8, 5, "Immagini/deer.bmp")

if __name__ == "__main__":
    main()
        
                
