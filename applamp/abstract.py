import socket
import time


class AbstractLight(object):
    """
    An abstract class with basic methods, not intended to be used directly.
    """
    def __init__(self, ip='192.168.1.100', port=50000):
        self.address = (ip, port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_command(self, code, value=0):
        data = bytearray([code, value, 85])
        self.socket.sendto(data, self.address)
        time.sleep(0.1)  # wait before AppLamp is ready for new commands

    def fade_out(self, duration=3, *args, **kwargs):
        step_duration = duration / 11.0
        for i in range(10):
            self.bright_down(*args, **kwargs)
            time.sleep(step_duration)

    def fade_in(self, duration=3, *args, **kwargs):
        step_duration = duration / 11.0
        for i in range(10):
            time.sleep(step_duration)
            self.bright_up(*args, **kwargs)
