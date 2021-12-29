FROM python: 3.9.7
RUN apt-get update -y
RUN apt-get upgrade -y
WORKDIR /Users/katya.nikitko/iTechArt/Django/udemy_course_devsearch_2/devsearch/devsearch
COPY ./devsearch ./devsearch
CMD ["python3", "./devsearch/manage.py", "runserver", "0.0.0.0:8000"]