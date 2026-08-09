import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# Differential Equations with Python
# Author: Samba THIAM
# ==========================================

# Équation différentielle :
# y' = y - x² + 1

def f(x, y):
    return y - x**2 + 1


# ==========================================
# Méthode d'Euler
# ==========================================

def euler(x0, y0, h, n):

    x = x0
    y = y0

    X = [x]
    Y = [y]

    for i in range(n):

        y = y + h * f(x, y)
        x = x + h

        X.append(x)
        Y.append(y)

    return X, Y


# ==========================================
# Méthode de Runge-Kutta d'ordre 4 (RK4)
# ==========================================

def rk4(x0, y0, h, n):

    x = x0
    y = y0

    X = [x]
    Y = [y]

    for i in range(n):

        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)

        y = y + (k1 + 2*k2 + 2*k3 + k4)/6
        x = x + h

        X.append(x)
        Y.append(y)

    return X, Y


# ==========================================
# Programme principal
# ==========================================

x0 = 0
y0 = 0.5
h = 0.2
n = 10

Xe, Ye = euler(x0, y0, h, n)
Xr, Yr = rk4(x0, y0, h, n)

print("Méthode d'Euler")
for i in range(len(Xe)):
    print(f"x = {Xe[i]:.2f}, y = {Ye[i]:.6f}")

print("\nMéthode RK4")
for i in range(len(Xr)):
    print(f"x = {Xr[i]:.2f}, y = {Yr[i]:.6f}")

# ==========================================
# Tracé des solutions
# ==========================================

plt.figure(figsize=(8,5))

plt.plot(Xe, Ye, 'o-', label="Euler")

plt.plot(Xr, Yr, 's-', label="Runge-Kutta 4")

plt.title("Numerical Solution of a Differential Equation")

plt.xlabel("x")

plt.ylabel("y")

plt.grid(True)

plt.legend()

plt.show()
