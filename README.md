# pretty
Python package simplify our logging from different services
### Usage
For debug information about parameters, execution time, etc...
```python
from pretty import pretty_debug


@pretty_debug
def foo(x, y, z):
    do_something()
    ...
```
