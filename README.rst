========================================
Bootstrap carousel plugin for Django CMS
========================================

This plugin lets you easily add *carousel* components (ie. slideshows)
into django-cms pages using `Bootstrap
<http://twitter.github.com/bootstrap/>`_.

Requirements
============

* `Django CMS >= 2.2 <http://django-cms.org>`_
* `Bootstrap <http://twitter.github.com/bootstrap/>`_
* `easy-thumbnails <https://github.com/SmileyChris/easy-thumbnails>`_

Installation
============

To use it into your project, just follow this procedure:

#. Open the *settings.py* file and add ``cmsplugin_bootstrap_carousel`` to the
   ``INSTALLED_APPS`` variable

#. Run the following command::

    $ ./manage.py syncdb


.. note::

    Bootstrap is not included with this plugin.
