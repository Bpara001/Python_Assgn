# Demonstrate how to customize logging output

import logging

extData = {'user': 'joem@example.com'}

# TODO: add another function to log from
def anotherFunction():
    logging.debug("This is a debug-level log message", extra=extData)
def main():
    # set the output file and debug level, and
    # TODO: use a custom formatting specification
    fmtStr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d User:%(user)s %(message)s"
    dateStr = "%m/%d/%Y %I:%M:%S %p"
    logging.basicConfig(filename="output.log",
                        level=logging.DEBUG,
                        format=fmtStr,
                        datefmt=dateStr)
    logging.info("This is an info-level log message")
    logging.warning("This is a warning-level message")
    anotherFunction()

if __name__ == "__main__":
    main()
