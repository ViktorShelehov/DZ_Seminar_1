# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
def can_break_chocolate(n, m, k):
    if n < 1 or m < 1 or k < 1:
        raise ValueError("Dimensions and number of breaks should be positive integers")
    
    total_pieces = n * m
    if k == total_pieces - 1:
        return True
    elif k > total_pieces - 1:
        return False
    else:
        return (k % n == 0) or (k % m == 0)

n = int(input("Введите количество долек по горизонтали (n): "))
m = int(input("Введите количество долек по вертикали (m): "))
k = int(input("Введите количество отломленных долек (k): "))

if can_break_chocolate(n, m, k):
    print("Можно отломить", k, "долек")
else:
    print("Нельзя отломить", k, "долек")