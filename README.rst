========================================
Bootstrap carousel plugin for Django-CMS
========================================

.. image:: https://travis-ci.org/nimbis/cmsplugin-bootstrap-carousel.svg?branch=master
    :target: https://travis-ci.org/nimbis/cmsplugin-bootstrap-carousel

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

#. add::

    THUMBNAIL_HIGH_RESOLUTION = True
    
to settings.py, if you want to support retina displays in the admin. (Otherwise 
you may encounter missing image placeholders in image file listings.)

#. Run the following command::

    $ ./manage.py syncdb


.. note::

    Bootstrap is not included with this plugin.
