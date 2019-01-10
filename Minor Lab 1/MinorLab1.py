def minor1(n):
    # Finds the nth term of the convergence.
    e = (1+(1/n))**n

    # Calculates the sigma notation for the nth term.
    sigma = 0
    for i in range(n+1):
        sigma = sigma + 5*(i**2)

    # Calculates the product notation for the nth term.
    product = 1
    for i in range(1, n+1):
        product = product * 3*(i**2)

    return e, sigma, product

# Test Case
result = minor1(5)
print("e_convergence =", result[0])
print("sigma =", result[1])
print("product =", result[2])
