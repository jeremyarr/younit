'''
younit is a collection of helpers for the :mod:`unittest` module.
'''

from .__version__ import __version__


from .main import *

def one_plus_one():
    '''silly function'''

    return 2

__all__ = ["TestHang","test_name","set_test_hang_alarm",
            "clear_test_hang_alarm","test_hang_alarm","close_all_threads",
            "asyncio_test","AsyncMock"]