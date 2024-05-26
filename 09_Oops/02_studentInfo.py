class Student :
    college = 'ABC'
    def __init__(this, name) : 
        this.name = name

    def showInfo(this) : 
        print(this.college, this.name)

s1 = Student('Rishi')
s1.showInfo()