import json


class JsonUtil:

    @staticmethod
    def list_to_json(list_elements=None):
        json_string = 'NOREGISTER'
        if len(list_elements) > 0:
            json_string = '{'
            for i, value in enumerate(list_elements):

                json_string += '\n"' + "{id}\":".format(id=value.id) + json.dumps(value.serialize())
                if i < len(list_elements) - 1:
                    json_string += ','
                else:
                    json_string += '\n}'

        return json_string

    @staticmethod
    def instrumented_list_to_json(lista):
        json_string = []
        for item in lista:
            json_string.append(dict(item.serialize()))
        return json_string
