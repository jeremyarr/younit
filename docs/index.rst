.. image:: https://cdn.rawgit.com/jeremyarr/younit/2275cf7a/docs/_static/logo_full.png
    :target: https://github.com/jeremyarr/younit

welcome to younit
===================

.. image:: http://tactile.com.au/jenkins/buildStatus/icon?job=younit1
    :target: https://github.com/jeremyarr/younit

.. image:: https://img.shields.io/pypi/l/younit.svg
    :target: https://pypi.python.org/pypi/younit

.. image:: https://tactile.com.au/badge-server/coverage/younit1
    :target: https://github.com/jeremyarr/younit

.. image:: https://img.shields.io/pypi/pyversions/younit.svg
    :target: https://pypi.python.org/pypi/younit

.. image::  https://img.shields.io/pypi/status/younit.svg
    :target: https://pypi.python.org/pypi/younit

.. image:: https://img.shields.io/pypi/implementation/younit.svg
    :target: https://pypi.python.org/pypi/younit


`younit <https://github.com/jeremyarr/younit>`_ is a collection of helpers for the :mod:`unittest` module.

Helpers
---------

==========================================  =======================================================
I want to                                   Helpers to Use
==========================================  =======================================================
Test coroutines                             :func:`@asyncio_test <younit.asyncio_test>`
Mock out coroutines                         :func:`~younit.AsyncMock`, 
                                            :func:`@asyncio_test <younit.asyncio_test>`
Print the name of a test before running it  :func:`@test_name <younit.test_name>`
Fail a test if it hangs                     :func:`@set_test_hang_alarm <younit.set_test_hang_alarm>`, 
                                            :func:`@clear_test_hang_alarm <younit.clear_test_hang_alarm>`
Close all threads associated with a test    :func:`@close_all_threads <younit.close_all_threads>`
==========================================  =======================================================

Get It Now
-----------

.. code-block:: bash

    $ pip install younit

Examples
--------------

Testing and mocking coroutines::

    class MyTestCase(unittest.TestCase):
        async def async_setUp(self):
            pass

        async def async_tearDown(self):
            pass

        @asyncio_test
        async def test_this(self):
            x = AsyncMock()
            await x()
            x.mock.assert_called_once()


Setting up test hang alarms::

    class MyTestCase(unittest.TestCase):
        @set_test_hang_alarm
        def setUp(self):
            pass

        @clear_test_hang_alarm
        def tearDown(self):
            pass

Check out the individual :ref:`helpers <api>` for more examples.

Project Documentation
-----------------------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api
   changelog
   license
   authors
   kudos
   contributing

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
