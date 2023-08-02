def hollow_triangle(n):
    try:
        num = int(n)
    except ValueError:
        raise ValueError("請輸入整數")
    
    if num <= 0:
        raise ValueError("請輸入正整數")

    triangle = ""
    for i in range(num):
        triangle += " " * (num - i - 1) + "*"  # 添加左側空格和星號
        if i > 0:
            triangle += " " * (2 * i - 1) + "*"  # 添加中間空格和星號（空心部分）
        triangle += "\n"  # 換行

    return triangle

# 測試函數
num_input = input("請輸入數字：")
try:
    result = hollow_triangle(num_input)
    print(result)
except ValueError as e:
    print("錯誤：", e)