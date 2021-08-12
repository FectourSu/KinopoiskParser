import json
import errno
import os
import asyncio

class JsonSerializer():
	@staticmethod
	async def serialize(data, id:int):
		jsonfile = f'src/{id}.json'
		if not os.path.exists(os.path.dirname(jsonfile)):
			try:
				await asyncio.sleep(0)
				os.makedirs(os.path.dirname(jsonfile))
			except OSError as exc: 
				if exc.errno != errno.EEXIST:
					raise
		with open(jsonfile, "w", encoding='utf8') as write_file:
			await asyncio.sleep(0)
			json.dump(data, write_file, indent=4, ensure_ascii=False)

