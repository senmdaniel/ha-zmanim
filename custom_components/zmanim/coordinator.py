import aiohttp
import logging

_LOGGER = logging.getLogger(__name__)

class ZmanimCoordinator(...):

    def __init__(self, hass, config):
        ...
        self.loxone_url = config.get("loxone_url")

    async def _send_to_loxone(self, data):
        if not self.loxone_url:
            return

        try:
            async with aiohttp.ClientSession() as session:
                await session.post(
                    self.loxone_url,
                    json=data
                )
        except Exception as e:
            _LOGGER.error("Loxone error: %s", e)
