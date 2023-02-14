from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.components.button import (PLATFORM_SCHEMA, ButtonEntity)

from homeassistant.const import CONF_NAME, CONF_IP_ADDRESS

import homeassistant.helpers.config_validation as cv

import logging

import voluptuous as vol

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME): cv.string,
    vol.Required(CONF_IP_ADDRESS): cv.string,
})

def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None:

    name = config[CONF_NAME]
    ip = config[CONF_IP_ADDRESS]
    
    add_entities([ExampleButtonEntity(name, ip)])

class ExampleButtonEntity(ButtonEntity):

    def __init__(self, name, ip) -> None:
        self._name = name
        self.ip = ip

    @property
    def name(self) -> str:
        """Return the display name of this light."""
        return self._name

    async def async_press(self) -> None:
        """Handle the button press."""
        _LOGGER.warning("Example button was pressed!")