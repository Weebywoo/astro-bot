import datetime
from typing import Literal


def log(severity: Literal["info", "error"], message: str) -> None:
    print(f"[{datetime.datetime.now()}]", f"[{severity}]", message)
