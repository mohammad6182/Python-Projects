class Cars:
    def __init__(self):
        self._carsvar =2

obj = Cars()
obj._carsvar = 'Red'
print(obj._carsvar)

class Cars:
    def __init__(self):
        self.__privateVar = 'Blue'
    def getPrivate(self):
        print(self.__privateVar)
    def setPrivate(self, private):
        self.__privateVar = private

obj = Cars()
obj.getPrivate()
obj.setPrivate('Pink')
obj.getPrivate()


