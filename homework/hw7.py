#參考了同學的程式碼並透過ChatGPT了解其中的運作方式後稍做修改
from micrograd.engine import Value

a = Value(2)
b = Value(1)
c = Value(3)

learning_rate = 0.01
tolerance = 0.001

while True:
    f = a**2 + b**2 + c**2

    print("a=", a.data, "b=", b.data, "c=", c.data, "f=", f.data)
    f.backward()

    # 檢查梯度的歐幾里得範數是否小於收斂標準
    gradient_norm = (a.grad**2 + b.grad**2 + c.grad**2)**0.5
    if gradient_norm < tolerance:
        break

    a -= a.grad * learning_rate
    b -= b.grad * learning_rate
    c -= c.grad * learning_rate

    # 重置梯度
    a.grad = 0.0
    b.grad = 0.0
    c.grad = 0.0
