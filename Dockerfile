# base-line image
FROM python:3.6.9

# 프로젝트 clone
# ex) git clone https://github.com/flask_app.git
RUN git clone "https://github.com/youseonh/opener.git"

# 현재 디렉토리의 모든 파일들을 컨테이너의 /app 디렉토리에 복사한다.
COPY . /app

# flask의 작업 위치가 /app이라는 뜻
WORKDIR /app

RUN pip install -r requirements.txt

# pip install 실행
# RUN pip install -r requirements.txt

# 환경변수 설정
# ENV FLASK_APP flask
ENV FLASK_APP "opener"

# entrypoint
# ENTRYPOINT ["flask"]

# 컨테이너 실행 시 flask run --host 0.0.0.0 실행
# --port 포트번호 => 포트번호 설정가능 기본포트 5000
CMD ["flask", "run", "--host", "0.0.0.0"]