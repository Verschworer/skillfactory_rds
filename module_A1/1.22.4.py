balance = 10000
spent = 2800

while balance > 0:
    balance -= spent
    if balance > 0:
        print(balance)
    else:
        print("Слишком большие расходы")