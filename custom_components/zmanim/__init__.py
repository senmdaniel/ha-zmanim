import logging
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, entry):
    _LOGGER.error("ZMANIM INIT START")

    hass.data.setdefault(DOMAIN, {})

    try:
        lat = entry.data.get("latitude")
        lon = entry.data.get("longitude")
        method = entry.data.get("method", "gra")

        _LOGGER.error("CONFIG: %s %s %s", lat, lon, method)

        from .coordinator import ZmanimCoordinator

        coordinator = ZmanimCoordinator(hass, entry.data)
        await coordinator.async_config_entry_first_refresh()

        hass.data[DOMAIN][entry.entry_id] = coordinator

        await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])

        _LOGGER.error("ZMANIM INIT OK")

        return True

    except Exception as e:
        _LOGGER.exception("ZMANIM INIT FAILED: %s", e)
        return False
