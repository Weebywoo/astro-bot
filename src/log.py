import datetime
from enum import Enum


class Severity(Enum):
    INFO: str = 'INFO'
    ERROR: str = 'ERROR'


def log(severity: Severity, message: str) -> None:
    timestamp: str = f'[{datetime.datetime.now()}]'
    severity: str = f'[{severity.value}]'

    print(timestamp, severity, message)
