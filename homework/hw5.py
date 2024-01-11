import random

def neighbor(f, p, h=0.01):
    """找尋鄰近的點"""
    q = p.copy()
    i = random.randint(0, len(p) - 1)
    q[i] = q[i] + h
    return q, f(*q)

def hillClimbing(f, p, h=0.01):
    failCount = 0  # 失敗次數歸零
    while failCount < 10000:  # 如果失敗次數小於一萬次就繼續執行
        fnow = f(*p)  # fnow 為目前高度
        p1, f1 = neighbor(f, p, h)
        if f1 >= fnow:  # 如果移動後高度比現在高
            fnow = f1  # 就移過去
            p = p1
            print('p=', p, 'f(p)=', fnow)
            failCount = 0  # 失敗次數歸零
        else:  # 若沒有更高
            failCount += 1  # 那就又失敗一次
    return p, fnow  # 結束傳回（已經失敗超過一萬次了）

def f(*args):
    # 這裡的 f 函數支援任意維度的向量
    # 例如：return -1 * (args[0]**2 + args[1]**2 + args[2]**2)
    return -1 * sum(x**2 for x in args)

# 使用示例
result = hillClimbing(f, [2, 1, 3])
print("Final result:", result)
