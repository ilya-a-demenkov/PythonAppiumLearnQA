class MainClass:

    def getLocalNumber(self):
        return 14


class MainClassTest(MainClass):

    def testGetLocalNumber(self):
        if self.getLocalNumber == 14:
            return "Тест пройден: значение 14"
        return "Тест провален: значение не 14"