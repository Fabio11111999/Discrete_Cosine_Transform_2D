from img_conversion import img_conv, open_img
import matplotlib.pyplot as plt

def testBW():
    bw_img = open_img("Immagini/prova.bmp")
    F_vals = [2, 4, 5, 10, 15, 20, 25]
    ran_d = 7
    idx = 0
    fig, ax = plt.subplots(nrows = len(F_vals), ncols = ran_d)
    ax = ax.flatten()
    for F in F_vals:
        for d in range(ran_d):
            com_img = img_conv(F, d+1, bw_img)
            ax[idx].imshow(com_img.convert("RGB"))
            ax[idx].set_xticks([])
            ax[idx].set_yticks([])
            idx += 1
    for d in range(ran_d):
        plt.setp(ax[-1-d], xlabel=f'd = {ran_d-d}')
    idx_F = 0
    for F in F_vals:
        plt.setp(ax[idx_F], ylabel=f'F = {F}')
        idx_F += ran_d
    plt.show()

def testChess():
    bw_img = open_img("Immagini/160x160.bmp")
    F_vals = [2, 4, 8, 10, 16, 20, 40]
    ran_d = 7
    idx = 0
    fig, ax = plt.subplots(nrows = len(F_vals), ncols = ran_d)
    ax = ax.flatten()
    for F in F_vals:
        for d in range(ran_d):
            com_img = img_conv(F, d+1, bw_img)
            ax[idx].imshow(com_img.convert("RGB"))
            ax[idx].set_xticks([])
            ax[idx].set_yticks([])
            idx += 1
    for d in range(ran_d):
        plt.setp(ax[-1-d], xlabel=f'd = {ran_d-d}')
    idx_F = 0
    for F in F_vals:
        plt.setp(ax[idx_F], ylabel=f'F = {F}')
        idx_F += ran_d
    plt.show()

def testDeer():
    bw_img = open_img("Immagini/deer.bmp")
    dim = min(bw_img.size)
    F_vals = [2, 4, 5, 10, 15, 20, 25]
    ran_d = 7
    idx = 0
    fig, ax = plt.subplots(nrows = len(F_vals), ncols = ran_d)
    ax = ax.flatten()
    for F_perc in F_vals:
        F = (F_perc * dim) // 100
        for d in range(ran_d):
            com_img = img_conv(F, d+1, bw_img)
            ax[idx].imshow(com_img.convert("RGB"))
            ax[idx].set_xticks([])
            ax[idx].set_yticks([])
            idx += 1
    for d in range(ran_d):
        plt.setp(ax[-1-d], xlabel=f'd = {ran_d-d}')
    idx_F = 0
    for F in F_vals:
        plt.setp(ax[idx_F], ylabel=f'F = {F}%')
        idx_F += ran_d
    plt.show()

def main():
    testBW()
    testChess()
    testDeer()


if __name__ == "__main__":
    main()

