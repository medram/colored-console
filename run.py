from MRLogger import init_logger

if  __name__== '__main__':
	
	format = '<BG_COLOR>[%(levelname)s]<RESET><COLOR>[%(asctime)s]: %(message)s<RESET>'

	# use "force=True" if you just want to color git bach messages on windows
	logger = init_logger(force=True, format=format)

	logger.debug('Hellow World!')
	logger.info('Hellow World!')
	logger.warning('Hellow World!')
	logger.error('Hellow World!')
