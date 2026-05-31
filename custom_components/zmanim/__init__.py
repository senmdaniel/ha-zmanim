from datetime import date
from .app.core.zmanim import calculate_zmanim

async def async_setup(hass, config):
    hass.data["zmanim"] = calculate_zmanim({}, date.today())
    return True
