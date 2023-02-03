# 플라스크 APP 전체의 구조와 설정들을 주입해주는 곳
from flask import Flask, jsonify
from config import flask_config
from router import auth


# Flask를 매개변수로 받음
def register_router(flask_app: Flask):
    # router들을 등록 해주는 곳
    from router.auth.login import login
    from router.review.review import review

    flask_app.register_blueprint(login)
    flask_app.register_blueprint(review)

    # 모든 플라스크 서비스 공통 request 처리 전
    @flask_app.before_request
    def before_my_request():
        print("before my request")

    # 모든 플라스크 서비스 공통 request 처리 후
    @flask_app.after_request
    def after_my_request(res):
        print("after my request", res.status_code)
        return res


# config 파일 불러오고 앱 반환
def create_app():
    app = Flask(__name__)
    app.config.from_object((get_flask_env()))
    register_router(app)
    return app


# 환경변수에 따라 config나누기
def get_flask_env():
    if (flask_config.Config.ENV == "prod"):
        return 'config.flask_config.prodConfig'
    elif (flask_config.Config.ENV == "dev"):
        return 'config.flask_config.devConfig'
