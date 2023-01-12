class MainClass:
    __class_number = 20
    __class_string = "Hello, world"

    def getClassString(self):
        return __class_string

    def getClassNumber(self):
        return __class_number

    def getLocalNumber(self):
        return 14

class MainClassTest(MainClass):

    def testGetClassString(self):
        if "hello" in self.getClassString or "Hello" in self.getClassString:
            return "Тест пройден: строка содержит hello или Hello"
        return "Тест провален: строка не содержит hello или Hello"

    def testGetClassNumber(self):
        if self.getClassNumber > 45:
            return "Тест пройден: значение больше 45"
        return "Тест провален: значение не больше 45"

    def testGetLocalNumber(self):
        if self.getLocalNumber == 14:
            return "Тест пройден: значение 14"
        return "Тест провален: значение не 14"