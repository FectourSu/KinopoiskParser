import argparse

class Console():

	@staticmethod
	def parse_args() -> argparse.Namespace:
		arg_parser = argparse.ArgumentParser()	
		arg_parser.add_argument(
			'-kp',
			'--kinopoisk',
			type=int,
			metavar='kp_id',
			help='The source of kinopoisk --kp, as the parameter of the movie id'
		)
		return arg_parser.parse_args()
