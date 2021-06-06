FROM centos:7
RUN yum install epel-release python3 -y
RUN yum install nginx python3 -y
RUN pip3 install mysql-connector-python
RUN chkconfig nginx on
RUN rm -f /usr/share/nginx/html/index.html
COPY get-data.py /bin/
COPY GetData.service /etc/systemd/system/GetData.service
RUN chmod 644 /etc/systemd/system/GetData.service
RUN systemctl enable GetData.service
ENV container=docker
