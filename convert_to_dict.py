#!/usr/bin/python3
class ConvertToDict():
    def __init__(self):
        pass

    def convert_to_dict(self, result):
        result_dict = dict()
        result_dict['id'] = result["_id"]
        result_dict['index'] = result["_index"]
        return result_dict
