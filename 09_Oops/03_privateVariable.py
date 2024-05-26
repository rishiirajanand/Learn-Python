class Account : 

    __name = 'Rishi'

    def __init__(this, amount, acNo) :
        this.__amount = amount
        this.__acNo = acNo
    
    def show(this) :
        print(this.__amount, this.__acNo, this.__name)

a1 = Account(3200, 1234)
a1.show()
# print(a1.__name) #can't access private variable