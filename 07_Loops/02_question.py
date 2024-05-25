# 1. print the multiplication table of a number N

# num = int(input('Enter number : '))

# temp = 1
# while temp <= 10 :
#     multi = num*temp
#     print(multi)
#     temp += 1

# print('Loop Ended')

# ---------------------------------------------------------------

# 2. print the element of the folloing list using a loop:
# [1,4,9,6,25,36,49,64, 81,100]

# myLists = [1,4,9,6,25,36,49,64, 81,100]

# num = 0
# while num < len(mySet) :
#     print(mySet[num])
#     num +=1

# ---------------------------------------------------------------

# 3. Search for a number X in this tuple using loop
# (1,4,9,6,25,36,49,64, 81,100)

x = int(input('Enter X value : '))
myTuple = (1,4,9,6,25,36,49,64, 81,100)
num = 0

while num < len(myTuple) :
    if(myTuple[num] == x) :
        print('Found at index : ', num)
        break
    num+=1

