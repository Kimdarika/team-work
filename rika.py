# Ex-1
text='AbbaBAaAb'
countA=0
countB=0
for char in text:
    if char .lower()=='a': 
        countA+=1
    elif char =='b':
        countB+=1
print('A and a', countA)
print('b:', countB)

text='AbbaBAaAb'
for i in range(len(text)):
    print(text[i])
# Ex2
number= 9
num = False
userNum = int (input("Please Enter your number: "))
while not num:
    if userNum == number:
        print("you are correct!")
        num = True
    else:
        print("You are not correct")
        userNum = int(input("Please Enter your number: "))