import math

def minor2(p, r, n, t):
    # A is the future value of p with compound interest.
    A = p*(1+(r/n))**(n*t)

    # B is also the future value of p with compound interest, but was calculated using a for loop.
    B = []
    total = p
    for i in range(1, (n*t)+1):
        total = total * (1+(r/n))
        B.append(total)

    # C is the future value of p with continuous compound interest.
    C = p*math.exp(r*t)

    # D is the relative difference between A and the last value of B expressed as a percentage.
    D = 100*((A-B[-1])/B[-1])

    # E is the relative difference between A and C expressed as a percentage.
    E = 100*((abs(A-C)/C))

    return A, B, C, D, E

# Test Case
result = minor2(100, 0.5, 4, 5)
print("A =", result[0])
print("B =", result[1])
print("C =", result[2])
print("D =", result[3])
print("E =", result[4])
