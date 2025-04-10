from bank_accounts import *

Kris = BankAccount(1000,"Kris")
Sara = BankAccount(2000,"Sara")

Kris.getBalance()
Kris.deposit(1000)

Kris.withdraw(1000)

Kris.transfer(1000,Sara)

Jim = InterestRewardsAcct(1000,"Jim")

Jim.getBalance()
Jim.deposit(100)

Jim.transfer(100,Kris)
Jim.getBalance()

Blaze = SavingsAcct(1000,"Blaze")
Blaze.getBalance()
Blaze.deposit(100)
Blaze.transfer(10000,Kris)
Blaze.transfer(100,Kris)