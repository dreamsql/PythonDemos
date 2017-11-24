import tornado.options
import logging
import os








if __name__ == '__main__':
	dir = os.path.dirname(__file__)
	path = os.path.join(dir, 'my.txt')
	handler = logging.FileHandler(path)
	logger = logging.getLogger('demo')
	logger.addHandler(handler)
	logger.setLevel(logging.INFO)
	logger.info('hello world')