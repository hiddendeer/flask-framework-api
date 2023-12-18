import json
from flask import Response


class HttpResponse(Response):

    def __int__(self, data=None, status=None, ):
        print('11111')
        # std_data = {
        #     "code": 2000,
        #     "data": data,
        # }
        # super().__int__(json.dumps(std_data))
