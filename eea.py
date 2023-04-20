def extended_euclidean_algorithm(a, b):
    """
    拡張ユークリッドの互除法を使ってaとbの最大公約数と、その係数x, yを返す関数
    """
    if b == 0:
        return a, 1, 0

    gcd, x_prev, y_prev = extended_euclidean_algorithm(b, a % b)

    x = y_prev
    y = x_prev - (a // b) * y_prev

    return gcd, x, y


a = int(input("a: "))
b = int(input("b: "))
(gcd, x, y) = extended_euclidean_algorithm(a, b)
print(f"gcd: {gcd}, x: {x}, y: {y}")
