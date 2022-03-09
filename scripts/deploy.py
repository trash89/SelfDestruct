from brownie import accounts, EtherGame, EtherGameFixed, Attack, AttackEGF, exceptions
import pytest


def main():
    eg = EtherGame.deploy({"from": accounts[0]})
    print(f"EtherGame deployed at {eg}")

    print("Accounts[1] depositing 1 ether...")
    tx = eg.deposit({"from": accounts[1], "value": "1 ether"})
    tx.wait(1)

    print("Accounts[2] depositing 1 ether...")
    tx = eg.deposit({"from": accounts[2], "value": "1 ether"})
    tx.wait(1)
    print(
        f"Accounts 1 and 2 deposited 1 ether each. EtherGame balance is {eg.balance()}")

    att = Attack.deploy(eg.address, {"from": accounts[0]})
    print(f"Attack deployed at {att}")

    tx = att.attack({"from": accounts[0], "value": "5 ether"})
    tx.wait(1)
    print(f"EtherGame balance is now {eg.balance()}")

    with pytest.raises(exceptions.VirtualMachineError):
        print("Accounts[3] trying to depositing 1 ether...Game is over!")
        tx = eg.deposit({"from": accounts[3], "value": "1 ether"})
        tx.wait(1)

    print(f"EtherGame winner() is {eg.winner()}")

    egf = EtherGameFixed.deploy({"from": accounts[0]})
    print(f"EtherGameFixed deployed at {egf}")

    print("Accounts[0] depositing 1 ether...")
    tx = egf.deposit({"from": accounts[0], "value": "1 ether"})
    tx.wait(1)

    print("Accounts[1] depositing 1 ether...")
    tx = egf.deposit({"from": accounts[1], "value": "1 ether"})
    tx.wait(1)
    print(
        f"Accounts 0 and 1 deposited 1 ether each. EtherGameFixed balance is {egf.balance()}, bal is {egf.bal()}")

    attegf = AttackEGF.deploy(egf.address, {"from": accounts[2]})
    print(f"AttackEGF deployed at {attegf}")

    print("Attacking with attack, 1 ether")
    tx = attegf.attack({"from": accounts[2], "value": "1 ether"})
    tx.wait(1)
    print(
        f"EtherGameFixed balance is {egf.balance()}, bal is {egf.bal()}")

    print("Accounts[2] depositing 1 ether...")
    tx = egf.deposit({"from": accounts[2], "value": "1 ether"})
    tx.wait(1)
    print(
        f"Accounts 2 deposited 1 ether. EtherGameFixed balance is {egf.balance()}, bal is {egf.bal()}")

    print(f"EtherGameFixed winner() is {egf.winner()}")

    print(
        f"Accounts[2] balance() before claimReward() is {accounts[2].balance()}")

    print("Accounts[2] claimReward()...")
    tx = egf.claimReward({"from": accounts[2]})
    tx.wait(1)

    print(
        f"Accounts[2] balance() after claimReward() is {accounts[2].balance()}")
