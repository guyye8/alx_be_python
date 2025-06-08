F,C=5/9,9/5
def f2c(f):return (f-32)*F
def c2f(c):return c*C+32

try:
    t=float(input("Temp: "))
    u=input("(C/F): ").upper()
    print(f"{t}{u} = {c2f(t):.1f}F"if u=='C'else f"{t}{u} = {f2c(t):.1f}C"if u=='F'else"Invalid unit")
except ValueError:print("Invalid number")
