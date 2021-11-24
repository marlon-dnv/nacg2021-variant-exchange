from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional


@dataclass
class Creds:
    credfile: Path
    _data: Optional[Dict[str, str]] = None

    def __init__(self, credfile: str = "vx_creds.json") -> None:
        self.credfile = Path(credfile)
        self.load()

    def load(self, credfile: Optional[str] = None):
        if credfile:
            self.credfile = Path(credfile)
        if not self.credfile.exists():
            raise FileNotFoundError(f"Could not find credentials file: {credfile}")
        self._data = json.loads(self.credfile.read_text())

    def _get_property(self, key: str):
        if self._data is None:
            self.load()
            assert self._data is not None
        if key not in self._data:
            raise KeyError(f"Could not find {key} in credential file: {self.credfile}")
        return self._data[key]

    @property
    def username(self):
        return self._get_property("username")

    @property
    def password(self):
        return self._get_property("password")

    @property
    def subscriptionKey(self):
        return self._get_property("subscriptionKey")
