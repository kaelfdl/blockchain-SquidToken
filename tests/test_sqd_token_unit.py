import pytest
from brownie import exceptions, accounts
from scripts.helpful_scripts import get_account
from scripts.deploy_token import deploy_token


def test_deploy_token():
    # Arrange
    account = get_account()
    # Act
    tx = deploy_token()
    starting_contract_balance = tx.balance()
    starting_owner_balance = tx.balanceOf(account)
    expected_contract_balance = 0
    expected_owner_balance = 10 ** 27
    # Assert
    assert starting_contract_balance == expected_contract_balance
    assert starting_owner_balance == expected_owner_balance


def test_can_transfer():
    # Arrange
    token = deploy_token()
    sender = get_account(index=0)  # Contract owner
    recipient = get_account(index=1)
    amount = 10 ** 18
    # Act
    starting_balance_of_sender = token.balanceOf(sender)
    starting_balance_of_recipient = token.balanceOf(recipient)
    tx = token.transfer(recipient, amount, {"from": sender})
    tx.wait(1)
    # Assert
    assert token.balanceOf(sender) == (starting_balance_of_sender - amount)
    assert token.balanceOf(recipient) == (starting_balance_of_recipient + amount)


def test_cannot_transfer_insuffient_balance():
    # Arrange
    token = deploy_token()
    sender = get_account(index=0)
    recipient = get_account(index=1)
    amount = token.balanceOf(sender) + 1
    # Act / Assert
    with pytest.raises(exceptions.VirtualMachineError):
        token.transfer(recipient, amount, {"from": sender})
