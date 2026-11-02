while True:
    try:
        def add(a1, a2):
            return a1 + a2
        def sub(a, b):
            return a - b
        def mul(f1, f2):
            return f1 * f2
        def div(dd, ds):
            return dd / ds

        op = input("Enter operation (+, -, *, /): ")
        n1 = float(input("Enter 1st number: "))
        n2 = float(input("Enter 2nd number: "))
        if op == "+":
            an = add(n1, n2)
            print(f"The answer is: {an}")
        elif op == "-":
            an = sub(n1, n2)
            print(f"The answer is: {an}")
        elif op == "*":
            an = mul(n1, n2)
            print(f"The answer is: {an}")
        elif op == "/":
            an = div(n1, n2)
            print(f"The answer is: {an}")
        else:
            print("Operation must be +, -, *, or /")
    except ValueError:
        print("Enter valid numbers")
    except ZeroDivisionError:
        print("Divisor cannot be 0")