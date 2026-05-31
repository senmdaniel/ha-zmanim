import logging
from datetime import date
from .app.core.zmanim import calculate_zmanim

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass, config):
    _LOGGER.warning("ZMANIM INIT LOADED")

    hass.data["zmanim"] = calculate_zmanim({}, date.today())

    return True
