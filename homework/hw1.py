def fibonacci(n):
    fib_sequence = [0, 1]
    
    for i in range(2, n+1):
        next_number = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_number)
    
    return fib_sequence

# 例子：打印前10个斐波那契数
result = fibonacci(10)
print(result)
