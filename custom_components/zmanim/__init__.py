from homeassistant.core import HomeAssistant
from .const import DOMAIN

DOMAIN = "zmanim"

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN]["loaded"] = True
    return True
