from datetime import datetime
from homeassistant.components.sensor import SensorEntity

from .core.hebrew_calendar import get_hebrew_date


async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities([HebrewDateSensor()])


class HebrewDateSensor(SensorEntity):
    _attr_name = "Hebrew Date"
    _attr_unique_id = "hebrew_date"

    @property
    def native_value(self):
        now = datetime.now()

        result = get_hebrew_date(now)

        return f"{result['hebrew_day']}/{result['hebrew_month']}/{result['hebrew_year']}"
