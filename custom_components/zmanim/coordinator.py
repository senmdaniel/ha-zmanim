import logging
from datetime import timedelta
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from .utils import calculate_zmanim
import aiohttp

_LOGGER = logging.getLogger(__name__)

class ZmanimCoordinator(DataUpdateCoordinator):
    """Coordinator voor Zmanim data."""

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
        self.loxone_url = config.get("loxone_url")

    async def _async_update_data(self):
        data = calculate_zmanim(self.lat, self.lon, self.method)

        # Optioneel naar Loxone sturen
        if self.loxone_url:
            await self._send_to_loxone(data)

        return data

    async def _send_to_loxone(self, data):
        try:
            async with aiohttp.ClientSession() as session:
                await session.post(self.loxone_url, json=data)
        except Exception as e:
            _LOGGER.error("Loxone error: %s", e)
