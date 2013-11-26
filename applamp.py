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
    """
    Create an object for controlling white AppLamp light bulbs.
    Optional attributes `ip` and `port` allow for a custom AppLamp Wifi Box setup.
    By default those values are `192.168.1.100` and `50000`.

    White AppLamp bulbs have a "group" future, allowing for partitioning of light sources
    into multiple groups. Most methods of this class supports this feature via an optional
    `group` attribute. The default value of `0` means the method will be applied to all
    light sources in all groups. Values between 1 and 4 will be interpreted as group
    identifiers, and the method will be applied only to light sources within a given group.
    """
    def _choose_group(self, options, group):
        try:
            self.send_command(options[group])
        except KeyError:
            raise ValueError(
                "Group must be a value between 0 and %d" % len(options) - 1
            )

    def on(self, group=0):
        """Turns the lights on."""
        self._choose_group([53, 56, 61, 55, 50], group)

    def off(self, group=0):
        """Turns the lights off."""
        self._choose_group([57, 59, 51, 58, 54], group)

    def night_mode(self, group=0):
        """Switches the lights into night mode (very low brightness)."""
        self._choose_group([185, 187, 179, 186, 182], group)

    def bright_up(self):
        """Makes the light brighter."""
        self.send_command(60)

    def bright_down(self):
        """Makes the light less bright."""
        self.send_command(52)

    def warmer(self):
        """Makes the light warmer."""
        self.send_command(62)

    def cooler(self):
        """Makes the light less warm."""
        self.send_command(63)

    def fade_out(self, duration=3, group=0):
        """Turns off the light by gradually fading it out.
        The optional `duration` parameter allows for control
        of the fade out duration (in seconds)"""
        self.on(group)
        super(WhiteLight, self).fade_out(duration)
        self.off(group)

    def fade_in(self, duration=3, group=0):
        """Turns on the light by gradually fading it in.
        The optional `duration` parameter allows for control
        of the fade in duration (in seconds)"""
        self.on(group)
        super(WhiteLight, self).fade_in(duration)


class ColorLight(AbstractLight):
    """
    Create an object for controlling RGB AppLamp light bulbs.
    Optional attributes `ip` and `port` allow for a custom AppLamp Wifi Box setup.
    By default those values are `192.168.1.100` and `50000`.
    """
    def hue(self, value):
        """
        Changes the light color to `value`,
        which must be a hue value (a number between 0 and 255)
        """
        if not (0 <= value <= 255):
            raise ValueError("Hue must be a value between 0 and 255.")
        self.send_command(32, value)

    def off(self):
        """Turns the lights off."""
        self.send_command(33)

    def on(self):
        """Turns the lights on."""
        self.send_command(34)

    def bright_up(self):
        """Makes the light brighter."""
        self.send_command(35)

    def bright_down(self):
        """Makes the light less bright."""
        self.send_command(36)

    def next_effect(self):
        """Switches to a next built-in light effect"""
        self.send_command(39)

    def previous_effect(self):
        """Switches to a previous built-in light effect"""
        self.send_command(40)

    def faster_effect(self):
        """Makes the current built-in light effect faster"""
        self.send_command(37)

    def slower_effect(self):
        """Makes the current built-in light effect slower"""
        self.send_command(38)

    def fade_out(self, duration=3, group=0):
        """Turns off the light by gradually fading it out.
        The optional `duration` parameter allows for control
        of the fade out duration (in seconds)"""
        super(ColorLight, self).fade_out(duration)
        self.off()

    def fade_in(self, duration=3, group=0):
        """Turns on the light by gradually fading it in.
        The optional `duration` parameter allows for control
        of the fade in duration (in seconds)"""
        self.on()
        super(ColorLight, self).fade_in(duration)
