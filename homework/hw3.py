def perm(n, p=[]):  # 主函數，使用預設參數 p=[]
    if len(p) == n:  # 全部排好了
        print(p)    # 印出排列
        return

    # 還沒排滿，繼續排下去
    for x in range(n):  # 對本列的每一個 x 去嘗試
        if x not in p:  # 若 x 不在排列中
            perm(n, p + [x])  # 把 x 放進盤面，使用新的列表 p + [x]，避免影響原先的列表 p

# 列出 2 個的排列
perm(2)

# 列出 3 個的排列
perm(3)

# 列出 4 個的排列
perm(4)

# 列出 5 個的排列
perm(5)
