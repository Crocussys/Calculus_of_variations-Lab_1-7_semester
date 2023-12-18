import sympy
from sympy.abc import x
import matplotlib.pyplot as plt
import math

x0 = -1
y0 = 2
x1 = 1
y1 = 4
delta = 100
count_iterations = 3


def f(var_y_derivative, var_y, var_x):
    return var_y_derivative ** 2 - 4 * var_y ** 2 + 2 * var_x * var_y - var_x ** 2


def exact(var_x):
    return 3 * math.cos(2 * var_x) / math.cos(2) + 3 * math.sin(2 * var_x) / (4 * math.sin(2)) + 1 / 4 * var_x


if __name__ == '__main__':
    x_all_values = [i / delta for i in range(x0 * delta, x1 * delta + 1)]
    styles = ["--", "-.", ":"]
    fig, ax = plt.subplots()
    ax.plot(x_all_values, list(map(exact, x_all_values)), label="Точное решение")
    y = (y1 - y0) / (x1 - x0) * (x - x0) + y0
    for i in range(1, count_iterations + 1):
        phi_system = list()
        y += sympy.Symbol(f'alpha{i}') * (x - x0) ** i * (x1 - x)
        y1 = y.diff(x)
        phi_alpha_i = sympy.integrate(f(y1, y, x), (x, x0, x1))
        for j in range(1, i + 1):
            phi_system.append(sympy.Equality(phi_alpha_i.diff(sympy.Symbol(f'alpha{j}')), 0))
        alphas = sympy.solve(phi_system)
        print(alphas)
        y_print = y
        for j in range(1, i + 1):
            symbol = sympy.Symbol(f'alpha{j}')
            y_print = y_print.subs(symbol, alphas[symbol])
        print(f"y{i} = {y_print}")
        if i == 3:
            ax.plot(x_all_values, list(map(lambda _x: y_print.subs(x, _x), x_all_values)), styles[i - 1], label=f"y{i}", linewidth=3)
        else:
            ax.plot(x_all_values, list(map(lambda _x: y_print.subs(x, _x), x_all_values)), styles[i - 1], label=f"y{i}")
    ax.grid(which='major', color='gray', linestyle=':')
    ax.legend()
    plt.xlim([x0, x1])
    plt.ylabel("y", fontsize=14)
    plt.xlabel("x", fontsize=14)
    plt.savefig("chart.svg")
    plt.show()
