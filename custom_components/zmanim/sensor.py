from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

DOMAIN = "zmanim"


async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities([ZmanimSensor()])


class ZmanimSensor(SensorEntity):
    _attr_name = "Zmanim Test"
    _attr_unique_id = "zmanim_test"

    @property
    def native_value(self):
        return "OK"
