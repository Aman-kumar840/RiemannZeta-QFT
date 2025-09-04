import numpy as np
from math import sqrt, log, pi, cos

def theta(t):
    return (t/2) * log(t/(2*pi)) - (t/2) - pi/8

def riemann_siegel(t, terms=None):
    if terms is None:
        terms = int(sqrt(t/(2*pi)))
    total = 0
    th = theta(t)
    for n in range(1, terms+1):
        total += cos(th - t*log(n)) / sqrt(n)
    return 2*total

if __name__ == "__main__":
    t = 1e4
    print(f"Z({t}) ≈ {riemann_siegel(t)}")
