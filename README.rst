========================================
Bootstrap carousel plugin for Django CMS
========================================

.. image:: https://travis-ci.org/nimbis/cmsplugin-bootstrap-carousel.svg?branch=master
    :target: https://travis-ci.org/nimbis/cmsplugin-bootstrap-carousel

A Django-CMS plugin to easily create carousel components using Bootstrap, from Twitter.
Forked from: https://bitbucket.org/tonioo/cmsplugin-bootstrap-carousel


Requirements
============

* `Django CMS >= 2.4 <http://django-cms.org>`_
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
