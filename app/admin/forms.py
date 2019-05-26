from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,ValidationError,Length
from app.models import Admin



class LoginForm(FlaskForm):
    """管理员登录表单"""
    account = StringField(
        label='账号',
        validators=[
            DataRequired('请输入账号！')
        ],
        description='账号',
        #附加选项
        render_kw={
            'class': "form-control",
            'placeholder': "请输入账号",
            #用户必须填
            'required': "required"
        }
    )
    pwd = PasswordField(
        label='密码',
        validators=[
            DataRequired('请输入密码！'),
            Length(min=3,max=15,message="输入的密码过短")
        ],
        description='密码',
        render_kw={
            'class': "form-control",
            'placeholder': "请输入密码",
            'required': "required"
        }
    )
    submit = SubmitField(
        label='登录',
        render_kw={
            'class': "btn btn-primary btn-block btn-flat"
        }
    )

    def validate_account(self,field):
        account=field.data
        # print("哈哈哈哈哈哈哈")

        admin_num = Admin.query.filter_by(name=account).count()
        if admin_num == 0:
            raise ValidationError('账号不存在')

class TagForm(FlaskForm):
    name = StringField(
        label='名称',
        validators=[
            DataRequired('标签名称不能为空！')
        ],
        description='标签',
        render_kw={
            'class': "form-control",
            'id': "input_name",
            'placeholder': "请输入标签名称！"
        }
    )
    submit = SubmitField(
        label='添加',
        render_kw={
            'class': "btn btn-primary"
        }
    )
