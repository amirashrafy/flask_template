

def create_lang(fa, en):
    return {"fa": fa, "en": en}


class Unknown(Exception):
    message = create_lang(
        fa="ارور ناشناخته",
        en="Unknown Error",
    )
    status = 400


class Forbidden(Exception):
    message = create_lang(
        fa="شما به این بخش دسترسی ندارید",
        en="access denied",
    )
    status = 403


class BadRequest(Exception):
    message = create_lang(
        fa="پارامتر های ارسالی اشتباه است",
        en="Error in request validation",
    )
    status = 400


class NotFound(Exception):
    message = create_lang(
        fa="موردی یافت نشد",
        en="Not Found",
    )
    status = 404


class InternalServerError(Exception):
    message = create_lang(
        fa="خطای داخلی سرور",
        en="ّInternal server error",
    )
    status = 500


class ValueIsNotIntNumber(Exception):
    message = create_lang(
        fa="مقدار وارد شده یک عدد صحیح معتبر نیست",
        en="Value is not an int number",
    )
    status = 400

