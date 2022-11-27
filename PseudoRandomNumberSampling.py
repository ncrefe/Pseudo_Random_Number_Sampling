import numpy as np
import numpy.random
from matplotlib import pyplot as plt

# Recommendation: Run this code in debug mode

# Part a (Inverse Transform Method)
U = []
Xa = []
av_Xa = []
vr_Xa = []


# Populate the given arrays.
def getMean(list: list) -> float:
    return sum(list) / len(list)


def getVariance(list: list, mean) -> float:
    return sum([(i - mean) ** 2 for i in list]) / len(list)


for i in range(50000):
    U.append(np.random.rand())
    Xa.append(numpy.sqrt(U[i]))
    mean = getMean(Xa)
    av_Xa.append(mean)
    vr_Xa.append(getVariance(Xa, mean))

# Inspect the following plots.
plt.figure()
for i in range(len(Xa)):
    plt.plot([Xa[i], U[i]], [1, 1.2])

plt.figure()
hU = plt.hist(U, 100, alpha=0.5, density=True)
hXa = plt.hist(Xa, 100, alpha=0.5, density=True)

plt.figure()
plt.plot(np.cumsum(hU[0]))
plt.plot(np.cumsum(hXa[0]))

# Plot the average and variance values.
yaxis = [i for i in range(0, 50000)]

plt.figure()
plt.title("Average Part A")
plt.plot(yaxis, av_Xa, label="Average")

plt.figure()
plt.title("Variance Part A")
plt.plot(yaxis, vr_Xa, label="Variance")

# Part b (Rejection Method)
Xb = []
av_Xb = []
vr_Xb = []


# Populate the given arrays.

# F(x)=x^2 derivative it and then f(x)=2x
# If we create a rectangle between 0-1 in axis x and 0-2 in axis y  ,it will include it

def f(x):
    if x < 1:
        return 2 * x
    else:
        return 0


a = 0
b = 1
c = 2
while len(Xb) < 50000:
    u = numpy.random.rand()
    v = numpy.random.rand()
    x = (b - a) * u + a
    y = c * v
    if y < f(x):
        Xb.append(x)
        mean = getMean(Xb)
        av_Xb.append(mean)
        vr_Xb.append(getVariance(Xb, mean))

# Inspect the following plots.
plt.figure()
hXb = plt.hist(Xb, 100, density=True)

plt.figure()
plt.plot(np.cumsum(hXb[0]))

# Plot the average and variance values.
plt.figure()
plt.title("Average Part B")
plt.plot(yaxis, av_Xb, label="Average")

plt.figure()
plt.title("Variance Part B")
plt.plot(yaxis, vr_Xb, label="Variance")

plt.show()
