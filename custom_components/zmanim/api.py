import logging
from aiohttp import web
from homeassistant.components.http import HomeAssistantView

DOMAIN = "zmanim"

_LOGGER = logging.getLogger(__name__)


class ZmanimView(HomeAssistantView):
    url = "/api/zmanim"
    name = "api:zmanim"
    requires_auth = False

    async def get(self, request):
        hass = request.app["hass"]

        try:
            # neem eerste coordinator (simpel model)
            coordinator = next(iter(hass.data[DOMAIN].values()))
            data = coordinator.data or {}

            return web.json_response(data)

        except Exception as e:
            _LOGGER.exception("Zmanim API error: %s", e)
            return web.json_response(
                {"status": "error", "message": str(e)},
                status=500,
            )
