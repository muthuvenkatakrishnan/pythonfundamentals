# ATMMachine
# ATMCard
# Person
# Money

# ATM Machine dispense cash
# Ambani sells potatoes
# 

class AtmMachine:

    def dispense(self, card, pin, amount):
        return Cash()


class Card:
    pass
class Cash:
    pass

class Person:

    def withdrawMoney(self,atmmachine, card):
        atmmachine = AtmMachine()
        atmmachine.dispense(card, 1233, 56730)
        print("Gotcha")

p = Person()
a = AtmMachine()
c = Card()
p.withdrawMoney(a,c)