# tìm dãy Fibonaci từ 0 đến 1000
n0 = 0
n1 = 1
n2 = 0
print(n0)
print(n1)
while n2<1000:
    n2 = n0 + n1
    if n2<1000:
        print(n2)
        n0 = n1
        n1 = n2
    else :
        break


