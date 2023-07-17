from enum import Enum


class ExpectedJSON(Enum):
    NOT_FOUND = {
        "detail": "Страница не найдена"
    }
    FIELD_CANNOT_BE_EMPTY = ['This field may not be blank']
    FIELD_CANNOT_CONTAINS_MORE_100 = ['Убедитесь, что это значение содержит не более 100 символов.']

    PAYMENT_SERVICE_WITH_THIS_NAME_EXISTS = ['payment service with this name already exists.']
    PAYMENT_SERVICE_EXCEEDED_NAME_LENGTH = ['Ensure this field has no more than 30 characters']
    PAYMENT_SERVICE_NOT_FOUND = {
            "detail": "Not found."
        }

    @staticmethod
    def key_value(key, value):
        json = {key: value}
        return json
