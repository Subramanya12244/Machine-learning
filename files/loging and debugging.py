# topic-4:logging and debugging

# They help developers understand what is happening in their code, identify and fix issues, and track the flow of execution. Let's delve into both topics in detail, along with examples.

import logging
logging.basicConfig(filename="file1.log",level=logging.INFO)  
logging.info("log this line for execution")

logging.debug('This is a debug message')

logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
# basically there are 6 levels defined
# 1.NOTSET-we cannot log
# 2.Debug-we cannot log
# 3.Info
# 4.Warning
# 5.Error
# 6.Critical

# logging.debug("log this line for execution")
# we cannot log the debug

import logging
logging.basicConfig(filename="depth.log",level=logging.DEBUG)

def divide(x, y):
    logging.debug(f"Dividing {x} by {y}")
    result = x/y
    logging.debug(f"Result is {result}")
    return result

divide(10, 0)


