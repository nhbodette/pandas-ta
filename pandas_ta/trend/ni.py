# -*- coding: utf-8 -*-
from pandas_ta.overlap import sma
from pandas_ta.utils import get_offset, verify_series

# - Standard definition of your custom indicator function (including docs)-

def ni(close, length=None, centered=False, offset=None, **kwargs):
    """
    Example indicator ni
    """
    # Validate Arguments
    length = int(length) if length and length > 0 else 20
    close = verify_series(close, length)
    offset = get_offset(offset)

    if close is None: return

    # Calculate Result
    t = int(0.5 * length) + 1
    ma = sma(close, length)

    ni = close - ma.shift(t)
    if centered:
        ni = (close.shift(t) - ma).shift(-t)

    # Offset
    if offset != 0:
        ni = ni.shift(offset)

    # Handle fills
    if "fillna" in kwargs:
        ni.fillna(kwargs["fillna"], inplace=True)
    if "fill_method" in kwargs:
        ni.fillna(method=kwargs["fill_method"], inplace=True)

    # Name and Categorize it
    ni.name = f"ni_{length}"
    ni.category = "trend"

    return ni

ni.__doc__ = \
