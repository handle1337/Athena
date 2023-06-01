# syntax=docker/dockerfile:1

FROM ubuntu:22.04

SHELL ["/bin/bash", "-c"]

# Install packages
RUN \
    apt update && \
    apt install -y \
    python-setuptools \
    python3-setuptools \
    python3-pip \
    chromium-browser \
    git \
    curl \
    wget \
    python2 \
    python3 \
    zip \
    unzip \
    dos2unix



ENV SHODAN_TOKEN=""
ENV NGROK_TOKEN=""
ENV DISCORD_TOKEN=""

# Install go
WORKDIR /tmp
RUN \
    wget -q https://go.dev/dl/go1.20.4.linux-amd64.tar.gz && \
    rm -rf /usr/local/go && \
    tar -C /usr/local -xzf go1.20.4.linux-amd64.tar.gz
ENV GOPATH "/root/go"
ENV PATH "$PATH:/usr/local/go/bin:$GOPATH/bin"

WORKDIR /opt
#RUN git clone https://github.com/danielmiessler/SecLists.git

RUN mkdir tools

WORKDIR /tools
RUN \
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | bash -s -- -y && \
    #source /.cargo/env && \
    git clone https://github.com/RustScan/RustScan && \
    cd RustScan/
    #cargo build --release && \
    #cp target/release/rustscan /bin/rustscan && \
    #cd .. && \
    #curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && \
    #echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | tee /etc/apt/sources.list.d/ngrok.list && \
    #apt update && \
    #apt install ngrok -y && \
    #git clone https://github.com/Sachin-v3rma/Astra && cd Astra/ && \
    #pip3 install -r requirements.txt && \
    #cd .. && \
    #git clone https://github.com/xnl-h4ck3r/waymore.git && \
    #cd waymore && \
    #python3 setup.py install && \
    #chmod +x waymore.py && \
    #dos2unix waymore.py



WORKDIR /athena
RUN \
#   ngrok config add-authtoken $NGROK_TOKEN && \
    apt install nmap -y && \
    go install github.com/tomnomnom/httprobe@latest && \
    go install github.com/ffuf/ffuf@latest && \
 #   go install -v go install -v github.com/owasp-amass/amass/v3/...@master && \
    go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest && \
    go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest

#RUN apt install nmap -y

# Setup main app
COPY . .
#COPY *.py .
# Install Python requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# run
CMD [ "python3", "athena.py" ]