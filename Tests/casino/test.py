from crash_numbers import crash_numbers as a

treshold=1

import numpy as np
import matplotlib.pyplot as plt

def miser(n, cash, bet, treshold) :
    cash += -bet
    if n >= treshold :
        cash += bet*treshold
    return cash

# t = 6.468
# print(len(a))
print(np.mean(a))

from scipy.optimize import minimize
import json


def compute():
    bet = 10    #ce qu'on pari à chaque fois
    cashs = []
    for t in np.linspace(0, 50, 1000):
        cash=100  #Notre argent
        for n in a:
            cash = miser(n, cash, bet, t)
        cashs.append((t, cash))

    # plt.show()

    json.dump(json.dumps(cashs),)




# plt.plot(*zip(*cashs))
#
# plt.savefig("graphe")

compute()
