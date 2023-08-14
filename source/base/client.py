import allure
import requests

from requests import Response
from typing import Dict, Optional, Any, Tuple
from source.base.logger import log


class Requests:
    @staticmethod
    @allure.step("GET request to:\n{url}")
    def get(
            url: str,
            params: Optional[Dict[str, Any]] = None,
            headers: Optional[Dict[str, str]] = None,
            cookies: Optional[Dict[str, str]] = None,
            auth: Optional[Tuple[str, str]] = None
    ) -> Response:
        log.save_request(method="GET", url=url, params=params, headers=headers, cookies=cookies, auth=auth)
        response = requests.get(url=url, params=params, headers=headers, cookies=cookies, auth=auth)
        log.save_response(response=response)
        return response

    @staticmethod
    @allure.step("POST request to:\n{url}")
    def post(
            url: str,
            data: str = None,
            json: Optional[Dict[str, Any]] = None,
            params: Optional[Dict[str, Any]] = None,
            headers: Optional[Dict[str, str]] = None,
            cookies: Optional[Dict[str, str]] = None,
            auth: Optional[Tuple[str, str]] = None
    ) -> Response:
        log.save_request(method='POST', url=url, data=data, json=json, params=params, headers=headers, cookies=cookies,
                         auth=auth)
        response = requests.post(url=url, data=data, json=json, params=params, headers=headers, cookies=cookies,
                                 auth=auth)
        log.save_response(response=response)
        return response

    @staticmethod
    @allure.step("PATCH request to:\n{url}")
    def patch(
            url: str,
            data: str = None,
            json: Optional[Dict[str, Any]] = None,
            params: Optional[Dict[str, Any]] = None,
            headers: Optional[Dict[str, str]] = None,
            cookies: Optional[Dict[str, str]] = None,
            auth: Optional[Tuple[str, str]] = None
    ) -> Response:
        log.save_request(method='PATCH', url=url, data=data, json=json, params=params, headers=headers, cookies=cookies,
                         auth=auth)
        response = requests.patch(url=url, data=data, json=json, params=params, headers=headers, cookies=cookies,
                                  auth=auth)
        log.save_response(response=response)
        return response

    @staticmethod
    @allure.step("PUT request to:\n{url}")
    def put(
            url: str,
            data: str = None,
            json: Optional[Dict[str, Any]] = None,
            params: Optional[Dict[str, Any]] = None,
            headers: Optional[Dict[str, str]] = None,
            cookies: Optional[Dict[str, str]] = None,
            auth: Optional[Tuple[str, str]] = None
    ) -> Response:
        log.save_request(method='PUT', url=url, data=data, json=json, params=params, headers=headers, cookies=cookies,
                         auth=auth)
        response = requests.put(url=url, data=data, json=json, params=params, headers=headers, cookies=cookies,
                                auth=auth)
        log.save_response(response=response)
        return response

    @staticmethod
    @allure.step("DELETE request to:\n{url}")
    def delete(
            url: str,
            data: str = None,
            json: Optional[Dict[str, Any]] = None,
            params: Optional[Dict[str, Any]] = None,
            headers: Optional[Dict[str, str]] = None,
            cookies: Optional[Dict[str, str]] = None,
            auth: Optional[Tuple[str, str]] = None
    ) -> Response:
        log.save_request(method='DELETE', data=data, json=json, params=params, headers=headers, cookies=cookies,
                         auth=auth)
        response = requests.delete(url=url, data=data, json=json, params=params, headers=headers, cookies=cookies,
                                   auth=auth)
        log.save_response(response=response)
        return response


client = Requests()
