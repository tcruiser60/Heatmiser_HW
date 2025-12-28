"""Heatmiser HW Platform for Home Assistant."""

from datetime import datetime
import logging
from typing import Any

from heatmiser_wifi import Heatmiser
import voluptuous as vol
import homeassistant.helpers.config_validation as cv

from homeassistant.components.water_heater import (
    STATE_GAS,
    STATE_OFF,
    WaterHeaterEntity,
    WaterHeaterEntityFeature,
    PLATFORM_SCHEMA,
)

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import UnitOfTemperature
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback


_LOGGER = logging.getLogger(__name__)

# entries from config file
from homeassistant.const import (
    CONF_HOST,
    CONF_PORT,
    CONF_PIN,
    #CONF_MAC,
    ATTR_FRIENDLY_NAME
    )

# Validation of the user's configuration
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_HOST): cv.string,
    vol.Optional(CONF_PORT, default=8068): cv.port,
    vol.Optional(CONF_PIN, default=0): cv.positive_int,
    #vol.Optional(CONF_MAC, default='00:1E:C0:00:4C:00'):cv.mac,
    vol.Optional(ATTR_FRIENDLY_NAME, default='_not_set_'): cv.string

})

def setup_platform(hass, config, add_entities, discovery_info=None):
    # Assign configuration variables.
    # The configuration check takes care they are present.
    host = config[CONF_HOST]
    port = config[CONF_PORT]
    pin = config[CONF_PIN]
    name = config[ATTR_FRIENDLY_NAME]

# Add devices
    add_entities([HeatmiserHW(host, port, pin, name)], True)
    _LOGGER.debug("Entity added! ", name)
    
class HeatmiserHW(WaterHeaterEntity):

    def __init__(self, host, port, pin, name):
        self._heatmiser = Heatmiser(host,port,pin)
        self._heatmiser_info = []
        self._name = name

        self._attr_temperature_unit = UnitOfTemperature.CELSIUS
        #self._attr_available = False
        self._attr_target_temperature = False
        self._attr_min_temp = False
        self._attr_max_temp = False
        
    @property
    def name(self):
        if self._name == '_not_set_':
            self._name = 'Heatmiser ' + self._heatmiser_info['model']
        return self._name
    
    @property
    def operation_list(self) -> list[str]:
        """Return the list of supported operation modes."""
        ha_modes = [
        STATE_OFF,
        STATE_GAS,
        ]
        return ha_modes
        
    @property
    def supported_features(self) -> WaterHeaterEntityFeature:
        """Return the list of supported features."""
        support_flags = WaterHeaterEntityFeature.OPERATION_MODE

        support_flags |= WaterHeaterEntityFeature.AWAY_MODE

        return support_flags
        
    @property
    def current_operation(self) -> str:
        """Return the current operation mode."""
        current_heat_mode = self._heatmiser_info['hot_water_state']
        if current_heat_mode == 'On':
            return STATE_GAS
        else:
            return STATE_OFF
            
    @property
    def is_away_mode_on(self):
        """Return True if away mode is on."""
        current_away_mode = self._heatmiser_info['away_mode']
        if current_away_mode == 'On':
            return True
        else:
            return False
    
    
    # ------------------- Set Working States --------------------------------------
            
    def set_operation_mode(self, operation_mode):
        """Set new target operation mode."""
        _LOGGER.debug("Hot Water State Changed", operation_mode)
        if operation_mode not in self.operation_list:
            raise HomeAssistantError("Operation mode not supported")

        if operation_mode == 'off':
            hot_water_state = 'Off'
            _LOGGER.debug("Setting STATE_OFF")
        elif operation_mode == 'gas':
            hot_water_state = 'On'
            _LOGGER.debug("Setting STATE_ON")
        self._heatmiser.connect()
        self._heatmiser.set_value('hot_water_state', hot_water_state)
        _LOGGER.debug("Hot Water State Changed")
        self._heatmiser_info = self._heatmiser.get_info() 
        self._heatmiser.disconnect()
        
    def turn_away_mode_on(self):
        """Turn away mode on."""
        _LOGGER.debug("Setting away mode on")
        away_mode = 'On'
        self._heatmiser.connect()
        self._heatmiser.set_value('away_mode', away_mode)
        self._heatmiser_info = self._heatmiser.get_info()
        self._heatmiser.disconnect()

    def turn_away_mode_off(self):
        """Turn away mode on."""
        _LOGGER.debug("Setting away mode off")
        away_mode = 'Off'
        self._heatmiser.connect()
        self._heatmiser.set_value('away_mode', away_mode)
        self._heatmiser_info = self._heatmiser.get_info()
        self._heatmiser.disconnect()
        
    def update(self):
        self._heatmiser.connect()
        self._heatmiser_info = self._heatmiser.get_info()
        _LOGGER.debug("Device update ")
        self._heatmiser.disconnect()

        
        