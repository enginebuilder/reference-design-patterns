class PaymentMethod:
    def __init__(self, balance):
        self.balance = balance

    def set_next(self, successor):
        self.successor = successor

    def pay(self, amount):
        if self.can_pay(amount):
            print(f"Paid amount using {type(self).__name__}")
        else:
            self.successor.pay(amount)
    
    def can_pay(self, amount):
        return amount >= self.balance

class Bank(PaymentMethod):

    def __init__(self, balance):
        super().__init__(balance)
    
class Venmo(PaymentMethod):

    def __init__(self, balance):
        super().__init__(balance)

if __name__ == "__main__":
    bank = Bank(100)
    venmo = Venmo(200)
    bank.set_next(venmo)
    bank.pay(120)



