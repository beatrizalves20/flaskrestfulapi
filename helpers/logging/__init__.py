import logging

logger = logging

logger.basicConfig(level=logging.INFO,
                   format='%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s',
                   handlers=[logging.FileHandler("helloflask.log", mode='w'), logging.StreamHandler()])

stream_handler = [h for h in logger.root.handlers if isinstance(h, logger.StreamHandler)][0]
stream_handler.setLevel(logger.INFO)