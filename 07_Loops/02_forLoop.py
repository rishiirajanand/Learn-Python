# 1. print the elements of the following list using for for loop
# 2. Search for a number x in this tuple using list
# [1,4,9,16,18,33,78,100]

# list  = [1,4,9,16,18,33,78,100]

# for num in list : 
#     print(num)


# 2. Search for a number x in this tuple using list
# (1,4,9,16,18,33,78,100)

tuple = (1,4,9,16,18,33,78,100)
x = 78

for num in tuple :
    if(num == x) : 
        print('Found')
        break
else :
    print('Not Found')
