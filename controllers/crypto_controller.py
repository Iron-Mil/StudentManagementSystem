from service import crypto_service


def get_coins():
    return crypto_service.get_coins()


def get_specific_coin(coin_name):
    return crypto_service.get_specific_coin(coin_name)

