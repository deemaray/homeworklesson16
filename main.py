print("Equation: ax^2 + bx + c ")

a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
d = (b**2) - (4*a*c)


if a == 0:
    print("that is wrong")
elif delta > 0:
    print("The roots are", (-b - delta ** 0.5) / (2 * a), "and", (-b + delta ** 0.5) / (2 * a))
elif delta == 0:
    print("The root is", (-b) / (2 * a))
elif delta < 0:
    print("There are no real roots")



quit()

