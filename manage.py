
# flask_script = 웹 모듈 밖에서 스크립트 관리해주는 라이브러리
from flask_script import Server, Manager
from app import create_app

app = create_app()
manager = Manager(app)
manager.add_command(
    "runserver",
    Server(host='0.0.0.0', port=5000, use_debugger=True)
)

if __name__ == "__main__":
    manager.run()
