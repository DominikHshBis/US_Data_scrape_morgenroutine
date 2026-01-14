
class Bulkloader_mashine():
        def __init__(self, configer,stora,pars,load):
            self.configer = configer
            self.stora = stora
            self.pars = pars
            self.load = load
            self.tickers = self.configer.ticker
          #  print(self.tickers)

        def loader_looper(self):
            for ticker in self.tickers:
                self.stora.safe_parquet(self.pars.parse(self.load.load_data(ticker=ticker)),ticker)

