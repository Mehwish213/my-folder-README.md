import random
b=[" "]*9
print(b)
computer="0"
user ="x"

    
n= int(input("enter cell no : "))
n1=random.randint(0,8)
b[n1]=computer

print(b)
b[n]=user
print(b)

def board(b):
    return f'''
    {b[0]} I {b[1]} I {b[2]}
    {b[3]} I {b[4]} I {b[5]}
    {b[6]} I {b[7]} I {b[8]}
    '''
print(board(b))
print("h")
