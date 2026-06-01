from homeassistant.core import HomeAssistant
from .const import DOMAIN
from .coordinator import ZmanimCoordinator

async def async_setup_entry(hass: HomeAssistant, entry):
    hass.data.setdefault(DOMAIN, {})

    lat = entry.data["latitude"]
    lon = entry.data["longitude"]
    method = entry.data.get("method", "gra")

    coordinator = ZmanimCoordinator(hass, lat, lon, method)
    await coordinator.async_config_entry_first_refresh()

    hass.data[DOMAIN][entry.entry_id] = coordinator

    hass.config_entries.async_setup_platforms(entry, ["sensor"])
    return True
