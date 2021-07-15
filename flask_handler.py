#!/usr/bin/python3
from elasticsearch import Elasticsearch
from convert_to_dict import ConvertToDict

conv = ConvertToDict()
es_client = Elasticsearch()

class ElasticHandlers():
    def __init__(self):
        pass

    def es_post(self, index_name, user_obj):
        result = es_client.index(index=index_name, body=user_obj)
        result_dict = conv.convert_to_dict(result)
        return result_dict

    def es_update(self, index_name, user_id, user_obj):
        result = es_client.update(index=index_name, id=user_id, body={"doc":user_obj})
        result_dict = conv.convert_to_dict(result)
        return result_dict

    def es_delete(self, index_name, user_id):
        result =  es_client.delete(index=index_name, id= user_id)
        result_dict = conv.convert_to_dict(result)
        return result_dict

    def es_get(self, index_name, user_id):
        result = es_client.get(index=index_name, id = user_id)
        result_dict = dict()
        result_dict = result["_source"]
        return result_dict

    def es_search(self, index_name, user_id, user_age):
        result = es_client.search(index=index_name, body ={"query":{
                                                                "bool": {
                                                                    "should": [
                                                                        {
                                                                            "match": {
                                                                                "id": user_id
                                                                            }

                                                                        },
                                                                        {
                                                                            "match": {
                                                                                "age": user_age
                                                                            }
                                                                        }
                                                                        ]
                                                                }}})
        for hit in result['hits']['hits']:
            return hit["_source"]