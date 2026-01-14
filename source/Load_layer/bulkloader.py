
class bulkloader_mashine():
        def __init__(self, configer):
            self.configer = configer

        def datei_erstellen(self):
            a = self.configer.raw_path
            with open(f"{a}/blalala2.txt","w") as g:
                g.write("erster Test")
