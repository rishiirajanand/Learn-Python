# def show(n) :
#     if(n == 0) :
#         return
#     print(n)
#     show(n-1)

# show(5)

# find a factorial using recursion

def fact(n) :
    if(n==0) : 
        return 1

    return n * fact(n-1) 

print(fact(5))
