.. image:: https://cdn.rawgit.com/jeremyarr/younit/2275cf7a/docs/_static/logo_full.png

.. image:: https://tactile.com.au/jenkins/buildStatus/icon?job=younit1
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


`younit <https://github.com/jeremyarr/younit>`_ is a collection of helpers for the `unittest <https://docs.python.org/3/library/unittest.html#module-unittest>`_ module.

Helpers
---------

==========================================  =======================================================
**I want to**                               **Helpers to Use**
Test coroutines                             @asyncio_test
Mock out coroutines                         AsyncMock(), 
                                            @asyncio_test 
Print the name of a test before running it  @test_name
Fail a test if it hangs                     @set_test_hang_alarm, @clear_test_hang_alarm, or
                                            @test_hang_alarm
Close all threads associated with a test    @close_all_threads
==========================================  =======================================================

Get It Now
-----------

.. code-block:: bash

    $ pip install younit

Examples
--------------

Testing and mocking coroutines:

.. code-block:: python

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


Setting up test hang alarms:

.. code-block:: python

    class MyTestCase(unittest.TestCase):
        @set_test_hang_alarm
        def setUp(self):
            pass

        @clear_test_hang_alarm
        def tearDown(self):
            pass



More at https://younit.readthedocs.io
-------------------------------------

Project Links
-------------

- Docs: https://younit.readthedocs.io/
- Changelog: https://younit.readthedocs.io/en/latest/changelog.html
- PyPI: https://pypi.python.org/pypi/younit
- Issues: https://github.com/jeremyarr/younit/issues

License
-------

MIT licensed. See the bundled `LICENSE <https://github.com/jeremyarr/younit/blob/master/LICENSE>`_ file for more details.

