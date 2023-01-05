# Micro Pico LOG Module

Import the LOG module into the **main.py**

```python
from micro_pico import log
```

## Functions

Log a peice of Information

```python
log.info(info string content here...)
```

Log a Warning content

```python
log.warn(warn string content here...)
```

Log an Error content

```python
log.error(error string content here...)
```

## Other function

Get the current local time, (returns date & time as a string)

```python
log.datetime_string()
```
