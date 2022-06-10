from adafruit_hid.keycode import Keycode as kc
from adafruit_hid.consumer_control_code import ConsumerControlCode as cc


STRING = 1
KEY = 2
CONTROL_CODE = 3

keys = [
    # ROW 3, COLUMN 1
    (KEY, [kc.CONTROL, kc.ALT, kc.V]),
    # ROW 3, COLUMN 2
    (KEY, [kc.CONTROL, kc.ALT, kc.C]),
    # ROW 3, COLUMN 3
    (KEY, [kc.CONTROL, kc.ALT, kc.X]),
    # ROW 3, COLUMN 4
    (KEY, [kc.CONTROL, kc.ALT, kc.Y]),
    # ROW 2, COLUMN 1
    (KEY, [kc.CONTROL, kc.ALT, kc.F]),
    # ROW 2, COLUMN 2
    (KEY, [kc.CONTROL, kc.ALT, kc.D]),
    # ROW 2, COLUMN 3
    (KEY, [kc.CONTROL, kc.ALT, kc.S]),
    # ROW 2, COLUMN 4
    (KEY, [kc.CONTROL, kc.ALT, kc.A]),
    # ROW 1, COLUMN 1
    (KEY, [kc.CONTROL, kc.ALT, kc.R]),
    # ROW 1, COLUMN 2
    (KEY, [kc.CONTROL, kc.ALT, kc.E]),
    # ROW 1, COLUMN 3
    (KEY, [kc.CONTROL, kc.ALT, kc.W]),
    # ROW 1, COLUMN 4
    (KEY, [kc.CONTROL, kc.ALT, kc.Q]),
]

