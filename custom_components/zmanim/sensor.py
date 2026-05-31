from homeassistant.components.sensor import SensorEntity
from datetime import date
from .app.core.zmanim import calculate_zmanim


async def async_setup_entry(hass, config_entry, async_add_entities):
    async_add_entities([ZmanimSensor()])


class ZmanimSensor(SensorEntity):

    def __init__(self):
        self._attr_name = "Zmanim"
        self._attr_unique_id = "zmanim_main"

        result = calculate_zmanim({}, date.today())

        self._attr_native_value = result["zmanim"]["shkia"]["time"]
        self._attr_extra_state_attributes = result["zmanim"]
