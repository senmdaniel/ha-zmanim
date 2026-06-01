from datetime import date
from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .core.zmanim_engine import calculate_zmanim

DOMAIN = "zmanim"


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
):
    async_add_entities([ZmanimSensor(entry.entry_id)])


class ZmanimSensor(SensorEntity):
    def __init__(self, entry_id: str):
        self._entry_id = entry_id
        self._attr_name = "Zmanim Test"
        self._attr_unique_id = f"zmanim_{entry_id}"

    @property
    def native_value(self):
        config = {
            "city": "Antwerp",
            "timezone": "Europe/Brussels",
            "latitude": 51.2194,
            "longitude": 4.4025,
        }

        data = calculate_zmanim(config, date.today())
        return data["zmanim"]["shkia"]["time"]

    @property
    def extra_state_attributes(self):
        config = {
            "city": "Antwerp",
            "timezone": "Europe/Brussels",
            "latitude": 51.2194,
            "longitude": 4.4025,
        }

        return calculate_zmanim(config, date.today())
