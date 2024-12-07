for x in range(10000, 1000, -1):
    z = str(x)
    k1 = int(z[0]) + int(z[1])
    k2 = int(z[1]) + int(z[2])
    k3 = int(z[2]) + int(z[3])
    first = str(k1 + k2 + k3 - max(k1, k2, k3) - min(k1, k2, k3))
    second = str(max(k1, k2, k3))
    a1 = first + second
    if a1 == '1517':
        print(x)
        break