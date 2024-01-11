def min_edit_distance(str1, str2):
    # 如果其中一個字串為空，則操作次數為另一個字串的長度
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)

    # 如果最後一個字元相同，則不需要操作，直接計算前面子字串的編輯距離
    if str1[-1] == str2[-1]:
        return min_edit_distance(str1[:-1], str2[:-1])

    # 否則，計算插入、刪除、替換操作後的最小編輯距離
    insert_cost = 1 + min_edit_distance(str1, str2[:-1])
    delete_cost = 1 + min_edit_distance(str1[:-1], str2)
    replace_cost = 1 + min_edit_distance(str1[:-1], str2[:-1])

    # 返回三種操作中的最小編輯距離
    return min(insert_cost, delete_cost, replace_cost)

# 測試
str1 = "kitten"
str2 = "sitting"
result = min_edit_distance(str1, str2)
print(f"The minimum edit distance between '{str1}' and '{str2}' is {result}.")