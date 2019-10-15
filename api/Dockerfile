FROM python:3-onbuild
COPY . /api
WORKDIR /api
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["api.py"]

