#!/usr/bin/env python3
"""
This Script Name v0.1

(A short description of the script...)
"""

import argparse 
import sys
import logging
import os

SCRIPT_NAME = os.path.basename(__file__)
SCRIPT_VERSION = "0.1.0"
log = None
		
def setup_logger(appname, args):
	"""Configure the python logger for improved logging output based on user provided arguments."""
	formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
	screen_handler = logging.StreamHandler(stream=sys.stdout)
	screen_handler.setFormatter(formatter)
	logger = logging.getLogger(appname)
	logger.addHandler(screen_handler)
	if args.verbose:
		logger.setLevel(logging.INFO)
	else:
		logger.setLevel(logging.ERROR)
	return logger

def main(argv):
	global log

	# Example of logging usage, INFO are only shown if --verbose is used.
	log.info("Hello %s!", argv.name)

	# Other examples:
	#log.warning(f"The name provided ({argv.name}) isn't good!")
	#log.error("Please provide a valid name argument!")

	return

if __name__ == "__main__":
	argparser = argparse.ArgumentParser(prog=SCRIPT_NAME, description="%s v%s" % (SCRIPT_NAME, SCRIPT_VERSION))
	argparser.add_argument('--verbose', action="store_true", dest="verbose", help="Verbose output",default=False)
	argparser.add_argument('--name', action="store", dest="name", help="A name!", required=True)
	argparser.add_argument('--myarg', action="store", dest="myarg", help="Another example argument.", default="my_default_value")
	argv = argparser.parse_args()

	# If we want to use argv["name"], uncomment the following line.
	#argv = vars(argv)

	log = setup_logger(SCRIPT_NAME, argv)
	main(argv)