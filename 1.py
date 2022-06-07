import numpy as np
from scipy.integrate import trapz
import time


def skalarni_soucin(vektor1, vektor2):
    old_time = time.time()
    ska_soucin = 0
    for i in range(len(vektor1)):
        ska_soucin += vektor1[i] * vektor2[i]
    print("skalarní součin trval: " + str(time.time() - old_time) + "s")
    return ska_soucin


def numpy_skalarni_soucin(vektor1, vektor2):
    old_time = time.time()
    ska_soucin = np.dot(vektor1, vektor2)
    print("skalarní součin s numpy trval: " +
          str(time.time() - old_time) + "s")
    return ska_soucin


def determinant(matice):
    old_time = time.time()
    det = 0
    mat_len = len(matice)
    # přidání řůdků
    for i in range(len(matice)-1):
        matice.append(matice[i])
    # \/
    rr = list(reversed(range(mat_len)))
    for posun in range(mat_len):
        mezi_plus = 1
        mezi_minus = 1
        for xy in range(mat_len):
            # print("x="+str(xy)+" y="+str(xy+posun) +
            #      "\tx="+str(rr[xy])+" y="+str(xy+posun))
            mezi_plus *= matice[xy+posun][xy]
            mezi_minus *= matice[xy+posun][rr[xy]]
        det += mezi_plus
        det -= mezi_minus
        #print(" ")
    print("Determinant trval: " + str(time.time() - old_time) + "s")
    return det


def numpy_determinant(matice):
    old_time = time.time()
    det = np.linalg.det(matice)
    print("Determinant s numpy trval: " + str(time.time() - old_time) + "s")
    return det


def integral(bod1,bod2,step):
    old_time = time.time()
    rngup = int(1/step)
    x1 = [x * step for x in range(rngup*bod1,rngup*bod2+1)]    
    resault = 0
    for i in x1:    
        resault = resault + (3*i+2)*step
    end_time = time.time()
    print("integrál trval: " + str(time.time() - old_time) + "s")
    return resault

def numpy_integral(start, end, step):
    old_time = time.time()
    step = int(1/step)
    x = np.linspace(start, end, step)
    f = 3*x+2
    resault = trapz(f, x)
    print("integrál s numpy trval: " + str(time.time() - old_time) + "s")
    return resault


if __name__ == "__main__":
    # skalánrí součin
    vec1 = [2, 4, 6]
    vec2 = [3, 5, 7]
    num_vec1 = np.array([2, 4, 6])
    num_vec2 = np.array([3, 5, 7])
    print(skalarni_soucin(vec1, vec2))
    print(numpy_skalarni_soucin(num_vec1, num_vec2))

    # integral
    point1 = 0
    point2 = 10
    step = 0.000001
    print(integral(point1, point2, step))
    print(numpy_integral(point1, point2, step))

    # determinant
    vec = [[6, 1, 1], [4, -2, 5], [2, 8, 7]]
    num_vec = np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
    print(determinant(vec))
    print(numpy_determinant(num_vec))
