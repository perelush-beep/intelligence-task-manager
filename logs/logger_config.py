import logging

logger = logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s | %(levelname)s | %(message)s',
    handlers=[
    logging.StreamHandler(),
    logging.FileHandler('logs/app.log')]
)

logger = logging.getLogger(logger)