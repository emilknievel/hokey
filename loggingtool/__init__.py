import logging
log = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)-5s: %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)
log.setLevel(logging.DEBUG)
