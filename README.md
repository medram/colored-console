# Colored-Console
Colored-Console is good to show nice looking by coloring console messages.
it supports just linux & git bash.

```
from MRLogger import init_logger

if  __name__== '__main__':
	
	# use "force=True" if you just want to color git bach messages on windows
	logger = init_logger(force=True)

	logger.debug('Hellow World!')
	logger.info('Hellow World!')
	logger.warning('Hellow World!')
	logger.error('Hellow World!')
```

![](https://raw.githubusercontent.com/medram/colored-console/master/imgs/colored_1.PNG)

![](https://raw.githubusercontent.com/medram/colored-console/master/imgs/colored_2.PNG)

## Make Your Format

```
from MRLogger import init_logger

if  __name__== '__main__':
	
	format = '<COLOR>[%(levelname)s][%(asctime)s]: %(message)s<RESET>'

	# use "force=True" if you just want to color git bach messages on windows
	logger = init_logger(force=True, format=format)

	logger.debug('Hellow World!')
	logger.info('Hellow World!')
	logger.warning('Hellow World!')
	logger.error('Hellow World!')
```

![](https://raw.githubusercontent.com/medram/colored-console/master/imgs/colored_3.PNG)

![](https://raw.githubusercontent.com/medram/colored-console/master/imgs/colored_4.PNG)

## Bold Font

```
from MRLogger import init_logger

if  __name__== '__main__':
	
	format = '<COLOR><BOLD>[%(levelname)s]<RESET><COLOR>[%(asctime)s]: %(message)s<RESET>'

	# use "force=True" if you just want to color git bach messages on windows
	logger = init_logger(force=True, format=format)

	logger.debug('Hellow World!')
	logger.info('Hellow World!')
	logger.warning('Hellow World!')
	logger.error('Hellow World!')
```

![](https://raw.githubusercontent.com/medram/colored-console/master/imgs/colored_5.PNG)

## Colored Background

```
from MRLogger import init_logger

if  __name__== '__main__':
	
	format = '<BG_COLOR>[%(levelname)s]<RESET><COLOR>[%(asctime)s]: %(message)s<RESET>'

	# use "force=True" if you just want to color git bach messages on windows
	logger = init_logger(force=True, format=format)

	logger.debug('Hellow World!')
	logger.info('Hellow World!')
	logger.warning('Hellow World!')
	logger.error('Hellow World!')
```

![](https://raw.githubusercontent.com/medram/colored-console/master/imgs/colored_6.PNG)