


from functools import wraps


def dec_func(func):

    @wraps(func)
    def inner(a,b):

        if a<b:
            a,b=b,a 
        
        return func(a,b)
    return inner



@dec_func
def div(a,b):
    print(a/b)

    
# #div=dec_func(div)

div(2,4)






from aiohttp import web

response_ok = 'OK'
response_code = 'responseCode'
response_message = 'responseMessage'
response_data = 'data'
response_fail = 'ERROR'
response_success = 200
response_error = 500
response_unauthorised = 401
response_forbidden = 403
response_not_found = 404
err_body = {"status": response_fail}
ok_body = {"status": response_ok}
response_messages = {
    0: 'Запрос обработан успешно',
    # Раздел 1 - Запрос и тело запроса
    10: 'Некорректный запрос: неизвестный URL или не поддерживаемый метод',
    11: 'Некорректный запрос: ошибка декодирования тела запроса (ошибка парсинга JSON)',
    12: 'Некорректный запрос: отсутствуют обязательные параметры',
    13: 'Некорректный запрос: недопустимые значения параметров',
    14: 'Некорректный запрос: неверная структура запроса',
    # Раздел 2 - Права доступа и пользовательская сессия
    20: 'Истек срок действия сессии',
    21: 'У пользователя недостаточно прав на выполнение данного действия',
    22: 'Отказ в доступе со стороны сервера',
    # Раздел 3 - Сторонние сервисы
    30: 'Внутренняя ошибка стороннего сервиса',
    31: 'Сторонний сервис не отвечает',
    # Раздел 9 - Логика бэкенда БС
    90: 'Ошибка на стороне сервера',
}
codes = {
    0: response_success,
    10: response_not_found,
    11: response_error,
    12: response_error,
    13: response_error,
    14: response_error,
    20: response_error,
    21: response_forbidden,
    22: response_unauthorised,
    30: response_error,
    31: response_error,
    90: response_error,
}


def get_err_handler(number):
    def wrapper():
        response = {
            response_code: number,
            response_message: response_messages[number],
            response_data: err_body
        }
        r = web.json_response(response, status=codes[number])
        return r

    return wrapper


def web_json_response(func):
    @wraps(func)
    def wrapper(instance):
        number = 0
        data = func(instance)
        if not data:
            data = ok_body
        response = {
            response_code: number,
            response_message: response_messages[number],
            response_data: data
        }
        return web.json_response(response, status=codes[number])

    return wrapper





print(get_err_handler(11)())