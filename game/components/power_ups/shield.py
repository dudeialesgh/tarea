# importo la clase
from game.components.power_ups.power_up import PowerUp

from game.utils.constants import SHIELD_TYPE, SHIELD


class Shield(PowerUp):
    def __init__(self):
        super().__init__(SHIELD, SHIELD_TYPE)