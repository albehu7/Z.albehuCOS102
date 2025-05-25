import numpy as np

def solve_quadratic(a, b, c):
    roots = np.roots([a, b, c])
    return roots

def solve_cubic(a, b, c, d):
    roots = np.roots([a, b, c, d])
    return roots

def solve_quartic(a, b, c, d, e):
    roots = np.roots([a, b, c, d, e])
    return roots

print("Select equation type to solve:")
print("1. Quadratic (Ax^2 + Bx + C = 0)")
print("2. Cubic (Ax^3 + Bx^2 + Cx + D = 0)")
print("3. Quartic (Ax^4 + Bx^3 + Cx^2 + Dx + E = 0)")

choice = input("Enter choice (1/2/3): ")

if choice == '1':
    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    c = float(input("Enter C: "))
    roots = solve_quadratic(a, b, c)
    print(f"Quadratic roots: {roots}")

elif choice == '2':
    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    c = float(input("Enter C: "))
    d = float(input("Enter D: "))
    roots = solve_cubic(a, b, c, d)
    print(f"Cubic roots: {roots}")

elif choice == '3':
    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    c = float(input("Enter C: "))
    d = float(input("Enter D: "))
    e = float(input("Enter E: "))
    roots = solve_quartic(a, b, c, d, e)
    print(f"Quartic roots: {roots}")

else:
    print("Invalid choice.")