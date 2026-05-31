from homeassistant.helpers.entity import Entity
from .zmanim import get_zman_times

DOMAIN = "zmanim"

async def async_setup_platform(hass, config, add_entities, discovery_info=None):
    add_entities([ZmanimSensor()])

class ZmanimSensor(Entity):

    def __init__(self):
        self._state = None

    @property
    def name(self):
        return "Zmanim Today"

    @property
    def unique_id(self):
        return "zmanim_today"

    @property
    def state(self):
        return self._state or "unknown"

    async def async_update(self):
        times = get_zman_times()
        self._state = times.get("sunrise", "unknown")
