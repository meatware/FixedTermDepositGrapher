import os
from yaml import safe_load
from typing import List, Dict, Any, NamedTuple


class Deposit(NamedTuple):
    """Named tuple that defines live job parameters for AD."""
    acc_no: str


