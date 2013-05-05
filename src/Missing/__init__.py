import os

if not 'PURE_PYTHON' in os.environ:  # pragma no cover
    try:
        from _Missing import *
    except ImportError:
        pass
