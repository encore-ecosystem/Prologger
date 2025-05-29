from datetime import datetime
from contextlib import contextmanager
import sys

class Logger:
    _writer = sys.stdout

    def __init__(self, importance_threshold: int = 0):
        self._importance_threshold = importance_threshold

    def info(self, message: str, importance: int = 0):
        self._print(message, "INFO", importance)

    def warning(self, message: str, importance: int = 0):
        self._print(message, "WARNING", importance)

    def error(self, message: str, importance: int = 0):
        self._print(message, "ERROR", importance)

    def critical(self, message: str, importance: int = 0):
        self._print(message, "CRITICAL", importance)

    def debug(self, message: str, importance: int = 0):
        self._print(message, "DEBUG", importance)

    def _print(self, message: str, extras: str, importance: int):
        text = f"[{datetime.now().strftime("%H:%M:%S %Y/%m/%d")}][{extras}] : {message}\n"
        self._writer.write(text)

    @contextmanager
    def change_writer(self, writer):
        old_writer = self._writer
        self._writer = writer
        try:
            yield None
        finally:
            self._writer = old_writer


__all__ = [
    "Logger",
]
