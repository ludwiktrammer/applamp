from .abstract import AbstractLight


class RgbLight(AbstractLight):
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

    def fade_out(self, duration=3):
        """Turns off the light by gradually fading it out.
        The optional `duration` parameter allows for control
        of the fade out duration (in seconds)"""
        super(RgbLight, self).fade_out(duration)
        self.off()

    def fade_in(self, duration=3):
        """Turns on the light by gradually fading it in.
        The optional `duration` parameter allows for control
        of the fade in duration (in seconds)"""
        super(RgbLight, self).fade_in(duration)
