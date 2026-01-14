import requests

class Loader:
    def __init__(self, config):
        self.configer = config
      
        
      # self.params = config.api_params
      #  self.headers = config.api_headers

    def load_data(self, ticker):

        self.url = f"https://stooq.com/q/d/l/?s={ticker}&i=d"
        response = requests.get(
            self.url,
         #   params=self.params,
          #  headers=self.headers,
            timeout=10
        )
        #response.raise_for_status()  # wirft Fehler bei 4xx/5xx

        return response.text # raw data zurückgeben

    

