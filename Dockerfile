FROM python:3.11-buster

WORKDIR /usr/project

VOLUME /usr/project/allure_results

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .