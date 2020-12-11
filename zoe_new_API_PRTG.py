from pyze.api import Gigya, Kamereon, Vehicle
import json
import sys

from prtg.sensor.result import CustomSensorResult
from prtg.sensor.units import ValueUnit


g = Gigya()
g.set_api_key('3_e8d4g4SE_Fo8ahyHwwP7ohLGZ79HKNN2T8NjQqoNnk6Epj6ilyYwKdHUyCw3wuxz')
g.login('email', 'password')
g.account_info()
k = Kamereon(gigya=g)
k.set_api_key('oF09WnKqvBDcrQzcW1rJNpjIuy7KdGaB')
v = Vehicle('VIN', k) 

data=v.battery_status()
data_hvac=v.hvac_status()

sensor = CustomSensorResult()
sensor.add_channel(name='Battery Percentage',unit='Percent',value=data['batteryLevel'])
sensor.add_channel(name='Range',unit='KM',value=data['batteryAutonomy'])
sensor.add_channel(name='External Temperature',unit='Temperature',value=data_hvac['externalTemperature'])
sensor.add_channel(name='Plugged In',value=data['plugStatus'])
sensor.add_channel(name='Charging Status',value=data['chargingStatus'])

print(sensor.json_result)
