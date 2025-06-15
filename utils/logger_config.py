# utils/logger_config.py

import logging
import sys

def setup_logger(name: str = __name__, level: int = logging.INFO) -> logging.Logger:
    """
    Configures and returns a logger for the given module name.

    Parameters
    ----------
    name : str, optional
        The name of the logger (typically __name__), by default __name__.
    level : int, optional
        The logging level (e.g., logging.INFO, logging.DEBUG), by default logging.INFO.

    Returns
    -------
    logging.Logger
        Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '[%(levelname)s] %(asctime)s - %(name)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
