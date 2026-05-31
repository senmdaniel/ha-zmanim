from homeassistant.core import HomeAssistant
from .const import DOMAIN

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up integration via YAML (fallback mode)."""
    
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN]["status"] = "loaded"

    return True
