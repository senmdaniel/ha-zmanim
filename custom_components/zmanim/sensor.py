from homeassistant.helpers.entity import Entity
from .zmanim import get_zman_times

async def async_setup_platform(hass, config, add_entities, discovery_info=None):
    add_entities([ZmanimSensor()])

class ZmanimSensor(Entity):

    def __init__(self):
        self._state = None

    @property
    def name(self):
        return "Zmanim Test"

    @property
    def unique_id(self):
        return "zmanim_test"

    @property
    def state(self):
        return self._state

    async def async_update(self):
        data = get_zman_times("Amsterdam")
        self._state = data["sunrise"]
