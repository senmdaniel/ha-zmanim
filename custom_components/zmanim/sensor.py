from homeassistant.components.sensor import SensorEntity

async def async_setup_platform(
    hass,
    config,
    async_add_entities,
    discovery_info=None,
):
    async_add_entities([ZmanimSensor()])


class ZmanimSensor(SensorEntity):
    _attr_name = "Zmanim Test"
    _attr_unique_id = "zmanim_test"

    @property
    def native_value(self):
        return "TEST-06:00"
