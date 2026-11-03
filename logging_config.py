import logging
import logging.config
import os
from pathlib import Path

try:
    from colorlog import ColoredFormatter
except ImportError:  # optional dependency
    ColoredFormatter = None

LOG_DIR = Path("logs")


def setup_logging() -> None:
    """App start hote hi ek baar call karo."""
    debug = os.getenv("DEBUG", "false").lower() == "true"
    log_level = "DEBUG" if debug else "INFO"

    LOG_DIR.mkdir(exist_ok=True)

    # Console formatter: colorlog ho toh colored, nahi toh plain
    if ColoredFormatter is not None:
        console_formatter = {
            "()": ColoredFormatter,
            "format": "%(log_color)s[%(levelname)-8s] [%(asctime)s] %(name)s: %(message)s",
            "log_colors": {
                "DEBUG": "cyan",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "red,bold",
            },
        }
    else:
        console_formatter = {
            "format": "[%(levelname)-8s] [%(asctime)s] %(name)s: %(message)s",
        }

    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "console": console_formatter,
            "file": {
                "format": (
                    "%(asctime)s | %(levelname)-8s | %(name)s | "
                    "%(funcName)s:%(lineno)d | %(message)s"
                ),
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": log_level,
                "formatter": "console",
            },
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "DEBUG",  # file mein hamesha sab kuch
                "formatter": "file",
                "filename": str(LOG_DIR / "app.log"),
                "maxBytes": 5 * 1024 * 1024,  # 5 MB
                "backupCount": 3,             # 3 purani files rakho
                "encoding": "utf-8",
            },
        },
        "loggers": {
            # noisy libraries ko chup karao
            "urllib3": {"level": "WARNING"},
            "requests": {"level": "WARNING"},
        },
        "root": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
        },
    }

    logging.config.dictConfig(logging_config)