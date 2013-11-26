AppLamp Python API
==================

`AppLamp Python API <https://github.com/ludwiktrammer/applamp>`_ is a library for controlling `AppLamp <http://www.wifiledlamp.com>`_ lighting from your Python code.

Installation
------------
* Install using `pip <http://www.pip-installer.org/>`_::

    sudo pip install applamp

* Or download the repository and install with `setup.py`::

    sudo python setup.py install

Examples & Documentation
--------
Controlling white light bulbs:

.. code:: python

    from applight import WhiteLight

    light = WhiteLight()
    light.on()
    light.warmer()
    light.fade_out()
    light.night_mode(group=1)


Controlling RGB light bulbs:

.. code:: python

    from applight import RgbLight

    light = RgbLight()
    light.fade_in()
    light.hue(100)  # changing color
    light.next_effect()


You can see a list of all methods and their descriptions in
`the reference documentation <http://applamp-python-api.readthedocs.org/>`_.

Disclaimer
----------
I'm not affiliated with `AppLamp <http://www.wifiledlamp.com/service/about/>`_ in any way. This project is not endorsed, supported or funded by the company. They are probably really cool guys, but I don't know them. "AppLamp" is most likely a registered trademark belonging to the company.
