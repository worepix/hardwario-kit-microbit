# hardwario-kit-microbit
micro:bit HARDWARIO KIT Modules implementation

## Install library to micro:bit
Install CLI tool for copying library

    pip3 install microfs

Copy library to micro:bit

    ufs put hio.py

## Examples

### Tmp112

```python
from hio import *

tmp112_init()
print(tmp112_read())
```

