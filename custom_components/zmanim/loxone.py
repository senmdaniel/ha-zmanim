import json
import logging
import aiohttp

_LOGGER = logging.getLogger(__name__)

class LoxoneExporter:
    def __init__(self, url: str):
        self.url = url

    async def send(self, data: dict):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    self.url,
                    json=data,
                    timeout=10
                ) as resp:
                    _LOGGER.info("Loxone response: %s", resp.status)
        except Exception as e:
            _LOGGER.error("Loxone export failed: %s", e)
