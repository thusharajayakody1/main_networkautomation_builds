FROM ubuntu:18.04
MAINTAINER thusharaj "thushara.k.jayakody@icloud.com"

RUN apt-get update
RUN apt-get upgrade -y
RUN mkdir -p /networkautomation
WORKDIR /networkautomation
COPY . .

RUN apt-get install python -y
RUN apt-get install build-essential libssl-dev libffi-dev -y
RUN apt-get --yes --force-yes install python-pip
RUN pip install cryptography
RUN pip install -r Buildjobpipfile.txt

ENTRYPOINT [ "python" ]

CMD [ "networkautomation/spanningtreetrafficdeviders/spanningtreetrafficdevider.py" ]