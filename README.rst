AppLamp Python API
==================

`AppLamp Python API <https://github.com/ludwiktrammer/applamp>`_ is a library for controlling `AppLight <http://www.wifiledlamp.com/service/about/>`_ lighting from your Python code.

Examples
--------
Controlling white light bulbs:

.. code:: python

    from applight import WhiteLight

    light = WhiteLight()
    light.on()
    light.warmer()
    light.fade_out()
    light.night_mode(group=2)


Controlling RGB light bulbs:

.. code:: python

    from applight import ColorLight
    
    light = ColorLight()
    light.fade_in()
    light.hue(100)  # changing color
    light.next_effect()
    light.off()
