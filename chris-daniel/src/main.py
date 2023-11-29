from argparse import ArgumentParser
from requests import post
from time import sleep

from sensirion_driver_adapters.i2c_adapter.i2c_channel import (
  I2cChannel as Channel
)
from sensirion_i2c_sht4x.device import (
  Sht4xDevice as Device
)
from sensirion_i2c_driver import (
  I2cConnection as Connection,
  CrcCalculator as Crc
)
from sensirion_shdlc_driver import (
  ShdlcSerialPort as Port,
  ShdlcConnection as DriverConnection
)
from sensirion_shdlc_sensorbridge import (
  SensorBridgePort as BridgePort,
  SensorBridgeShdlcDevice as Bridge,
  SensorBridgeI2cProxy as BridgeProxy
)

parser = ArgumentParser()
parser.add_argument('--port', '-p', default='/dev/cu.usbserial-EKS261R9AF')
parser.add_argument('--url', '-u')
driver_port = parser.parse_args().port
url = parser.parse_args().url
port = BridgePort.ONE
crc = Crc(8, 49, 255, 0)

with Port(port=driver_port, baudrate=460800) as driver_port:
  bridge = Bridge(DriverConnection(driver_port), slave_address=0)

  bridge.set_i2c_frequency(port, frequency=100e3)
  bridge.set_supply_voltage(port, voltage=3.3)
  bridge.switch_supply_on(port)

  connection = Connection(BridgeProxy(bridge, port=port))
  sensor = Device(Channel(connection, slave_address=68, crc=crc))
  sensor.soft_reset()

  while True:
    t, rh = map(lambda v: v.value, sensor.measure_lowest_precision())
    json = { 'temperature': t, 'humidity': rh }

    post(url, json=json)
    sleep(1)
