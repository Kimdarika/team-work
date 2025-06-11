for i in range(11):
    print(i)


for i in range (1,11):
    print(i)


numbers=[0,1,2,3,4,5,6,7,8,9,10]
for i in range (len(numbers)):
    print(numbers[-i-1])



n = 10
while n < 10:
    print(n)
    n +=1


numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i in range(len(numbers)):
    if numbers[i] % 2 == 1:
        print(numbers[i])



numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        print(numbers[i])


i=0 
while i <= 15:
    if i >= 4 and i <=8:
        print(i)
    i += 1



str='banana'
print(len(str))


str='banana'
print(str[4])


str='banana'
for i in range(len(str)):
    print(str[i])




str='banana'
for i in range(len(str)):
    print(str[-i-1])



str='banana'
count=0
for i in range (len(str)):
        if str[i]== 'a':
            count+=1
print(count)






fruits = ['banana', 'coconut', 'manago','jackfruit']
print(len(fruits))   


fruits = ['banana', 'coconut', 'manago','jackfruit']
for i in range (len(fruits)):
    print(fruits[i])



fruits = ['banana', 'coconut', 'manago','jackfruit']
fruits.append('durain')
print(fruits)


fruits = ['banana', 'coconut', 'manago','jackfruit']
fruits[0]= ('orange')
print(fruits)


fruits = ['banana', 'coconut', 'manago','jackfruit']
for i in range(len(fruits)):
    if fruits[i] == "manago":
        print(i)


numbers = [2, 3, 4, 5, 6, 7, 3, 8, 9, 3, 1]
sum=0
for i in range (len(numbers)):
    sum+=numbers[i]
print(sum)



numbers = [2, 3, 4, 5, 6, 7, 3, 8, 9, 3, 1]
sum=0
for i in range (len(numbers)):
    sum+=numbers[i]
print(sum/len (numbers))




numbers = [2, 3, 4, 5, 6, 7, 3, 8, 9, 3, 1]
count=0
for i in range (len(numbers)):
    if numbers[i]== 3:
        count+=1
print(count)



numbers = [2, 3, 4, 5, 6, 7, 3, 8, 9, 3, 1]
count=0
for i in range (len(numbers)):
    if numbers[i] %2== 1:
        count+=1
print(count)



numbers = [2, 3, 4, 5, 6, 7, 3, 8, 9, 3, 1]
sum=0
for i in range (len(numbers)):
    if numbers[i]%2== 0:
        sum+=numbers[i]
print(sum)



numbers = [2, 3, 4, 5, 6, 7, 3, 8, 9, 3, 1]
i=0
isFirstThree= False
while i < len(numbers) and not isFirstThree:
    if numbers[i] == 3:
        print(i)
        isFirstThree= True
    i +=1



numbers = [2,3,4,5,6,7,8,3,9,3,1]
newNumbers=[]
lastIndex = len(numbers)-1
for i in range (len(numbers)):
    newNumbers.append(numbers[lastIndex-i])
print(newNumbers)


scores = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],]
for i in range (len(scores)):
    for x in range (len(scores[i])):
        print(scores[i][x])




scores = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],]
sum =0
for i in range (len(scores)):
    for x in range (len(scores[i])):
        sum += scores[i][x]
print(sum)

userName='admin'
password='12345678'
isUserName=False
while not isUserName:
    name = input('Ente your name here:')
    passwords=input('Enter your password')
    if userName== name and passwords==password:
       print('login success')
       isUserName= True
    else:
        print('Try again')








students = [
    {"id": 1, "name": "Alice", "age": 18, "class": "A", "score": 85},
    {"id": 2, "name": "Bob", "age": 17, "class": "B", "score": 90},
    {"id": 3, "name": "Charlie", "age": 18, "class": "C", "score": 49},
    {"id": 4, "name": "Dara", "age": 19, "class": "A", "score": 92},
    {"id": 5, "name": "Eve", "age": 17, "class": "C", "score": 88}
]
for i in range(len(students)):
    print(students[i]['name'])



students = [
    {"id": 1, "name": "Alice", "age": 18, "class": "A", "score": 85},
    {"id": 2, "name": "Bob", "age": 17, "class": "B", "score": 90},
    {"id": 3, "name": "Charlie", "age": 18, "class": "C", "score": 49},
    {"id": 4, "name": "Dara", "age": 19, "class": "A", "score": 92},
    {"id": 5, "name": "Eve", "age": 17, "class": "C", "score": 88}
]

total_age=0
for students in students:
    total_age+=(students['age'])
print(total_age/len(students))



students = [
    {"id": 1, "name": "Alice", "age": 18, "class": "A", "score": 85},
    {"id": 2, "name": "Bob", "age": 17, "class": "B", "score": 90},
    {"id": 3, "name": "Charlie", "age": 18, "class": "C", "score": 49},
    {"id": 4, "name": "Dara", "age": 19, "class": "A", "score": 92},
    {"id": 5, "name": "Eve", "age": 17, "class": "C", "score": 88}
]
maxScore=students[0]['score']
topstudent=''
for student in students:
    if student['score']>maxScore:
        maxScore=student['score']
        topStudent=student['name']
print(topStudent)




students = [
    {"id": 1, "name": "Alice", "age": 18, "class": "A", "score": 85},
    {"id": 2, "name": "Bob", "age": 17, "class": "B", "score": 90},
    {"id": 3, "name": "Charlie", "age": 18, "class": "C", "score": 49},
    {"id": 4, "name": "Dara", "age": 19, "class": "A", "score": 92},
    {"id": 5, "name": "Eve", "age": 17, "class": "C", "score": 88}
]
maxScore=students[0]['score']
topstudent=''
for student in students:
    if student['score']< maxScore:
        maxScore=student['score']
        topStudent=student['name']
print(topStudent)




students = [
    {"id": 1, "name": "Alice", "age": 18, "class": "A", "score": 85},
    {"id": 2, "name": "Bob", "age": 17, "class": "B", "score": 90},
    {"id": 3, "name": "Charlie", "age": 18, "class": "C", "score": 49},
    {"id": 4, "name": "Dara", "age": 19, "class": "A", "score": 92},
    {"id": 5, "name": "Eve", "age": 17, "class": "C", "score": 88}
]

total_age=0
for students in students:
    total_age+=(students['score'])
print(total_age/len(students))



students = [
    {"id": 1, "name": "Alice", "age": 18, "class": "A", "score": 85},
    {"id": 2, "name": "Bob", "age": 17, "class": "B", "score": 90},
    {"id": 3, "name": "Charlie", "age": 18, "class": "C", "score": 49},
    {"id": 4, "name": "Dara", "age": 19, "class": "A", "score": 92},
    {"id": 5, "name": "Eve", "age": 17, "class": "C", "score": 88}
]

counter = 0
for student in students:
   if (student['class'] == "C"):
      counter += 1
print(counter)



def sumArray(array):
    sum=0
    for num in array:
        sum += num
    return sum
arr1 = [2, 4, 5, 6, 7, 9]
arr2 = [3, 5, 6]
arr3 = [4, 8, 9, 2, 1]
print(sumArray(arr1))
print(sumArray(arr2))
print(sumArray(arr3))



def sumArray(array):
    sum=0
    for num in array:
        sum += num
    return sum
def averageArray(array):
    return sumArray(array) / len(array)
arr1 = [2, 4, 5, 6, 7, 9]
arr2 = [3, 5, 6]
arr3 = [4, 8, 9, 2, 1]
print(averageArray(arr1))
print(averageArray(arr2))
print(averageArray(arr3))


def countOddNumber(array):
    counter = 0
    for i in array:
        if i % 2 != 0:
            counter+=1
    return counter
arr1 = [2, 4, 5, 6, 7, 9]
arr2 = [3, 5, 6]
arr3 = [4, 8, 9, 2, 1]
print(countOddNumber(arr1))
print(countOddNumber(arr2))
print(countOddNumber(arr3))




def findMax(array):
    max = array[0]
    for n in array:
        if n > max:
            max= n
    return max


arr1 = [2, 4, 5, 6, 7, 9]
arr2 = [3, 5, 6]
arr3 = [4, 8, 9, 2, 1]
print(findMax(arr1))
print(findMax(arr2))
print(findMax(arr3))




def replaeValue(array, value):
    for i in range (len(array)):
        if array [i] % 2== 0:
            array[i] = value 
    return array

arr1 = [2, 4, 5, 6, 7, 9]
arr2 = [3, 5, 6]
arr3 = [4, 8, 9, 2, 1]
print(replaeValue(arr1,100))
print(replaeValue(arr2,100))
print(replaeValue(arr3,100))




def findMin(array):
    min= array[0]
    for n in array:
         if n < min:
             max= n
         return min


arr1 = [5, 6, 56, 6, 7, 9]
arr2 = [3, 5, 7, 9, 8]
arr3 = [4, 8, 3, 2, 1, 7, 3, 9]
print(findMin(arr1))
print(findMin(arr2))
print(findMin(arr3))



def sumEvenNumber(array):
    sum =0
    for value in array:
        if value % 2==0:
            sum += value
    return sum
arr1 = [5, 6, 56, 6, 7, 9]
arr2 = [3, 5, 7, 9, 8]
arr3 = [4, 8, 3, 2, 1, 7, 3, 9]
print(sumEvenNumber(arr1))
print(sumEvenNumber(arr2))
print(sumEvenNumber(arr3))



def reverseArray(array):
    lenght = len(array)-1
    newArray=[]
    for i in range(len(array)):
        newArray.append(array[lenght-i])
    return newArray
arr1 = [5, 6, 56, 6, 7, 9]
arr2 = [3, 5, 7, 9, 8]
arr3 = [4, 8, 3, 2, 1, 7, 3, 9]
print(reverseArray(arr1))
print(reverseArray(arr2))
print(reverseArray(arr3))

    
        
arr1 = [5, 6, 56, 6, 7, 9]
arr2 = [3, 5, 7, 9, 8]
arr3 = [4, 8, 3, 2, 1, 7, 3, 9]
arr1.append(100)
arr2.append(100)
arr3.append(100)
print(arr1)
print(arr2)
print(arr3)



def indexNumSeven(list):
    myNewList = []
    for i in range(len(list)):
        if array[i] == 7:
            myNewList.append(i)
    return myNewList

array = [1,2,5,6,7,0,2,7,8,9]
result = indexNumSeven(list)
print(result)


myArray = [1,2,5,6,7,0,2,7,8,9]
isFound = False
index = 0
while not isFound:
    print(index)
    if myArray[index] == 7:
        print(index)
        isFound = True
    index+=1
    print(index)



def indexText(string):
    myNewText = []
    for i in range(len(text)):
        if text[i] == 'n':
            myNewText.append(i)
    return myNewText

text= 'banana'
result = indexText(list)
print(result)















