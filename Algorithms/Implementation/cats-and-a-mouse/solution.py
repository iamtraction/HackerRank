def catAndMouse(a, b, c):
    cat_a = abs(a - c)
    cat_b = abs(b - c)
    return "Cat A" if cat_a < cat_b else "Cat B" if cat_b < cat_a else "Mouse C"
