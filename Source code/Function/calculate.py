def calculate(n):
    if n <= 1:
        return n
    
    fi_minus_2 = 0
    fi_minus_1 = 1

    for i in range(2, n + 1):
        fi = 2 * fi_minus_1 + fi_minus_2
        fi_minus_2, fi_minus_1 = fi_minus_1, fi
    return fi
