import numpy as np 

# This method centers the numbers
# instead of a linear number from 0 to 96, where 96 have great distance to 0, we treat it as a clock
# if we treat this as clock, 0 and 96 are besides each other, and technically, 96 is -1 of 0.
# treating it as a clock and laying it flat on a line, using 0 as the center
# it will be like -48...-3, -2, -1, 0, 1, 2, 3...+48
def centered(x: int, q: int) -> int:

    # target x, q is the modulo and is a prime number, sample 97. x mod q will never be greater than q as it return to 0 when q mod q, q + 1 mod q = 1
    r = np.mod(x, q)

    # if r is greater than q // 2, then it means it should be negative on our line. 
    # if q is 97, and q // 2 is 48, if r is 96, we do 96 - 97 and we get -1
    # Now we can plot it like -48...-3, -2, -1, 0, 1, 2, 3...+48
    # instead of 98, 97, 96, 0, 1, 2, 3
    # note that // is divide then floor. 

    return np.where(r > q // 2, r - q, r) # means if r is greater than half a q, return r-q, else, r


