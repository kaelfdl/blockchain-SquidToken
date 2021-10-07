from brownie import accounts, network, config
from brownie.network.contract import Contract

LOCAL_BLOCKCHAIN_ENV = ["development", "ganache-cli"]


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if network.show_active() in LOCAL_BLOCKCHAIN_ENV:
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])
