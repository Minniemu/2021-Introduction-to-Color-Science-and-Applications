#4107056007-07-Bin2Dec.py
def ieee_754_conversion(s,expo,m):
    """
    Converts an arbitrary precision Floating Point number.
    Note: Since the calculations made by python inherently use floats, the accuracy is poor at high precision.

    :param n: An unsigned integer of length `sgn_len` + `exp_len` + `mant_len` to be decoded as a float
    :param sgn_len: number of sign bits
    :param exp_len: number of exponent bits
    :param mant_len: number of mantissa bits
    :return: IEEE 754 Floating Point representation of the number `n`
    """
    sgn_len=1
    exp_len=8
    mant_len=23
    '''if n >= 2 ** (sgn_len + exp_len + mant_len):
        raise ValueError("Number n is longer than prescribed parameters allows")
    '''
    sign = (int(s,2))
    exponent_raw = (int(expo,2))
    mantissa = (int(m,2))
    #print("0","{0:b}".format(n))
    # print("sign",sign)
    # print("exponent",exponent_raw)
    # print("mantissa",mantissa)
    
    sign_mult = 1
    if sign == 1:
        sign_mult = -1

    if exponent_raw == 2 ** exp_len - 1:  # Could be Inf or NaN
        if mantissa == 2 ** mant_len - 1:
            return float('nan')  # NaN

        return sign_mult * float('inf')  # Inf

    exponent = exponent_raw - (2 ** (exp_len - 1) - 1)

    if exponent_raw == 0:
        mant_mult = 0  # Gradual Underflow
    else:
        mant_mult = 1

    for b in range(mant_len - 1, -1, -1):
        if mantissa & (2 ** b):
            mant_mult += 1 / (2 ** (mant_len - b))

    return sign_mult * (2 ** exponent) * mant_mult


if __name__ == '__main__':
    import struct
    ieee_754 = []
    with open('sideinforbina.txt','r') as file:
        Lines = file.readlines()
        for i in Lines:
            num = i.strip()
            s = bin(int(num[0],2))
            expo = bin(int(num[1:9],2))
            m = bin(int(num[9:],2))
            #print("sign:{0} exponent:{1} mantissa:{2}".format(s,expo,m))
            result = round(ieee_754_conversion(s,expo,m),4)
            ieee_754.append(str(result)+"\n")
    
    #print(ieee_754)

    with open('sideinfordeci.txt','w') as out_file:
        out_file.writelines(ieee_754)
        out_file.close()
            