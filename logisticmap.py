
import numpy as np
import matplotlib.pyplot as plt

def logisticmap(r,x):
    return r*x*(1-x)


def iteration(seed, n_skip, n_iter, step=0.0001, r_min=0):
    R = []
    X = []
    
    r_range = np.linspace(r_min, 4, int(1/step))

    for r in r_range:
        x = seed
        
        for i in range(n_iter+n_skip+1):
            if i >= n_skip:
                R.append(r)
                X.append(x)
                
            x = logisticmap(r,x)
   

    plt.scatter(R, X, s=0.1)
    plt.show()


    
iteration(0.2, 1000, 10, r_min=2)