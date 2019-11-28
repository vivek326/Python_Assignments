def wallet(previousbalance):
    balance: int = 0

    def deposit(amount):
        nonlocal balance

        print('Deposited')
        balance = previousbalance + amount
        print('New Balance:' + str(balance))

    def spend(amount):
        nonlocal balance

        if amount > balance:
            print('Not enough money in wallet')
        else:
            print('Deduction taking place')
            balance = balance - amount
            print('New Balance is:' + str(balance))

    def transfer(amount):
        nonlocal balance
        if balance < amount:
            print('Not enough money to transfer')
        else:
            balance = balance - amount

    return [deposit, spend]


w1 = wallet(1000)
w2=wallet(100)
w1[1](50)
w2[0](50)

