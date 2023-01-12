class MainClass:
    __class_number = 20

    def getClassNumber(self):
        return __class_number

    def getLocalNumber(self):
        return 14

class MainClassTest(MainClass):

    def testGetClassNumber(self):
        if self.getClassNumber > 45:
            return "Тест пройден: значение больше 45"
        return "Тест провален: значение не больше 45"

    def testGetLocalNumber(self):
        if self.getLocalNumber == 14:
            return "Тест пройден: значение 14"
        return "Тест провален: значение не 14"