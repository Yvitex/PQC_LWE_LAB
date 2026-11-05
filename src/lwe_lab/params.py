from dataclasses import dataclass

@dataclass(frozen=True)
class Params:
    n: int # this pertains to dimension, the higher the number, the harder it is to crack
    m: int # pertains to how many noisy equation the public key have
    q: int # q is always a prime number.
    eta: int # eta, is an n with longer leg, and pertains to noise, in ML-KEM standard, it's usually 2 or 3

TOY = Params(n=8, m=32, q=97, eta=1)

# q is always a prime number because we perform modulo on it, and it must turn back to 0 1 time
# in a full rotation like a clock. We can modulo 97 by 97 to make it 0, like a clock.

# imagine this, 1 mod 97 is 1, 2 mod 97 is 2, 3 mod 97 is 3, then 97 mod 97 is back to 0, 98 mod 97 is 1


# Fact: the smallest prime number is 2. Not 1, because 1 is divisible by a single divisor but 
# a prime number should be divisible by 2 divisor, itself and 1.
# the ml kem standard uses: `n = 256, q = 3329, η = 2 or 3` and this causes so large numbers