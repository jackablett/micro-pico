# Micro Pico LOG Module

Import the LOG module into the **main.py**

```python
from micro_pico import log
```

## Functions

Log a peice of Information content

```python
log.info(info string content here...)
```

Log a peice of Warning content

```python
log.warn(warn string content here...)
```

Log a peice of Error content

```python
log.error(error string content here...)
```

## Other functions

Get the current local time (returns date & time as a string)

```python
log.datetime_string()
```

Reads then prints out the log file

```python
log.read_logs()
```
