from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__) # 实例化flask
app.debug = True# 开启调试模式
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://admin:123456@192.168.195.131/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = "f9807cc8472b4dc493a94b84cedc5f63"

# 定义db对象，实例化SQLAlchemy，传入app对象
db = SQLAlchemy(app)

from app.home import home as home_blueprint  #导入
from app.admin import admin as admin_blueprint

#注册蓝图
app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint,url_prefix='/admin')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
