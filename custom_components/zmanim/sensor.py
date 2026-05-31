from homeassistant.helpers.entity import Entity
from .const import DOMAIN

async def async_setup_platform(hass, config, add_entities, discovery_info=None):
    add_entities([MySensor()])

class MySensor(Entity):

    @property
    def name(self):
        return "My Integration Status"

    @property
    def state(self):
        return "running"

    @property
    def unique_id(self):
        return "my_integration_status"
