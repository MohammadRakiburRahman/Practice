def beautiful_array(z, a):
    b = [0] * z
    b[0] = a[0]
    for i in range(1, z):
        b[i] = min(a[i], b[i - 1])
    return b

t = int(input())

for _ in range(t):
    z = int(input())
    a = list(map(int, input().split()))

    beautiful_array = beautiful_array(z, a)
    print(*beautiful_array)