# 方法 1
def power2n_method1(n):
    return 2**n

# 方法 2a：用遞迴
def power2n_method2a(n):
    if n == 0:
        return 1
    else:
        return power2n_method2a(n-1) + power2n_method2a(n-1)

# 方法 2b：用遞迴
def power2n_method2b(n):
    if n == 0:
        return 1
    else:
        return 2 * power2n_method2b(n-1)

# 方法 3：用遞迴+查表
def power2n_method3(n, memo={}):
    if n == 0:
        return 1
    if n not in memo:
        memo[n] = power2n_method3(n-1, memo) + power2n_method3(n-1, memo)
    return memo[n]

# 測試程式
def test_power2n():
    n = 5

    # 方法 1 測試
    result_method1 = power2n_method1(n)
    print(f"方法 1 結果：{result_method1}")

    # 方法 2a 測試
    result_method2a = power2n_method2a(n)
    print(f"方法 2a 結果：{result_method2a}")

    # 方法 2b 測試
    result_method2b = power2n_method2b(n)
    print(f"方法 2b 結果：{result_method2b}")

    # 方法 3 測試
    result_method3 = power2n_method3(n)
    print(f"方法 3 結果：{result_method3}")

# 執行測試
test_power2n()
