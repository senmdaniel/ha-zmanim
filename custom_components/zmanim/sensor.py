from homeassistant.helpers.entity import Entity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

ZMANIM_KEYS = [
    "alot_hashachar",
    "netz",
    "chatzot",
    "shkia",
    "tzeit",
]

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities([
        ZmanimSensor(coordinator, key)
        for key in ZMANIM_KEYS
    ])


class ZmanimSensor(CoordinatorEntity, Entity):
    def __init__(self, coordinator, key):
        super().__init__(coordinator)
        self._key = key

    @property
    def name(self):
        return f"Zmanim {self._key}"

    @property
    def unique_id(self):
        return f"zmanim_{self._key}"

  @property
def state(self):
    if not self.coordinator.data:
        return None

    value = self.coordinator.data.get(self._key)

    return value.isoformat() if hasattr(value, "isoformat") else value

    @property
    def available(self):
        return bool(self.coordinator.data)
