FROM python:3.8 AS python


# timezone part
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ "Europe/Paris"
RUN echo $TZ > /etc/timezone && \
apt-get update && apt-get install -y tzdata && \
rm /etc/localtime && \
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
dpkg-reconfigure -f noninteractive tzdata

# dependance part
RUN apt-get update && apt-get install -y libsasl2-dev python-dev libldap2-dev libssl-dev \
 llvm  binutils git autoconf automake build-essential libhdf5-serial-dev vim g++ git cmake \
 swig libncurses5-dev libedit-dev libpthread-stubs0-dev g++ make  && apt-get clean .tmp-build-deps

RUN mkdir /code && mkdir /data
WORKDIR /code
RUN pip install -U pip

FROM python as base


COPY --from=icalialabs/watchman:4-alpine3.4 /usr/local/bin/watchman* /usr/local/bin/
RUN mkdir -p /usr/local/var/run/watchman \
 && touch /usr/local/var/run/watchman/.not-empty

