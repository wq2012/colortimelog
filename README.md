# colortimelog: Logging elapsed time and errors in colors

[![Python package](https://github.com/wq2012/colortimelog/actions/workflows/python-package.yml/badge.svg)](https://github.com/wq2012/colortimelog/actions/workflows/python-package.yml)
[![PyPI Version](https://img.shields.io/pypi/v/colortimelog.svg)](https://pypi.python.org/pypi/colortimelog)
[![Python Versions](https://img.shields.io/pypi/pyversions/colortimelog.svg)](https://pypi.org/project/colortimelog)
[![Downloads](https://static.pepy.tech/badge/colortimelog)](https://www.pepy.tech/projects/colortimelog)

![demo](resources/demo.gif)

## Install

```
pip install colortimelog
```

## Usage

### Add timing for a function

```python
import colortimelog

@colortimelog.timefunc
def my_function():
  ...
```

### Add timeing for a block of code

```python
import colortimelog

with colortimelog.timeblock("Doing XYC"):
  do_x()
  do_y()
  do_z()
```

### Add logging with verbosity control

```python
import colortimelog

logger = colortimelog.Logger(verbosity=3)
logger.debug("Debugging message will not show")
logger.info("This is info")
logger.warning("This is warning")
logger.error("This is an error")
logger.fatal("This will raise exception")

logger.verbosity = 4
logger.debug("Debugging message will now show")
```
