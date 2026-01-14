from configer import config
from Load_layer import bulkloader,parser,loadi
from storage import storage


conf = config.Config()
load = loadi.Loader(conf)
pars = parser.Parser(conf)
stora = storage.Storage(conf)
bulk = bulkloader.Bulkloader_mashine(conf,stora,pars,load)

bulk.loader_looper()
#loaded_data = load.load_data()
#print(loaded_data)

#parsed_data = pars.parse(loaded_data)
#stora.safe_csv(parsed_data)
#print(parsed_data)


