#4107056007-07-Dec2Bin.py
def ieee_754_conversion(n, sgn_len=1, exp_len=8, mant_len=23):
    """
    Converts an arbitrary precision Floating Point number.
    Note: Since the calculations made by python inherently use floats, the accuracy is poor at high precision.

    :param n: An unsigned integer of length `sgn_len` + `exp_len` + `mant_len` to be decoded as a float
    :param sgn_len: number of sign bits
    :param exp_len: number of exponent bits
    :param mant_len: number of mantissa bits
    :return: IEEE 754 Floating Point representation of the number `n`
    """
    if n >= 2 ** (sgn_len + exp_len + mant_len):
        raise ValueError("Number n is longer than prescribed parameters allows")

    sign = (n & (2 ** sgn_len - 1) * (2 ** (exp_len + mant_len))) >> (exp_len + mant_len)
    exponent_raw = (n & ((2 ** exp_len - 1) * (2 ** mant_len))) >> mant_len
    mantissa = n & (2 ** mant_len - 1)
    ieee = str(0)+str(bin(n)[2:])+str("\n")
    ieee_754.append(ieee)
    
    #print("0","{0:b}".format(n))
    #print("sign",sign)
    #print("exponent",exponent_raw)
    #print("mantissa",mantissa)
    

if __name__ == '__main__':
    import struct
    ieee_754 = []
    with open('sideinfordeci.txt','r') as file:
        Lines = file.readlines()
        for i in Lines:
            num = float(i.strip())
            m = struct.unpack('I', struct.pack('f', num))[0]
            ieee_754_conversion(m, exp_len=8, mant_len=23)

    with open('sideinforbina.txt','w') as out_file:
        out_file.writelines(ieee_754)
        out_file.close()
        
            