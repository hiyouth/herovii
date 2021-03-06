
from flask import json
from flask import request,url_for
from flask import current_app
from werkzeug.exceptions import HTTPException
from werkzeug._compat import text_type


class APIException(HTTPException):
    code = 400
    error = 'invalid_request'
    error_code = 999

    def __init__(self, error=None, error_code=None, code=None, response=None):
        if code is not None:
            self.code = code
        if error is not None:
            self.error = error
        if error_code is not None:
            self.error_code = error_code
        super(APIException, self).__init__(error, response)

    def get_body(self, environ=None):

        return text_type(json.dumps(dict(
            msg=self.error,
            code=self.error_code,
            request=request.method+'  '+self.get_url_no_param()
        )))

    # 截取url ‘?’ 前的路径
    def get_url_no_param(self):
        full_path = str(request.full_path)
        q_index = full_path.find('?')
        full_path = full_path[0:q_index]
        return full_path

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]


class FormError(APIException):

    # error_code=1000 means 参数错误
    def __init__(self, form, error='invalid_parameter', error_code=1000, response=None):
        self.form = form
        super(FormError, self).__init__(error, error_code, None, response)

    def get_body(self, environ=None):
        if current_app.config['SHOW_DETAIL_ERROR']:
            self.error = str(self.form.errors)
        return super().get_body(environ)
