# Heatmiser Hot Water compentent for  Home Assistant 

Home Assistant Intergration to expose the Water Heating Component from a Heatmiser Thermostat PRT-HW.

This uses the Heatmiser_WiFi libuary and is designed to complement the Heatmiser_WiFi_HA intergration.
All based on the Midstar original intergration and Libuary. ( https://github.com/midstar )

Copy files to /config/custom_components/heatmiser_hw/ directory on you Home Assistant Server
Note currently no Icon for the intergration.

Clone at [tcruiser60/heatmiser_HW](https://github.com/tcruiser60/Heatmiser_HW) .

## Overview
A [Heatmiser](http://www.heatmiser.com/) WiFi Thermostat Hot Water Home Assistant plugin.

Supports:
Note - PRT-HW only have on/off for water heating no temperature control, they also 
support Away mode.   

* Turning Hot Water On or Off
* Setting Away Mode On or Off, Note this will affect heating mode as well.
  


Supported Heatmiser Thermostats are WiFi versions of  PRT-HW.

Note that non-WiFi thermostat versions (i.e. using RS-485 serial bus) 
connected through an Heatmiser Ethernet HUB are supported by the
[Home Assistant Heatmiser Core component](https://www.home-assistant.io/integrations/heatmiser/)

## Installation

Copy the heatmiser_hw directory and its contents to the 
Home Assistant /comfig/custom_components directory.
Note currently no Icon for the intergration.

## Configuration
Add following configuration to Home Assistant configuration.yaml

    water_heater:
    - platform: heatmiser_hw
      host: xxx.xxx.xxx.xxx  # IP address of PRTHW 
      port: 8068  # default port 
      pin: 1234  # default pin change as required 
      friendly_name: 'HotWater'  # change as required 

  
## See also
* [Heatmiser Wifi](https://github.com/midstar/heatmiser_wifi) the library used for communication with Heatmiser WiFi devices.
* [iainbullock/heatmiser_wifi_ha](https://github.com/iainbullock/heatmiser_wifi_ha) 
* [Home Assistant Heatmiser Core component](https://www.home-assistant.io/integrations/heatmiser/) for non WiFi versions of Heatmister Thermostats.
 
### Author and license
This component is written by Tim Moore and is licensed under the MIT License.

  


