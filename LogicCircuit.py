# Данный код реализует построение схем с помощью логических вентилей
# NOT,AND,OR,NAND,NOR,XOR,XNOR и соединителей.

# Шаблон для вентиля. Отсюда будут наследоваться все остальные вентили.
class LogicGate:

    def __init__(self, n):
        self.name = n
        self.output = None

# У каждого вентиля будет метка для их дальнейшей идентификации.
    def getName(self):
        return self.name

# Каждый вентиль должен вычислять значение на выходе посредством взаимодействия со входными значениями.
    def getOutput(self):
        self.output = self.performGateLogic() # У каждого типа вентилей будет разная логика вычисления.
        return self.output

# Вентиль с двумя входами (к ним относятся AND,OR,NAND,NOR,XOR,XNOR)
class BinaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pinA = None
        self.pinB = None

# Значения для входов первоначальных вентилей в схеме задаются вручную,
# Входы последующих будут получать значения от выходов предыдущих вентилей.
    def getPinA(self):
        if self.pinA == None:
            return int(input("Введите значение входа A для вентиля "+self.getName()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Введите значение входа B для вентиля "+self.getName()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Соединение невозможно (нет свободных входов)")

# Вентиль И
class AndGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

# Вентиль ИЛИ
class OrGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


# Вентиль НЕ И
class NandGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 0
        else:
            return 1


# Вентиль НЕ ИЛИ
class NorGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 0 and b == 0:
            return 1
        else:
            return 0


# Вентиль исключающее ИЛИ
class XorGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 0 and b == 1:
            return 1
        elif a == 1 and b == 0:
            return 1
        else:
            return 0

# Вентиль исключающее ИЛИ с инверсией
class XnorGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 0 and b == 0:
            return 1
        elif a == 1 and b == 1:
            return 1
        else:
            return 0

# Вентиль с одним входом
class UnaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Введите значение входа для вентиля "+self.getName()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print("Соединение невозможно (нет свободных входов)")

# Вентиль НЕ
class NotGate(UnaryGate):

    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1


# Соединитель берёт значение с выхода одного вентиля и подаёт его на вход следующего.
class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate

# Пример построения схемы с использованием всех возможных вентилей.
def main():
   g1 = AndGate("G1")
   g2 = AndGate("G2")
   g3 = OrGate("G3")
   g4 = OrGate("G4")
   g5 = NorGate("G5")
   g6 = XorGate("G6")
   g7 = XnorGate("G7")
   g8 = NotGate("G8")
   c1 = Connector(g1, g5)
   c2 = Connector(g2, g5)
   c3 = Connector(g3, g6)
   c4 = Connector(g4, g6)
   c5 = Connector(g5, g7)
   c6 = Connector(g6, g7)
   c7 = Connector(g7, g8)

   print(g8.getOutput())

main()