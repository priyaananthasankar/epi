Tricks with Bitwise operations:

1. x & (x-1) will always drop the lowest set bit. 1011 & 1010 = 1010 and 1010 & 1001 = 1000 (lowest set bit drops)
2. XOR of a set of numbers will always cancel out the same bits and retain the different bits. Also XOR of a set of numbers will always cancel out same numbers and retain the different number.
3. x ^ y = z. z ^ y = x (XOR a number twice with another number yields original number)
4. x & 1 will give you the LSBit of x.
5. XOR is associative.