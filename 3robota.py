import cmath

a, b, c = map(float, input("Введіть коф a b c через пробіл: ").split())

# розрахунок дискримінанту
discriminant = cmath.sqrt(b**2 - 4*a*c)

# Пошук коренів
root1 = (-b + discriminant) / (2 * a)
root2 = (-b - discriminant) / (2 * a)

# ваш результат
print(f"Корінь 1: {root1}")
print(f"Корінь 2: {root2}")
