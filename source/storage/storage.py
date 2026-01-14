class Storage():
    def __init__(self,config):
        self.configer = config
       # self.ticker = self.configer.ticker


    def save(self,raw):
        a = self.configer.raw_path
        with open(f"{a}/blalala2.csv","w") as g:
            g.write(raw)

    def safe_parquet(self,raw,ticker):
        a = self.configer.raw_path
        raw.write_parquet(f"{a}/{ticker}.parquet")


