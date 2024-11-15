import sympy as sp

def euler_method(func_str, y0, x0, xn, step):
    # Перетворення рядка у функцію за допомогою sympy
    x, y = sp.symbols('x y')
    func = sp.sympify(func_str)
    f = sp.lambdify((x, y), func, 'numpy')  # Перетворення в функцію для обчислень
    
    # Масиви для значень x та y
    x_values = [x0]
    y_values = [y0]
    
    # Метод Ейлера
    x_curr, y_curr = x0, y0
    while x_curr < xn:
        y_next = y_curr + step * f(x_curr, y_curr)
        x_curr += step
        
        x_values.append(x_curr)
        y_values.append(y_next)
        y_curr = y_next
    
    return x_values, y_values

def runge_kutta_method(func_str, y0, x0, xn, step):
    # Перетворення рядка у функцію за допомогою sympy
    x, y = sp.symbols('x y')
    func = sp.sympify(func_str)
    f = sp.lambdify((x, y), func, 'numpy')  # Перетворення в функцію для обчислень
    
    # Масиви для значень x та y
    x_values = [x0]
    y_values = [y0]
    
    # Метод Рунге-Кутта
    x_curr, y_curr = x0, y0
    while x_curr < xn:
        k1 = step * f(x_curr, y_curr)
        k2 = step * f(x_curr + step / 2, y_curr + k1 / 2)
        k3 = step * f(x_curr + step / 2, y_curr + k2 / 2)
        k4 = step * f(x_curr + step, y_curr + k3)
        
        y_next = y_curr + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x_curr += step
        
        x_values.append(x_curr)
        y_values.append(y_next)
        y_curr = y_next
    
    return x_values, y_values