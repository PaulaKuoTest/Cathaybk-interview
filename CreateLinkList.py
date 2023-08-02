def create_linkList(n):
    # 建立一個包含n個人的列表，從1到n
    people = list(range(1, n+1))
    
    # 從第一個人開始報數，從0開始計數
    index = 0
    
    while len(people) > 1:
        # 報到3的人退出圈子，用索引刪除該人
        index = (index + 2) % len(people)
        del people[index]
        
    # 如果列表為空，表示原本沒有人參加，直接返回0
    if len(people) == 0:
        return 0

    # 返回最後留下的人的順位
    return people[0]

if __name__ == "__main__":
    n = int(input("請輸入n值(0-100): "))
    if 0 <= n <= 100:
        result = create_linkList(n)
        if result != 0:
            print(f"最後留下的同事是第 {result} 順位")
        else:
            print("原本沒有人參加，最後留下的同事是第 0 順位")
    else:
        print("輸入值超出範圍，請輸入0-100之間的整數。")