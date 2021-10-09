from flask import Blueprint

from controllers.crypto_controller import get_coins, get_specific_coin

crypto_bp = Blueprint('crypto_bp', __name__)

# Shows all
crypto_bp.route('/', methods=['GET'])(get_coins)

# Shows bitcoin
crypto_bp.route('/<coin_name>', methods=['GET'])(get_specific_coin)
