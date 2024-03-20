FROM bellsoft/liberica-openjdk-alpine-musl:17 AS base

RUN apk add --no-cache dpkg
COPY . .
ENV WSPORT 8080
ENV WEBSKD_VERSION 0.4.1
RUN dpkg --add-architecture amd64
RUN wget https://github.com/joewalnes/websocketd/releases/download/v$WEBSKD_VERSION/websocketd-$WEBSKD_VERSION\_amd64.deb && \
    dpkg -i websocketd-$WEBSKD_VERSION\_amd64.deb && \
    rm websocketd-$WEBSKD_VERSION\_amd64.deb

CMD websocketd --port=$WSPORT /bin/sh -c "java -jar problem_4.jar 2>&1"
