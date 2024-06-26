import logging

# Start logging setup
logger = logging.getLogger("app")

# Set logging levels for specific loggers
logging.getLogger("telegram").setLevel(logging.ERROR)
logging.getLogger("httpx").setLevel(logging.WARNING)

# root logger
logger.root.setLevel(logging.INFO)

# console handler
console_log = logging.StreamHandler()

# message format
format = "∴ %(levelname)s ∴ %(filename)s: line %(lineno)s ∴ %(funcName)s ∴ %(message)s"
console_log.setFormatter(logging.Formatter(format))


logger.root.handlers.clear()
logger.root.addHandler(console_log)

# Log a debug message
logger.debug("Logging setup successfully!")
