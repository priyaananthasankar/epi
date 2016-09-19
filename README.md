Tricks with Bitwise operations:

1. x & (x-1) will always drop the lowest set bit. 1011 & 1010 = 1010 and 1010 & 1001 = 1000 (lowest set bit drops).
2. XOR of a set of numbers will always cancel out the same bits and retain the different bits. Also XOR of a set of numbers will always cancel out same numbers and retain the different number.
3. x ^ y = z. z ^ y = x (XOR a number twice with another number yields original number)
4. x & 1 will give you the LSBit of x.
5. XOR is associative.
6. x & ~(x-1) will extract the lowest set bit of x.1011 & ~(1010) = 1011 & 0101 = 0001. 1010 & ~(1001) = 1010 & 0110 = 0010.
7. XOR of any number with all 1's will flip the bits of that number. Eg: 10110110 XOR 11111111 = 01001001. So if you want to flip specific bits of a certain number, construct another number where those bits alone are set to 1 and then XOR with the original number. The bits in those bit positions of original number will be flipped.
8. The easier way to rotate an array in circular manner with O(n) time is to calculate the possible values of indices when it rotates and retrieve the indices from the main array itself instead of the actual rotation. Also if the number of rotations are more than the actual number of elements, then the array will come back to original form after n rotations. Then number of rotations say k, k %n will be the remainder rotations that can be considered. Calculate the way it would have moved forward and do negative calculations backward on original array. 
