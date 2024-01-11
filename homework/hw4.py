def solve_equation_bruteforce():
    solutions = []
    for x in range(-1000, 1001):  # 假设 x 在 -1000 到 1000 之间
        equation_result = x**2 - 3*x + 1
        if equation_result == 0:
            solutions.append(x)
    return solutions

solutions_bruteforce = solve_equation_bruteforce()
print("Bruteforce solutions:", solutions_bruteforce)
