from configer import config
from Load_layer import bulkloader,parser,loadi
from storage import storage


conf = config.Config()
load = loadi.Loader(conf)
pars = parser.Parser(conf)
stora = storage.Storage(conf)
bulk = bulkloader.Bulkloader_mashine(conf,stora,pars,load)

bulk.loader_looper()





