from homeassistant.components.sensor import SensorEntity


def setup_platform(hass, config, add_entities, discovery_info=None):
    add_entities([ZmanimSensor(hass)])


class ZmanimSensor(SensorEntity):

    def __init__(self, hass):
        self.hass = hass
        self._attr_name = "Zmanim"
        self._attr_unique_id = "zmanim_main"

    @property
    def native_value(self):
        data = self.hass.data.get("zmanim", {})
        return data.get("zmanim", {}).get("shkia", {}).get("time", "unknown")

    @property
    def extra_state_attributes(self):
        return self.hass.data.get("zmanim", {}).get("zmanim", {})
