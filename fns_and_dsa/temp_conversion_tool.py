F_TO_C = 5/9
C_TO_F = 9/5

def f2c(f): return (f-32)*F_TO_C
def c2f(c): return c*C_TO_F+32

def main():
    try:
        t = float(input("Temp: "))
        u = input("(C/F): ").upper()
        if u == 'C': print(f"{t}C = {c2f(t):.1f}F")
        elif u == 'F': print(f"{t}F = {f2c(t):.1f}C")
        else: print("Invalid unit")
    except ValueError: print("Invalid number")

if __name__ == "__main__":
    main()
