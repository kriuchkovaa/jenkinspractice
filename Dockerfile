FROM jenkins/jenkins:latest
 
USER root
#referenced: https://docs.docker.com/engine/install/debian/ and matched up to Dockerfile format
RUN apt-get update -qq \
    && apt-get install -qqy  \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
WORKDIR /etc/apt/keyrings
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg

RUN echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

RUN apt-get update  -qq \
    && apt-get install docker-ce docker-ce-cli containerd.io -y
 
RUN usermod -aG docker jenkins



