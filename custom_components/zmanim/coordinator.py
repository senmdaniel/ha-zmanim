from datetime import timedelta
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
import logging
from .utils import calculate_zmanim

_LOGGER = logging.getLogger(__name__)

class ZmanimCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, lat, lon, method):
        super().__init__(
            hass,
            _LOGGER,
            name="zmanim",
            update_interval=timedelta(minutes=30),
        )

        self.lat = lat
        self.lon = lon
        self.method = method

    async def _async_update_data(self):
        try:
            return calculate_zmanim(self.lat, self.lon, self.method)
        except Exception as e:
            _LOGGER.exception("Zmanim calculation failed: %s", e)
            return {}
