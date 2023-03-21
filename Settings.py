import json
import os
class Storage:

    __title="%(title)s.mp4"

    def __init__(self):
        self.option={"outtmpl":self.__title}
        self.settomgs_path=os.path.join(os.getcwd(),"Settings","Setting.json")
        if self.settomgs_path is None:
            self.MakeJson()
    def MakeJson(self):
        with open (self.settomgs_path,"w") as jf:
            jf.write(json.dumps(self.option))
    def ReadJson(self)->dict:
        with open (self.settomgs_path) as jf:
            return json.load(jf)
    def Change_Storage(self,storage_path:str)->dict:
        dictionary=self.ReadJson()
        if storage_path in dictionary.values():
            return self.option
        else:
            self.option["outtmpl"]=os.path.join(storage_path,self.__title)
            self.MakeJson()
            return self.option



