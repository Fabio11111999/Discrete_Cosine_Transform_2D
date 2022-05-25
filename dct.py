import math 
import numpy as np
from scipy.fftpack import dct, idct
import time

def get_alpha(N):
    alpha = [1. / math.sqrt(N)] * N
    for i in range(1, N):
        alpha[i] = math.sqrt(2. / N)
    return alpha

def my_dct(f):
    N = len(f)
    t = [(2 * i + 1) / (2 * N) for i in range(0, N)]
    alpha = get_alpha(N)
    c = [0] * N
    for k in range(0, N):
        for i in range(0, N):
            c[k] += f[i] * alpha[k] * math.cos(math.pi * k * t[i])
    return c

def my_idct(c):
    N = len(c)
    t = [(2 * i + 1) / (2 * N) for i in range(0, N)]
    alpha = get_alpha(N)
    f = [0] * N
    for i in range(0, N):
        for k in range(0, N):
            f[i] += c[k] * alpha[k] * math.cos(math.pi * k * t[i])
    return f

def my_dct2(pf):
    f = np.copy(pf)
    n, m = f.shape
    for j in range(m):
        f[:,j] = my_dct(f[:,j])
    for i in range(n):
        f[i,:] = my_dct(f[i,:])
    return f
    
def my_idct2(pc):
    c = np.copy(pc)
    n, m = c.shape
    for i in range(n):
        c[i,:] = my_idct(c[i,:])
    for j in range(m):
        c[:,j] = my_idct(c[:,j])
    return c

def examples():
    # 1D
    f = np.array([3., 2., 5., 9., 1.])
    m_dct1 = my_dct(f)
    m_f = my_idct(m_dct1)
    print(m_dct1)
    print(m_f)


    lib_dct1 = dct(f, norm='ortho')
    lib_f = idct(lib_dct1, norm='ortho')
    print(lib_dct1)
    print(lib_f)

    # 2D
    f = np.array([[3., 2., 1., 4.], [9., 1., 4., 2.], [3., 3., 3., 1.]])
    m_dct2 = my_dct2(f)
    m_f = my_idct2(m_dct2)
    print(m_dct2)
    print(m_f)

    lib_dct2 = dct(dct(f, axis=0, norm='ortho'), axis=1, norm='ortho')
    lib_f = idct(idct(lib_dct2, axis=1, norm='ortho'), axis=0, norm='ortho')
    print(lib_dct2)
    print(lib_f)


def get_random_matrix(N):
    return np.random.uniform(low=-100.0, high=100.0, size=(N, N))

def test(N):
    f = get_random_matrix(N)
    
    start_my_time = time.time()
    m_dct2 = my_dct2(f)
    end_my_time = time.time()

    start_lib_time = time.time()
    lib_dct2 = dct(dct(f, axis=0, norm='ortho'), axis=1, norm='ortho')
    end_lib_time = time.time()

    return (end_my_time - start_my_time, end_lib_time - start_lib_time)
    
    

def main():
    for sz in range(20, 501, 20):
        print(sz, test(sz))


if __name__ == '__main__':
    main()

