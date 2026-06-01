from homeassistant.core import HomeAssistant
from .const import DOMAIN

async def async_setup_entry(hass: HomeAssistant, entry):
    hass.data.setdefault(DOMAIN, {})

    lat = entry.data.get("latitude")
    lon = entry.data.get("longitude")
    method = entry.data.get("method", "gra")

    from .coordinator import ZmanimCoordinator

    coordinator = ZmanimCoordinator(hass, lat, lon, method)
    await coordinator.async_config_entry_first_refresh()

    hass.data[DOMAIN][entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])

    return True
