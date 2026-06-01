from datetime import date
from homeassistant.components.sensor import SensorEntity

from .core.zmanim_engine import calculate_zmanim


DEFAULT_CONFIG = {
    "city": "Antwerp",
    "timezone": "Europe/Brussels",
    "latitude": 51.2194,
    "longitude": 4.4025,
}


async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities([ZmanimSensor()])


class ZmanimSensor(SensorEntity):
    _attr_name = "Zmanim"
    _attr_unique_id = "zmanim_engine"

    @property
    def native_value(self):
        data = calculate_zmanim(DEFAULT_CONFIG, date.today())

        # simpele “main value”
        return data["zmanim"]["shkia"]["time"]

    @property
    def extra_state_attributes(self):
        return calculate_zmanim(DEFAULT_CONFIG, date.today())
