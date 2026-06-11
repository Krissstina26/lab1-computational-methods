# Модель: Метод Ньютона (5 семестр)
# Автор: Глазкова Крістіна, група АІ-232

import math

def f(x):
    """Функція f(x) = x^3 - 2x - 5"""
    return x**3 - 2*x - 5

def f_prime(x):
    """Похідна f'(x) = 3x^2 - 2"""
    return 3*x**2 - 2

def newton_method(x0, tolerance=1e-6, max_iterations=100):
    """
    Метод Ньютона для знаходження кореня рівняння f(x) = 0.
    
    Параметри:
        x0           - початкове наближення
        tolerance    - точність обчислення
        max_iterations - максимальна кількість ітерацій
    
    Повертає:
        корінь рівняння та кількість виконаних ітерацій
    """
    x = x0
    print(f"{'Ітерація':<12} {'x':<20} {'f(x)':<20} {'|f(x)|':<15}")
    print("-" * 67)

    for i in range(max_iterations):
        fx = f(x)
        fpx = f_prime(x)

        print(f"{i:<12} {x:<20.10f} {fx:<20.10f} {abs(fx):<15.10f}")

        if abs(fx) < tolerance:
            print(f"\nКорінь знайдено: x = {x:.10f}")
            print(f"Кількість ітерацій: {i}")
            print(f"f(x) = {fx:.2e}")
            return x, i

        if fpx == 0:
            print("Похідна дорівнює нулю. Метод не може продовжуватись.")
            return None, i

        x = x - fx / fpx

    print("Досягнуто максимальну кількість ітерацій.")
    return x, max_iterations


if __name__ == "__main__":
    print("=" * 67)
    print("  Метод Ньютона для розв'язання рівняння f(x) = x^3 - 2x - 5")
    print("=" * 67)

    x0 = 2.0
    print(f"\nПочаткове наближення: x0 = {x0}")
    print(f"Точність: 1e-6\n")

    root, iterations = newton_method(x0)

    if root is not None:
        print(f"\nПеревірка: f({root:.6f}) = {f(root):.2e}")
