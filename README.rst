========================
opsdroid ZODB extension
========================

**Note: this extension requires an opsdroid release that has support for entry point - facilitated
packaged extensions. Currently there are no such releases yet; use opsdroid github master checkout
until then.**

This extension provides ZODB support for opsdroid. To use, just add 'zodb' to
the databases section of your opsdroid config, and optionally give a path
to the database file, if you wish not to use the default which is 'opsdroid.fs'
stored in current directory.

* Free software: Apache Software License 2.0


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
