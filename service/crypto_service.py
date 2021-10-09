from pycoingecko import CoinGeckoAPI
from backend_logic import timed_lru_cache

cg = CoinGeckoAPI()


@timed_lru_cache(2)
def get_coins():
    global cg
    return cg.get_price(ids=['bitcoin', 'ethereum', 'tether', 'dogecoin'],
                        vs_currencies='eur', include_24hr_change='true')


@timed_lru_cache(2)
def get_specific_coin(coin_name):
    global cg
    print("Updating from server...")
    return cg.get_price(ids=coin_name, vs_currencies='eur', include_24hr_change='true')
