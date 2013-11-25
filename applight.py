import socket
import time


class AbstractLight(object):
    def __init__(self, ip='192.168.1.100', port=50000):
        self.address = (ip, port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_command(self, code, value=0):
        data = bytearray([code, value, 85])
        self.socket.sendto(data, self.address)

    def fade_out(self, duration=3):
        step_duration = duration / 11.0
        for i in range(10):
            self.bright_down()
            time.sleep(step_duration)

    def fade_in(self, duration=3):
        step_duration = duration / 11.0
        for i in range(10):
            time.sleep(step_duration)
            self.bright_up()


class WhiteLight(AbstractLight):
    def _choose_group(self, options, group):
        try:
            self.send_command(options[group])
        except KeyError:
            raise ValueError(
                "Group must be a value between 0 and %d" % len(options) - 1
            )

    def on(self, group=0):
        self._choose_group([53, 56, 61, 55, 50], group)

    def off(self, group=0):
        self._choose_group([57, 59, 51, 58, 54], group)

    def night_mode(self, group=0):
        self._choose_group([185, 187, 179, 186, 182], group)

    def bright_up(self):
        self.send_command(60)

    def bright_down(self):
        self.send_command(52)

    def warmer(self):
        self.send_command(62)

    def cooler(self):
        self.send_command(63)

    def fade_out(self, duration=3, group=0):
        self.on(group)
        super(WhiteLight, self).fade_out(duration)
        self.off(group)

    def fade_in(self, duration=3, group=0):
        self.on(group)
        super(WhiteLight, self).fade_in(duration)


class ColorLight(AbstractLight):
    def hue(self, value):
        if not (0 <= value <= 255):
            raise ValueError("Hue must be a value between 0 and 255.")
        self.send_command(32, value)

    def off(self):
        self.send_command(33)

    def on(self):
        self.send_command(34)

    def bright_up(self):
        self.send_command(35)

    def bright_down(self):
        self.send_command(36)

    def next_effect(self):
        self.send_command(39)

    def previous_effect(self):
        self.send_command(40)

    def faster_effect(self):
        self.send_command(37)

    def slower_effect(self):
        self.send_command(38)

    def fade_out(self, duration=3, group=0):
        super(ColorLight, self).fade_out(duration)
        self.off()

    def fade_in(self, duration=3, group=0):
        self.on()
        super(ColorLight, self).fade_in(duration)
