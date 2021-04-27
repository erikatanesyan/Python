a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if a==b and b==c and a==c:
    print("Isosceles triangle")
elif a==b!=c or a==c!=b or b==c!=a:
    print("2 sides equal triangle")
elif a!=b or b!=c or a!=c:
    print("Simple triangle")
else:
    print("Impossible")

num = int(input("num: "))
if (num % 4 == 0) and (num % 100 != 0) or (num % 400 == 0):
    print('Yes')
else:
    print('No')

d = int(input("d: "))
f = int(input("f: "))
g = int(input("g: "))
h = int(input("h: "))

chess = abs(d - g) <= 1 and abs(f - h) <= 1 and (d, f) != (g, h)
print("YES" if chess else "NO")

