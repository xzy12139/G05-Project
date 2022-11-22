from flask import Flask
import config
from exts import db
from blueprints.auth import bp as auth_bp
from blueprints.search import bp as search_bp
from blueprints.result import bp as result_bp

app = Flask(__name__)
# 绑定配置文件
app.config.from_object(config)

db.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(search_bp)
app.register_blueprint(result_bp)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
