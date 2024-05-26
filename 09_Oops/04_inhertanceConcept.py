class Car :

    __id = 101

    @staticmethod
    def start() :
        print('Start the car...')
    
    @staticmethod
    def stop() :
        print('Stop the car...')

class ToyotaCar(Car) :

    def __init__(this, name) :
        this.name = name
    
car1 = ToyotaCar('Fortuner')
car2 = ToyotaCar('Prius')

car1.start()
car1.stop()