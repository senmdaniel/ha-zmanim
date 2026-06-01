import voluptuous as vol
from homeassistant import config_entries

from .const import DOMAIN


class ZmanimConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Zmanim."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(
                title="Zmanim",
                data=user_input or {},
            )

        schema = vol.Schema({})

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
        )
