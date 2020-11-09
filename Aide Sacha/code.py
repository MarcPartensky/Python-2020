#! /usr/bin/env python

"""
Created on Thu Oct 29 22:19:43 2020

@author: Maxence et Marc?
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("rawdata.csv")
t_serie = data['Time (s)']
x_serie = data['Rotation x (rad/s)']

# Stocker les t lors d'un changement de signe de x
l = []

x1 = x_serie[0]
for x, t in zip(x_serie[1:], t_serie[1:]):
    if x*x1<0:
        l.append(t)
    x1 = x

print("instants de changement de signe de vitesse radiale", l)

print("période moyenne", (l[-1]-l[0])/(len(l)*2))

t = range(len(l)//2-2)
l1 = []
for i in t:
    l1.append(l[2*i+1]-l[2*i])

# Évolution de la période au cours du temps
plt.plot(t,l1)
# plt.xlabal("temps (s)")
# plt.ylabel("Vz (rad/s")
plt.show()
