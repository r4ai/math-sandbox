def euclidean_algorithm(a, b):
    """
    ユークリッドの互除法を使ってaとbの最大公約数を返す関数
    """
    while b != 0:
        r = a % b
        a = b
        b = r
        print(f"a%b: {r}, a: {a}, b: {b}")
    return a


a = int(input("a: "))
b = int(input("b: "))
print(f"gcd: {euclidean_algorithm(a, b)}")
