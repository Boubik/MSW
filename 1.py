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
    ska_soucin = np.dot(vec1, vec2)
    print("skalarní součin s numpy trval: " + str(time.time() - old_time) + "s")
    return ska_soucin
    

if __name__ == "__main__":
    # skalánrí součin
    vec1 = [ 2, 4, 6 ]
    vec2 = [ 3, 5, 7 ]
    num_vec1 = np.array([ 2, 4, 6 ])
    num_vec2 = np.array([ 3, 5, 7 ])
    print(skalarni_soucin(vec1, vec2))
    print(skalarni_soucin(num_vec1, num_vec2))
    
        