import logging
from homeassistant.helpers.entity import CoordinatorEntity
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, entry, async_add_entities):
    """Set up the Zmanim sensor."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([ZmanimSensor(coordinator, entry)], True)

class ZmanimSensor(CoordinatorEntity):
    """Sensor voor Zmanim JSON data."""

    def __init__(self, coordinator, entry):
        super().__init__(coordinator)
        self._entry = entry
        self._attr_name = "Zmanim"

    @property
    def state(self):
        if not self.coordinator.data:
            return "unknown"

        import json
        return json.dumps(self.coordinator.data)
