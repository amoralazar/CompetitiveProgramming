#Algorithm

# 1, set a limit to the input that their value is between 1 and 16
# 2, since the dominos and board are in rectangular shape position won't alter the maximum number
# find the possibility that the board is perfectly hold the dominos and remove the extra one if exists

def domino_pilling(num1 ,num2):
    if(1 < num1 <= 16 and 1 < num2 <= 16 ):
        max_piece = (mum1 * num2) // 2
        return max_piece
    else:
        return -1

num1= int(input("Enter the num1 value: "))
num2 = int(input("Enter the num2 value: "))
print(domino_pilling(num1, num2))