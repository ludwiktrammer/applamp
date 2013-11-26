from .abstract import AbstractLight


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

    def full_brightness(self, group=0):
        """Sets brightness to 100%."""
        self._choose_group([181, 184, 189, 183, 178], group)

    def bright_up(self, group=0):
        """Makes the light brighter."""
        self.on(group)
        self.send_command(60)

    def bright_down(self, group=0):
        """Makes the light less bright."""
        self.on(group)
        self.send_command(52)

    def warmer(self, group=0):
        """Makes the light warmer."""
        self.on(group)
        self.send_command(62)

    def cooler(self, group=0):
        """Makes the light less warm."""
        self.on(group)
        self.send_command(63)

    def fade_out(self, duration=3, group=0):
        """Turns off the light by gradually fading it out.
        The optional `duration` parameter allows for control
        of the fade out duration (in seconds)"""
        self.on(group)
        super(WhiteLight, self).fade_out(duration, group=group)
        self.off(group)

    def fade_in(self, duration=3, group=0):
        """Turns on the light by gradually fading it in.
        The optional `duration` parameter allows for control
        of the fade in duration (in seconds)"""
        self.on(group)
        super(WhiteLight, self).fade_in(duration, group=group)
