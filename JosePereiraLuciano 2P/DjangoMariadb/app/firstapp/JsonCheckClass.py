import json


class CheckJson():

    def isJsonCheck(self,myjson):
        try:
            json_object = json.loads(myjson)
        except ValueError as e:
            return False

        return True
        
