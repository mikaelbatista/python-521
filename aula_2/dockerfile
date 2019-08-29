FROM ubuntu

RUN apt update && apt install apache2 -y

COPY entrypoint.sh /usr/local/bin

ENTRYPOINT [ "sh", "/usr/local/bin/entrypoint.sh" ]

CMD [ "/bin/bash" ]
