from math import gcd

def lcm(a, b):
    return int(a * b / gcd(a, b))


p = int(input("p: "))
q = int(input("q: "))
e = int(input("e: "))

n = p * q
l = lcm(p - 1, q - 1)

if gcd(e, l) != 1:
    print("e と lcm(p-1, q-1) は互いに素である必要があります")
    exit(1)

d = pow(e, -1, l)

print()
print(f"公開鍵: n={n}, e={e}")
print(f"秘密鍵: p={p}, q={q}, d={d}")

print()
x = int(input("平文 x: "))

c = pow(x, e, n)
xx = pow(c, d, n)

print()
print(f"暗号文: c={c}")
print(f"復号文: x={xx}")
