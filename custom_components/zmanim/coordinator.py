from datetime import timedelta
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
import logging
from .utils import calculate_zmanim
from .loxone import LoxoneExporter

_LOGGER = logging.getLogger(__name__)

class ZmanimCoordinator(DataUpdateCoordinator):

    def __init__(self, hass, config):
        super().__init__(
            hass,
            _LOGGER,
            name="zmanim",
            update_interval=timedelta(minutes=5),
        )

        self.lat = config["latitude"]
        self.lon = config["longitude"]
        self.method = config.get("method", "gra")

        self.loxone_enabled = config.get("enable_loxone", False)
        self.loxone_url = config.get("loxone_url")

        self.loxone = LoxoneExporter(self.loxone_url) if self.loxone_url else None

    async def _async_update_data(self):
        data = calculate_zmanim(self.lat, self.lon, self.method)

        # 🔥 AUTO LOXONE EXPORT
        if self.loxone_enabled and self.loxone:
            await self.loxone.send(data)

        return data
