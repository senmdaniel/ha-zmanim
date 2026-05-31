from homeassistant.components.sensor import SensorEntity


async def async_setup_platform(
    hass,
    config,
    async_add_entities,
    discovery_info=None,
):
    async_add_entities([HelloWorldSensor()])


class HelloWorldSensor(SensorEntity):

    @property
    def name(self):
        return "Zmanim Hello"

    @property
    def unique_id(self):
        return "zmanim_hello"

    @property
    def native_value(self):
        return "Hello World"
