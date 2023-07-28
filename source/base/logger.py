import datetime
import json
import logging
import os
import allure


class Log:
    def __init__(self):
        self._time_request = None
        self._time_response = None
        self.message_request = None
        self.message_response = None
        self.logger = logging.Logger("API")
        self._setup()

    @staticmethod
    def _get_current_time(formats):
        return datetime.datetime.now().strftime(formats)

    def _setup(self):
        self.logger.setLevel(logging.INFO)

        if not os.path.exists('logs'):
            os.makedirs('logs', exist_ok=True)

        current_time = self._get_current_time("%Y-%m-%d_%H-%M-%S")
        filename = f'./logs/log_{current_time}.log'
        handler = logging.FileHandler(filename)

        date_format = "%Y-%m-%d_%H:%M:%S"
        log_format = f"%(asctime)s\n" \
                     f"%(message)s"

        formatter = logging.Formatter(log_format, datefmt=date_format)
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

    def _attach_all_message(self):
        if self.message_request and self.message_response:
            message_request = f'{self._time_request}\n{self.message_request}'
            message_response = f'\n{self._time_response}\n{self.message_response}'
            all_message = message_request + message_response
            allure.attach(all_message, name='Logs', attachment_type=allure.attachment_type.TEXT)

            self._time_request = None
            self._time_response = None
            self.message_request = None
            self.message_response = None

    def save_request(self, method, **kwargs):
        self._time_request = self._get_current_time("%d.%m.%Y_%H:%M:%S.%f")
        message = f'REQUEST: {method}' \
                  f'\nurl: {kwargs.get("url")}' \
                  f'\nheaders: {json.dumps(kwargs.get("headers"), indent=2)}' \
                  f'\ncookie: {kwargs.get("cookie")}' \
                  f'\nauth: {kwargs.get("auth")}' \
                  f'\ndata: {kwargs.get("data")}' \
                  f'\nparams: {json.dumps(kwargs.get("params"), indent=2)}' \
                  f'\njson: {json.dumps(kwargs.get("json"), indent=2)}\n'

        self.logger.info(msg=message)
        self.message_request = message

    def save_response(self, response):
        self._time_response = self._get_current_time("%d.%m.%Y_%H:%M:%S.%f")
        message = f'RESPONSE' \
                  f'\nstatus code: {response.status_code}' \
                  f'\nheaders: {json.dumps(dict(response.headers), indent=2)}'

        if response.text:
            message += f'\njson: {json.dumps(response.json(), indent=2, ensure_ascii=False)}\n'

        self.logger.info(msg=message)
        self.message_response = message
        self._attach_all_message()


log = Log()
