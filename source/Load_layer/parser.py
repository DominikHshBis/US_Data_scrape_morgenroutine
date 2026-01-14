import polars as pl
from io import StringIO

class Parser:
    def __init__(self,config):
        self.configer = config

    def parse(self, raw):

        df = pl.read_csv(StringIO(raw), separator=";")
        # raw kann JSON, CSV-String, Dict, Liste, HTML etc. sein
       # df = pl.DataFrame(raw)
        print(df)
        

       # print(df.columns)

        # Beispiel: Spalten normalisieren
        #df = df.rename({"Date": "date", "Close": "close"})

        # Beispiel: Typen setzen
      #  df = df.with_columns([
        #    pl.col("date").str.strptime(pl.Date),
        #    pl.col("close").cast(pl.Float64)
       # ])

        return df

