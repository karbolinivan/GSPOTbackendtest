from enum import Enum


class ExpectedJSON(Enum):
    NOT_FOUND = {
        "detail": "Страница не найдена."
    }
    FIELD_CANNOT_BE_EMPTY = ['This field may not be blank']
    FIELD_CANNOT_BE_EMPTY_RUS = ['Это поле не может быть пустым.']
    FIELD_CANNOT_CONTAINS_MORE_100 = ['Убедитесь, что это значение содержит не более 100 символов.']

    PAYMENT_SERVICE_WITH_THIS_NAME_EXISTS = ['payment service with this name already exists.']
    PAYMENT_SERVICE_EXCEEDED_NAME_LENGTH = ['Ensure this field has no more than 30 characters']
    PAYMENT_SERVICE_NOT_FOUND = {
        "detail": "Not found."
    }

    PAYMENT_ACCOUNTS_OWNER_LESS_THAN_ALLOWED_COMMISSION = ["Ensure this value is greater than or equal to 0."]
    PAYMENT_ACCOUNTS_OWNER_EXCEEDED_LENGTH_COMMISSION = ["Ensure this value is less than or equal to 100."]
    PAYMENT_ACCOUNTS_OWNER_INVALID_VALUE_COMMISSION = ["A valid number is required."]
    PAYMENT_ACCOUNTS_OWNER_MORE_THAN_2_DECIMAL_PLACES_COMMISSION = [
        "Ensure that there are no more than 2 decimal places."]
    PAYMENT_ACCOUNTS_OWNER_MORE_THAN_5_DIGITS_IN_TOTAL_COMMISSION = [
        "Ensure that there are no more than 5 digits in total."]
    PAYMENT_ACCOUNTS_OWNER_INVALID_VALUE_FROZEN_TIME = [
        "Duration has wrong format. Use one of these formats instead: [DD] [HH:[MM:]]ss[.uuuuuu]."]
    PAYMENT_ACCOUNTS_OWNER_INVALID_VALUE_GIFT_TIME = [
        "Duration has wrong format. Use one of these formats instead: [DD] [HH:[MM:]]ss[.uuuuuu]."]
    PAYMENT_ACCOUNTS_OWNER_INVALID_VALUE_PAYOUT_DAY = ["A valid integer is required."]

    PAYMENT_ACCOUNTS_PAYOUT_DATA_INVALID_VALUE_ACCOUNT_NUMBER_YOO_MONEY = [
        "yoomoney account number should contain only digits"]
    PAYMENT_ACCOUNTS_PAYOUT_DATA_INVALID_VALUE_PAYOUT_TYPE = ["\"paypal\" is not a valid choice."]
    PAYMENT_ACCOUNTS_PAYOUT_NO_AVAILABLE_BALANCE = "Developer has not required amount on balance to withdraw"

    @staticmethod
    def key_value(key, value):
        json = {key: value}
        return json
