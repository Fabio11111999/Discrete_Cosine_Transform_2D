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
    f = f.astype('float64')
    N = len(f)
    t = [(2 * i + 1) / (2 * N) for i in range(0, N)]
    alpha = get_alpha(N)
    c = np.array([0] * N).astype('float64')

    # New version
    # TODO: convert everything to numpy
    t = np.array(t)
    alpha = np.array(alpha)
    f = np.array(f)
    for k in range(0, N):
        c[k] = np.sum(f * alpha[k] * np.cos(math.pi * k * t))

    return c

def my_idct(c):
    c = c.astype('float64')
    N = len(c)
    t = [(2 * i + 1) / (2 * N) for i in range(0, N)]
    alpha = get_alpha(N)
    f = [0] * N

    # New version
    # TODO: convert everything to numpy
    t = np.array(t)
    alpha = np.array(alpha)
    f = np.array(f).astype('float64')
    ran_k = np.zeros(N)
    for i in range(0, N):
        ran_k[i] = i
    for i in range(0, N):
        f[i] = np.sum(c * alpha * np.cos(math.pi * ran_k * t[i]))

    return f

def my_dct2(pf):
    f = np.copy(pf.astype('float64'))
    n, m = f.shape
    for j in range(m):
        f[:,j] = my_dct(f[:,j])
    for i in range(n):
        f[i,:] = my_dct(f[i,:])
    return f
    
def my_idct2(pc):
    c = np.copy(pc.astype('float64'))
    n, m = c.shape
    for i in range(n):
        c[i,:] = my_idct(c[i,:])
    for j in range(m):
        c[:,j] = my_idct(c[:,j])
    return c

def check_pdf_examples():
    # 1D
    print(my_dct(np.loadtxt('CheckValues/1d.txt')))
    # 2D
    print(my_dct2(np.loadtxt('CheckValues/2d.txt')))

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
    check_pdf_examples()
    for sz in range(20, 501, 20):
        print(sz, test(sz))


if __name__ == '__main__':
    main()

