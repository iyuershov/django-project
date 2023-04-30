from django.http import HttpRequest, JsonResponse


def hello_world_view(request: HttpRequest) -> JsonResponse:
    """
    Метод для тестирования инициализации приложения
    :param request: HttpRequest object
    :return: {"message": "Hello world"}
    """
    return JsonResponse({"message": "Hello world"})
