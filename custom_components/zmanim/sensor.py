from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
):
    async_add_entities([ZmanimSensor()])


class ZmanimSensor(SensorEntity):
    _attr_name = "Zmanim Test"
    _attr_unique_id = "zmanim_test"

    @property
    def native_value(self):
        return "TEST-06:00"
