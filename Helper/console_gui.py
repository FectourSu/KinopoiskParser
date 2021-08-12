import argparse

class Console():
	def __init__(self) -> argparse.Namespace:
		arg_parser = argparse.ArgumentParser()	

	@staticmethod
	def parse_args(self) -> argparse.Namespace:
		self.arg_parser.add_argument(
			'-kp',
			'--kinopoisk',
			type=int,
			metavar='kp_id',
			help='The source of kinopoisk --kp, as the parameter of the movie id'
		)
		return self.arg_parser.parse_args()
