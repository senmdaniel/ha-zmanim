import logging
from .const import DOMAIN
from .api import ZmanimView

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, entry):
    """Set up Zmanim from a config entry."""
    _LOGGER.error("ZMANIM INIT START: %s", entry.data)

    hass.data.setdefault(DOMAIN, {})

    try:
        from .coordinator import ZmanimCoordinator

        coordinator = ZmanimCoordinator(hass, entry.data)
        await coordinator.async_config_entry_first_refresh()

        hass.data[DOMAIN][entry.entry_id] = coordinator

        # API endpoint registreren
        await hass.http.async_register_view(ZmanimView)

        # Sensor platform setup
        await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])

        _LOGGER.error("ZMANIM INIT SUCCESS")
        return True

    except Exception as e:
        _LOGGER.exception("ZMANIM INIT FAILED: %s", e)
        return False
