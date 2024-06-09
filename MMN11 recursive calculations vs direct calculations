import numpy as np
import matplotlib.pyplot as plt

n = 40
#recursive
a = np.empty(n)
a[0] = 1/3
a[1] = 1/12
for i in range(2,n):
    a[i] = 2.25*a[i-1] - 0.5*a[i-2]

#direct
b = np.empty(n)
for j in range(0,n-1):
    b[j] = pow(4,-j)/3

#added because of a bug in matplotlib which throw seemingly random as b[39]
b[39] = pow(4,-39)/3
x = np.arange(n)

plt.plot(x+1, np.log(np.abs(a)), 'r', x+1, np.log(np.abs(b)), 'g')
plt.show()

