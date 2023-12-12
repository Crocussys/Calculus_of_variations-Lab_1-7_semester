import sympy
from sympy.abc import x, alpha
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math

x0 = -1
x1 = 1
delta = 100
count_iterations = 5


def f(var_y_derivative, var_y, var_x):
    return var_y_derivative ** 2 - 4 * var_y ** 2 + 2 * var_x * var_y - var_x ** 2


def exact(var_x):
    return 1 / 4 * var_x - math.sin(2 * var_x) / (4 * math.sin(2))


if __name__ == '__main__':
    x_all_values = [i / delta for i in range(x0 * delta, x1 * delta + 1)]
    fig, ax = plt.subplots()
    ax.plot(x_all_values, list(map(exact, x_all_values)), label="Точное решение")
    y = 0
    for i in range(1, count_iterations + 1):
        w = (x - x0) * (x - x1) * x ** i
        y += alpha * w
        y1 = y.diff(x)
        phi = sympy.integrate(f(y1, y, x), (x, x0, x1))
        phi1 = phi.diff(alpha)
        alp = sympy.solve(phi1, alpha)[0]
        y = y.subs(alpha, alp)
        print(f"{i}: {y}")
        ax.plot(x_all_values, list(map(lambda _x: y.subs(x, _x), x_all_values)), label=f"y{i}")

    ax.xaxis.set_major_locator(ticker.MultipleLocator(10 / delta))
    # ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.01))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(10 / delta))
    # ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))
    # ax.grid(which='major', color='gray')
    ax.grid(which='major', color='gray', linestyle=':')
    ax.legend()
    plt.xlim([x0, x1])
    # plt.ylim([-1, 1])
    plt.ylabel("y", fontsize=14)
    plt.xlabel("x", fontsize=14)
    plt.savefig("chart.svg")
    plt.show()
