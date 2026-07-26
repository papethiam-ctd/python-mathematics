import math

# ==========================================
# Numerical Methods in Python
# Author: Samba THIAM
# ==========================================

# Fonction à étudier
def f(x):
    return x**3 - x - 2

# Dérivée de la fonction
def df(x):
    return 3*x**2 - 1


# ------------------------------------------
# 1. Bisection Method
# ------------------------------------------
def bisection(a, b, tol=1e-6):

    while (b - a) / 2 > tol:

        c = (a + b) / 2

        if f(c) == 0:
            return c

        elif f(a) * f(c) < 0:
            b = c

        else:
            a = c

    return (a + b) / 2


# ------------------------------------------
# 2. Newton Method
# ------------------------------------------
def newton(x0, tol=1e-6):

    x = x0

    while abs(f(x)) > tol:

        x = x - f(x)/df(x)

    return x


# ------------------------------------------
# 3. Secant Method
# ------------------------------------------
def secant(x0, x1, tol=1e-6):

    while abs(f(x1)) > tol:

        x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))

        x0 = x1
        x1 = x2

    return x1


# ------------------------------------------
# 4. Euler Method
# y' = x + y
# ------------------------------------------
def euler(x0, y0, h, n):

    x = x0
    y = y0

    print("\nEuler Method")

    for i in range(n):

        y = y + h*(x + y)
        x = x + h

        print("x =", round(x,3),
              " y =", round(y,6))


# ==========================================
# Results
# ==========================================

print("Bisection :", bisection(1,2))

print("Newton :", newton(1.5))

print("Secant :", secant(1,2))

euler(0,1,0.1,10)
