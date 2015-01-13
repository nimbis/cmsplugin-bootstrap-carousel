========================================
Bootstrap carousel plugin for Django-CMS
========================================

.. image:: https://travis-ci.org/nimbis/cmsplugin-bootstrap-carousel.svg?branch=master
   :target: https://travis-ci.org/nimbis/cmsplugin-bootstrap-carousel

.. image:: https://coveralls.io/repos/nimbis/cmsplugin-bootstrap-carousel/badge.png?branch=master
   :target: https://coveralls.io/r/nimbis/cmsplugin-bootstrap-carousel?branch=master

A Django-CMS plugin to easily create carousel components using Bootstrap, from Twitter.
Forked from: https://bitbucket.org/tonioo/cmsplugin-bootstrap-carousel

This plugin supports filer and will use it if it is found in your INSTALLED_APPS.

Requirements
============

* `Django-CMS >= 2.4 <http://django-cms.org>`_
* `Bootstrap <http://twitter.github.com/bootstrap/>`_
* `easy-thumbnails <https://github.com/SmileyChris/easy-thumbnails>`_
* `Pillow`
* `filer` is optional.


Installation
============

To use it into your project, just follow this procedure:

#. Open the *settings.py* file and add ``cmsplugin_bootstrap_carousel`` to the
   ``INSTALLED_APPS`` variable

#. This plugin will use filer if it is in your INSTALLED_APPS

#. Run the following command::

    $ ./manage.py syncdb


.. note::

    Bootstrap is not included with this plugin.

Contributing
============

Contributors please submit pull requests to the `develop` branch.

History
=======

0.2.2:

    * Fixing setup.py for pip>=1.6.

0.2.1:

    * Changed plugin name from CarouselPlugin to BootstrapCarouselPlugin to avoid name collision
    with djangocms-cascade.

0.2.0:

    * Added fields for toggling visibility of carousel controls and slide indicator. Improved the included template.