# importo la clase
from game.components.power_ups.power_up import PowerUp

from game.utils.constants import DEFAULT_TYPE, THUNDER


class SpeedPowerUp(PowerUp):
    def __init__(self):
        super().__init__(THUNDER, DEFAULT_TYPE)