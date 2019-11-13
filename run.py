from MRLogger import init_logger

if  __name__== '__main__':
	logger = init_logger()

	logger.debug('this is a debug message.')
	logger.info('Hi this is an error!')
	logger.warning('Hi this is an error!')
	logger.error('Hi this is an error!')
