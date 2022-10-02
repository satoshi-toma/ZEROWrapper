from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import AuthenticationForm


# ユーザーモデルを取得し、インスタンス化
User = get_user_model()

class UserRegistForm(forms.ModelForm):
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput)

    # ユーザー作成時に入力する項目
    class Meta:
        model = User
        fields = ('username', 'employee_number', 'department', 'division',
         'group', 'phone_number', 'email', 'password')

    # パスワードが一致しているかの確認
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('パスワードが一致しません。再入力してください。')

    # パスワードのバリデーションとパスワードの暗号化
    def save(self, commit=False):
        user = super().save(commit=False)
        #TODO:バリデーションが表示されない
        validate_password(self.cleaned_data['password'], user)
        user.set_password(self.cleaned_data.get('password'))
        user.save()
        return user


# ユーザー修正
class UserModifyForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        # 修正時に設定する項目　 
        fields = ('username', 'employee_number', 'department', 'division',
         'group', 'phone_number', 'email', 'password', 'is_staff', 'is_active', 'is_superuser')

    # ユーザーのパスワードを変更できないように初期値を返す
    def clean_password(self):
        return self.initial['password']


# 
# class UserLoginForm(forms.Form):
#     email = forms.EmailField(label='メールアドレス')
#     password = forms.CharField(label='パスワード', widget=forms.PasswordInput())

class UserLoginForm(AuthenticationForm):
    # ユーザモデルのUSERNAME_FIELD(一意に定めるフィールドを指定　)
    username = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    keep_login_session = forms.BooleanField(label='ログイン状態を保持', required=False)