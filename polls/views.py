from django.http import HttpRequest, JsonResponse


def index(request: HttpRequest) -> JsonResponse:
    """
    Метод для тестирования инициализации приложения
    :param request: empty
    :return: {"message": "Hello world"}
    """
    return JsonResponse({"message": "Hello world"})
