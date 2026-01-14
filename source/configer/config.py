import yaml
from pathlib import Path

class Config:
    def __init__(self):
        self._cfg = self._load_yaml()
        
        # Pfade
        self._data_path = Path(self._cfg["paths"]["data"])
        self._raw_path = Path(self._cfg["paths"]["raw"])
        self._processed_path = Path(self._cfg["paths"]["processed"])

        # Loader Settings
        self._stooq_url = self._cfg["loader"]["stooq_url"]
        self._symbols = self._cfg["loader"]["symbols"]

        # Compute Settings
        self._nhnl_lookback = self._cfg["compute"]["nhnl_lookback"]
        self._penny_filter = self._cfg["compute"]["penny_filter"]

    # --- Properties (Getter) ---
    @property
    def data_path(self):
        return self._data_path

    @property
    def raw_path(self):
        return self._raw_path

    @property
    def processed_path(self):
        return self._processed_path

    @property
    def stooq_url(self):
        return self._stooq_url

    @property
    def symbols(self):
        return self._symbols

    @property
    def nhnl_lookback(self):
        return self._nhnl_lookback

    @property
    def penny_filter(self):
        return self._penny_filter

    # --- interne Hilfsmethode ---
    def _load_yaml(self):
        base = Path(__file__).resolve().parent
        path = base / "settings.yaml"
        with open(path, "r") as f:
            return yaml.safe_load(f)

