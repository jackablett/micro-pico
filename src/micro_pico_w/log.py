import machine

def datetime_string(): # Returns local date & time to be used in the logging definitions
  date_time = machine.RTC().datetime()
  return "{0:04d}-{1:02d}-{2:02d} {4:02d}:{5:02d}:{6:02d}".format(*date_time)

file_name = "log.txt" # Log file name (feel free to change it)

def read_logs(): # Opens, reads then outputs the whole log file to the console
    with open(file_name, 'r') as log_file:
        for line in log_file:
            print(line)

def info(text): # Writes the date & time with [INFO] after followed by the enter content
    datetime = datetime_string()
    log = datetime + " [INFO] " + text + "\n"
    with open(file_name, 'a') as log_entry:
        log_entry.write(log)
        
def warn(text): # Writes the date & time with [WARN] after followed by the enter content
    datetime = datetime_string()
    log = datetime + " [WARN] " + text + "\n"
    with open(file_name, 'a') as log_entry:
        log_entry.write(log)
        
def error(text): # Writes the date & time with [ERROR] after followed by the enter content
    datetime = datetime_string()
    log = datetime + " [ERROR] " + text + "\n"
    with open(file_name, 'a') as log_entry:
        log_entry.write(log)
