from lwe_lab.params import TOY
import argparse
from lwe_lab.modq import centered

def demo_params(p):
    print(p)

def demo_modq(p):
    for x in (0, 1, p.q // 2, p.q // 2 + 1, p.q // 2 - 1, p.q, -3):
        print(f"{x} mod {p.q} -> centered {int(centered(x, p.q))}")


DEMO = {
    "params": demo_params,
    "modq": demo_modq
}



def main() -> None:
    parser = argparse.ArgumentParser(description="LWE Lab")
    parser.add_argument("demo", choices=DEMO)
    args = parser.parse_args()
    DEMO[args.demo](TOY)


