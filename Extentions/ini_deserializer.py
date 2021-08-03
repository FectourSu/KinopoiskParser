import os
import errno

#There is no point in making it asynchronous
class IniDeserializer():

	@staticmethod
	def deserialize(config, f_name):
		try:
			if os.path.exists(f_name) == False:
				open(f_name, "w").close
		except OSError as exc: 
			print(exc)
			if exc.errno != errno.EEXIST:
				raise
		config.read(f_name)
		return config