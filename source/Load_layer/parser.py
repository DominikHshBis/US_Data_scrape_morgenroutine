import polars as pl

class Parser:
    def parse(self, raw):
        # raw kann JSON, CSV-String, Dict, Liste, HTML etc. sein
        df = pl.DataFrame(raw)

        # Beispiel: Spalten normalisieren
        df = df.rename({"Date": "date", "Close": "close"})

        # Beispiel: Typen setzen
        df = df.with_columns([
            pl.col("date").str.strptime(pl.Date),
            pl.col("close").cast(pl.Float64)
        ])

        return df

