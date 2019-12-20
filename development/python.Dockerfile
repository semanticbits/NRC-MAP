FROM python:latest

WORKDIR /usr/src/NRC-MAP

COPY . .

RUN pip3 install --upgrade pip \
	&& pip3 install --no-cache-dir -r requirements.txt \
	&& pip3 install -e .[all] \
	&& curl -sL https://deb.nodesource.com/setup_11.x | bash - \
	&& apt-get update -y \
	&& apt-get upgrade -y \
	&& apt-get install -y \
		apt-utils \
		nodejs \
	&& jupyter labextension install jupyterlab-drawio \
	&& rm -rf /tmp/* \
	&& rm -rf /var/lib/apt/lists/* \
	&& apt-get clean

CMD [ "/bin/bash" ]

