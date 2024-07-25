"""
Example for a BLE 4.0 Server
"""
import sys
import logging
import asyncio
import threading

from typing import Any, Union

from bless import (  # type: ignore
    BlessServer,
    BlessGATTCharacteristic,
    GATTCharacteristicProperties,
    GATTAttributePermissions,
)

SERVICE_UUID = 'A07498CA-AD5B-474E-940D-16F1FBE7E8CD'
COMMAND_CHAR_UUID = '12345678-1234-5678-1234-56789abcdef1'
RESPONSE_CHAR_UUID = '12345678-1234-5678-1234-56789abcdef2'

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(name=__name__)

# NOTE: Some systems require different synchronization methods.
trigger: Union[asyncio.Event, threading.Event]
if sys.platform in ["darwin", "win32"]:
    trigger = threading.Event()
else:
    trigger = asyncio.Event()


def read_request(characteristic: BlessGATTCharacteristic, **kwargs) -> bytearray:
    logger.debug(f"Reading {characteristic.value}")
    return characteristic.value


def write_request(characteristic: BlessGATTCharacteristic, value: Any, **kwargs):
    characteristic.value = value
    logger.debug(f"Char value set to {characteristic.value}")
    if characteristic.value == b"\x0f":
        logger.debug("NICE")
        trigger.set()


async def run(loop):
    trigger.clear()
    # Instantiate the server
    my_service_name = "Test Service"
    server = BlessServer(name=my_service_name, loop=loop)
    server.read_request_func = read_request
    server.write_request_func = write_request

    # Add Service
    await server.add_new_service(SERVICE_UUID)

    # Add a Characteristic to the service
    commandCharacteristicUuid = "12345678-1234-5678-1234-56789abcdef1"
    char_flags = (
        GATTCharacteristicProperties.read
        | GATTCharacteristicProperties.write
        | GATTCharacteristicProperties.indicate
    )
    permissions = GATTAttributePermissions.readable | GATTAttributePermissions.writeable
    await server.add_new_characteristic(
        SERVICE_UUID, commandCharacteristicUuid, char_flags, None, permissions
    )

    logger.debug(server.get_characteristic(commandCharacteristicUuid))
    await server.start()
    logger.debug("Advertising")
    logger.info(f"Write '0xF' to the advertised characteristic: {commandCharacteristicUuid}")
    if trigger.__module__ == "threading":
        trigger.wait()
    else:
        await trigger.wait()

    await asyncio.sleep(2)
    logger.debug("Updating")
    server.get_characteristic(commandCharacteristicUuid)
    server.update_value(SERVICE_UUID, commandCharacteristicUuid)
    await asyncio.sleep(5)
    await server.stop()


loop = asyncio.get_event_loop()
loop.run_until_complete(run(loop))