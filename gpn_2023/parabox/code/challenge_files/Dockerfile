# docker build -t parabox . && docker run --rm -it -p1337:1337 parabox
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install --no-install-recommends -y socat python3 python3-pip git build-essential libsdl2-dev libglew-dev libgtk-3-dev && \
    apt-get clean

RUN pip3 install --no-cache-dir cryptography==3.3 pwntools

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf && echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

RUN git clone https://github.com/drhelius/Gearboy.git gearboy && cd gearboy && git checkout 25435a844f283c2583370dc0720bef8910aad9b9

WORKDIR /home/ctf/gearboy/

COPY --chmod=0744 headless.patch headless.patch

RUN git apply --ignore-space-change --ignore-whitespace headless.patch

WORKDIR /home/ctf/gearboy/platforms/linux
RUN make

WORKDIR /home/ctf/gearboy/

ARG FLAG=GPNCTF{fake_flag}
RUN echo "$FLAG" > flag.txt

COPY --chmod=0744 parabox.gbc parabox.gbc
COPY --chmod=0755 run run
COPY --chmod=0755 server.py server.py

USER ctf

EXPOSE 1337

ENTRYPOINT [ "socat", "-v", "tcp-l:1337,reuseaddr,fork", "EXEC:./run,stderr" ]
