from homeassistant.core import HomeAssistant

async def async_setup(hass: HomeAssistant, config: dict):
    hass.states.async_set("test_sensor.hello", "working")
    return True
