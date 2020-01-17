class Account(object):
    def __init__(self,rate):
        self.__amt = 0
        self.rate = rate

    # def amount(self):
    #     return self.__amt

    def cny(self):
        return self.__amt*self.rate

    def amount(self,value):
        if value < 0:
            print("Sorry, no negative amount in the account.")
            return self.rate

if __name__ == "__main__":
    acc = Account(rate = 6.6)
    acc.amount = 20
    print("Dollar amount: ",acc.amount)
    print("In CNY:{}".format(acc.cny))
    acc.amount=-120
    print("Dollar amount: ",acc.amount)
