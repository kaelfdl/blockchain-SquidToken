from brownie import SQDToken
from brownie.network import account
from scripts.helpful_scripts import get_account

# Total supply of 1 billion
initial_supply = 10 ** 27


def deploy_token():
    account = get_account()
    sqd_token = SQDToken.deploy(initial_supply, {"from": account})
    print(sqd_token.name())
    return sqd_token


def main():
    deploy_token()
