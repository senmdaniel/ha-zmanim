from datetime import timedelta
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
import logging
from .utils import calculate_zmanim

_LOGGER = logging.getLogger(__name__)

class ZmanimCoordinator(DataUpdateCoordinator):

    def __init__(self, hass, config):
        super().__init__(
            hass,
            _LOGGER,
            name="zmanim",
            update_interval=timedelta(minutes=5),
        )

        self.lat = config.get("latitude")
        self.lon = config.get("longitude")
        self.method = config.get("method", "gra")

    async def _async_update_data(self):
        try:
            _LOGGER.debug("Calculating zmanim...")
            return calculate_zmanim(self.lat, self.lon, self.method)
        except Exception as e:
            _LOGGER.exception("Zmanim error: %s", e)
            return {
                "alot_hashachar": None,
                "netz": None,
                "chatzot": None,
                "shkia": None,
                "tzeit": None,
            }
