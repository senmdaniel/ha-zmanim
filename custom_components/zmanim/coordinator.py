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
            update_interval=timedelta(minutes=10),
        )

        self.lat = lat
        self.lon = lon
        self.method = method

    async def _async_update_data(self):
        try:
            _LOGGER.warning("Updating Zmanim data...")

            data = calculate_zmanim(self.lat, self.lon, self.method)

            _LOGGER.warning("Zmanim data result: %s", data)

            # 🔥 BELANGRIJK: nooit None teruggeven
            if not data:
                return {
                    "alot_hashachar": None,
                    "netz": None,
                    "chatzot": None,
                    "shkia": None,
                    "tzeit": None,
                }

            return data

        except Exception as e:
            _LOGGER.exception("Zmanim calculation failed: %s", e)

            return {
                "alot_hashachar": None,
                "netz": None,
                "chatzot": None,
                "shkia": None,
                "tzeit": None,
            }
