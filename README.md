Home Assistant Intergration to expose the Water Heating Component from a Heatmiser Thermostat PRT-HW.

This uses the Heatmiser_WiFi libuary and is to complement the Heatmiser_WiFi_HA componet.
All based on the Midstar original intergration and Libuary. ( https://github.com/midstar )

copy files to /config/custom_componets/heatmiser_hw/ directory on you Home Assistant Server
Note currently no Icon for the intergration.

Yaml configeuration is as follows - 
Add to configuration.yaml

water_heater: 
    - platform: heatmiser_hw
      host: xxx.xxx.xxx.xxx # IP address of PRTHW 
      port: 8068 # default port
      pin: 1234  # default pin change as required
      friendly_name: 'HotWater'
    # type: gas PRTHW

Note - PRT-HW only have on/off for water heating no temperature control, they also 
support Away mode.   
