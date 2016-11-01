def Karatsuba_mltiply(a, b):
    '''
    fast multiply a and b which have same even number digits
    '''
    digit_length = len(str(a))
    a_str = str(a)
    b_str = str(b)
    divide_index = len(a_str) // 2
    a1 = int(a_str[:divide_index])
    a2 = int(a_str[divide_index:])
    b1 = int(b_str[:divide_index])
    b2 = int(b_str[divide_index:])
    # print(a1, a2, b1, b2)
    a1b1 = a1 * b1
    a2b2 = a2 * b2
    ad_bc = (a1 + a2) * (b1 + b2) - a1b1 - a2b2
    return 10**digit_length * a1b1 + 10**(digit_length / 2) * ad_bc + a2b2

print(Karatsuba_mltiply(3141592653589793238462643383279502884197169399375105820974944592,
                        2718281828459045235360287471352662497757247093699959574966967627))
