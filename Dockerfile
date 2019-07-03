FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /project_code
ADD . /project_code
WORKDIR /project_code
RUN ls
RUN pip install -r requirements.txt
ENV USING_DOCKER=1
RUN chmod +x start.sh
ENTRYPOINT ["sh", "start.sh"]
EXPOSE 8000
