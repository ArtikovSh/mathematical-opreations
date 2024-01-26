a = int(input('Birinchi sonni kiriting: '))
b = int(input('ikkinchi sonni kiriting: '))
print(f"{a}+{b}={a+b},\n{a}-{b}={a-b},\n{a}*{b}={a*b},")
if a/b-int(a/b)==0:
    print(f"{a}:{b}={a//b}.")
else:
    print(f"{a}:{b}={a/b}.")
    