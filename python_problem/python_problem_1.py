import random

def get_valid_input():
    while True:
        try:
            count = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
            if count in [1, 2, 3]:
                return count
            else:
                print("1, 2, 3 중 하나를 입력하세요")
        except ValueError:
            print("정수를 입력하세요")

def brGame():
    num = 0
    player = "player"
    
    while num < 31:
        if player == "player":
            count = get_valid_input()
            for i in range(1, count + 1):
                num += 1
                print(f"{player} {num}")
                if num == 31:
                    print("computer win!")
                    return
            player = "computer"
        else:
            count = random.randint(1, 3)
            for i in range(1, count + 1):
                num += 1
                print(f"{player} {num}")
                if num == 31:
                    print("player win!")
                    return
            player = "player"

brGame()