FROM jenkins/jenkins
USER root
RUN apt-get update -y && apt-get install python3 -y && apt-get install vim -y


