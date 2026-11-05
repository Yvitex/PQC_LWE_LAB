from lwe_lab.params import TOY
import argparse
from lwe_lab.modq import centered
import numpy as np


def demo_params(p, rng):
    print(p)

def demo_modq(p, rng):
    for x in (0, 1, p.q // 2, p.q // 2 + 1, p.q // 2 - 1, p.q, -3):
        print(f"{x} mod {p.q} -> centered {int(centered(x, p.q))}")

# function that calcualtes a public key using a noiseless formula.
# The basic formula of this is b = (A * s) mod q
# where s is the list of n rows of numbers.  and A is a public matrix composed of random number of n * n shape
# For example, in n = 2
# A = [ 2  1 ]     s = [ 3 ]
#     [ 1  1 ]         [ 5 ]
# Our parameters are basically n = 8
def demo_noiseless(p, rng):
    s = rng.integers(0, p.q, size=p.n) # the secret, must be protected
    A = rng.integers(0, p.q, size=(p.n, p.n))
    b = (A * s) % p.q

    print("Secret: ", b)




DEMO = {
    "params": demo_params,
    "modq": demo_modq,
    "noiseless": demo_noiseless
}



def main() -> None:
    parser = argparse.ArgumentParser(description="LWE Lab")
    parser.add_argument("demo", choices=DEMO)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()
    rng = np.random.default_rng(args.seed)
    DEMO[args.demo](TOY, rng)


