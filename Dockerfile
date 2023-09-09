FROM python:3.11-slim-bookworm

WORKDIR /usr/project

VOLUME /usr/project/allure-results

RUN apt-get update && apt-get install -y \
    default-jre \
    default-jdk \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

RUN curl -o allure-commandline-2.23.0.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.23.0/allure-commandline-2.23.0.tgz \
    && tar -zxvf allure-commandline-2.23.0.tgz -C /opt/ \
    && ln -s /opt/allure-2.23.0/bin/allure /usr/bin/allure \
    && rm -rf allure-commandline-2.23.0.tgz

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 9999