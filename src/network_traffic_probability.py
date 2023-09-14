import numpy as np
from matplotlib import pyplot as plt
import math

# TODO: fix the floating point errors introduced
# due to addition of small numbers when step size is reduced:
# Try using kahan algorithm or figure out the problem by doing addition of
# numbers on python kernel


def probability_n_users(n: int, k: int, p: float) -> float:
    '''
    probability of n users using the network
    '''
    nCk = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
    p = nCk * np.power(p, k) * np.power(1-p, n - k)
    return p


if __name__ == "__main__":
    N = np.arange(35, 81, 7)
    K = np.arange(10, 16, 1)
    p = 0.1
    total_prob = 0
    # probability of > 10 users in 35 capacity network.
    for i in range(11, 36):
        total_prob = total_prob + probability_n_users(35, i, p)

    print(f"Probability of users > 11 using the network in capacity of 35 \
            users: {total_prob} \n \n")

    for k in K:
        tp = 0
        total_prob_variation = []
        for n in N:
            for i in range(k, n):
                tp = tp + probability_n_users(n, i, p)
            total_prob_variation.append(tp)
        plt.plot(N, np.array(total_prob_variation), '--o')
        print(f'total probability variation with user size={N} \
              - p={np.array(total_prob_variation)} \n')
    plt.legend(K)
    plt.minorticks_on()
    plt.grid(True, which='major')
    plt.xlabel('number of users (N)')
    plt.ylabel('probability that atleast k users are online')
    plt.show()
