import logging
import sys

FORMAT = "<COLOR><BOLD>[%(levelname)s]<RESET><COLOR> %(message)s<RESET>"
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, GREY, INTENSITY = range(9)
BG_BLACK, BG_RED, BG_GREEN, BG_YELLOW, BG_BLUE, BG_MAGENTA, BG_CYAN, BG_GREY, BG_INTENSITY = range(0, 90, 10)

#These are the sequences need to get colored ouput
COLOR_SEQ = "\033[0;%dm"
RESET_SEQ = "\033[0m"
BOLD_SEQ = "\033[1m"

COLORS = {
	'DEBUG': GREY,
	'INFO': BLUE,
	'WARNING': YELLOW,
	'ERROR': RED,
	'CRITICAL': RED
}

BG_COLORS = {
	'BG_DEBUG': BG_GREY,
	'BG_INFO': BG_BLUE,
	'BG_WARNING': BG_YELLOW,
	'BG_ERROR': BG_RED,
	'BG_CRITICAL': BG_RED
}

def colorate_message(message, color=8, use_color=True):
	if use_color:
		message = message.replace('<COLOR>', COLOR_SEQ % (30 + color)).replace('<BG_COLOR>', COLOR_SEQ % (30 + color + 10)).replace('<BOLD>', BOLD_SEQ).replace('<RESET>', RESET_SEQ)
	else:
		message = message.replace('<COLOR>', '').replace('<BG_COLOR>', '').replace('<BOLD>', '').replace('<RESET>', '')
	return message


class ColoredFormatter(logging.Formatter):
	def __init__(self, msg, use_color=True):
		logging.Formatter.__init__(self, msg)
		self.use_color = use_color

	def format(self, record):
		result = logging.Formatter.format(self, record)
		if record.levelname in COLORS:
			result = colorate_message(result, color=COLORS[record.levelname], use_color=self.use_color)
		return result

def init_logger(colored=True, level=logging.DEBUG, format=FORMAT):
	logger = None

	colored = colored if sys.platform != 'win32' else False

	logger = logging.getLogger(name='my_logger')
	logger.setLevel(level)

	console = logging.StreamHandler()
	#console.setLevel(logging.DEBUG)
	console.setFormatter(ColoredFormatter(format, use_color=colored))
	logger.addHandler(console)

	return logger