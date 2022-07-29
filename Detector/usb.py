import usb.core
import usb.backend.libusb1

VENDOR_ID = 0x0451
PRODUCT_ID = 0xE008

device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)

if device is None:
    raise ValueError('ADU Device not found. Please ensure it is connected to the tablet.')
    sys.exit(1)

# Claim interface 0 - this interface provides IN and OUT endpoints to write to and read from
usb.util.claim_interface(device, 0)