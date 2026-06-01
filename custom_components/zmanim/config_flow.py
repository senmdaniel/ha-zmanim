import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN, DEFAULT_METHOD


class ZmanimConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(
                title="Zmanim",
                data=user_input,
            )

        schema = vol.Schema({
            vol.Required("latitude"): float,
            vol.Required("longitude"): float,
            vol.Optional("method", default=DEFAULT_METHOD): str,
        })

        return self.async_show_form(step_id="user", data_schema=schema)
