from rest_framework.views import exception_handler


def custom_exeption_handler(exc, context):
    responce = exception_handler(exc, context)
    if responce is not None:
        responce.data["status code"] = responce.status_code
    return responce
