# this is using the standard base image and trying to install python
FROM registry.access.redhat.com/ubi8/ubi:latest

USER root

RUN yum -y install --disableplugin=subscription-manager python36

RUN echo "Installed Python and now running image"

EXPOSE 80

CMD ["-D", "FOREGROUND"]


# this is using the existing python image and trying to install flask
# Ideally I wont do this, since all libraries would go into a requirements.txt, but this is only to test 
# FROM registry.access.redhat.com/ubi8/python-36:latest

# USER root

# RUN pip3 install flask

# RUN echo "Installed Flask and now running image"

# EXPOSE 80

# CMD ["-D", "FOREGROUND"]
