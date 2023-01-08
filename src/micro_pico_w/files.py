import os

# https://github.com/jackablett/micro-pico/blob/main/documentation/modules/files.md

def file_exists(filename): # Return True if the file with the name is found
  try:
    return (os.stat(filename)[0] & 0x4000) == 0
  except OSError:
    return False
