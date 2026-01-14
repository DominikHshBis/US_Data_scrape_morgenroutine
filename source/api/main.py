from configer import config
from Load_layer import bulkloader


conf = config.Config()
bulk = bulkloader.bulkloader_mashine(conf)
bulk.datei_erstellen()

