from datetime import timedelta
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from .utils import calculate_zmanim

class ZmanimCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, lat, lon, method):
        super().__init__(
            hass,
            logger=None,
            name="zmanim",
            update_interval=timedelta(minutes=30),
        )

        self.lat = lat
        self.lon = lon
        self.method = method

    async def _async_update_data(self):
        return calculate_zmanim(self.lat, self.lon, self.method)
