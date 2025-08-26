import math
import random
import Information_atm

# Sytem ATM Machine Simulation ( Aidil )

mode = input("Options? \n1.Check Balance\t\t2.Deposit Money\n3.Withdraw Money\t4.Exit\n")

if mode == 1 :
    print("Your balance : {Information_atm.balance}")
