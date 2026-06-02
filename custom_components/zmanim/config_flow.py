import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN, DEFAULT_METHOD

class ZmanimConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Zmanim config flow."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle user step."""

        if user_input is not None:
            return self.async_create_entry(
                title="Zmanim",
                data={
                    "latitude": float(user_input["latitude"]),
                    "longitude": float(user_input["longitude"]),
                    "method": user_input.get("method", DEFAULT_METHOD),
                },
            )

        schema = vol.Schema({
            vol.Required("latitude"): vol.Coerce(float),
            vol.Required("longitude"): vol.Coerce(float),
            vol.Optional("method", default=DEFAULT_METHOD): str,
        })

        return self.async_show_form(step_id="user", data_schema=schema)
