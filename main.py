import Helper.console_gui as console
import logging
import time
from kinopoisk import KinopoiskParser
import asyncio

def main():
	args = console.Console().parse_args()

	if args.kinopoisk:
		a  = KinopoiskParser()
		start_time = time.time()
		loop = asyncio.get_event_loop()
		loop.run_until_complete(a.parse(args.kinopoisk))
		print("--- Result time: %s seconds ---" % (time.time() - start_time))  
	else:
		logging.error("Id not specified")
		return

if __name__ == '__main__':
	main()
	