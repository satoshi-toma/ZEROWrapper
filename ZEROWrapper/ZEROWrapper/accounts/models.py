from __future__ import division
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin,
)
from django.urls import reverse_lazy


# ユーザー/管理者作成のカスタマイズ
class UserManager(BaseUserManager):
    # ユーザー作成の設定
    def create_user(self, username, employee_number, department, division, group, phone_number, email, password=None):
        if not username:
            raise ValueError('Please Enter username')        
        elif not email:
            raise ValueError('Please Enter Email')
        
        user = self.model(
            username=username,
            employee_number=employee_number,
            department=department,
            division=division,
            group=group,
            phone_number=phone_number,
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 管理者作成の設定
    def create_superuser(self, username, employee_number, department, division, group, phone_number, email, password=None):
        user = self.model(
            username=username,
            employee_number=employee_number,
            department=department,
            division=division,
            group=group,
            phone_number=phone_number,
            email=email,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# ユーザモデル
class User(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField(max_length=100, help_text='例) 當間 郷史', verbose_name='氏名')
    employee_number = models.PositiveIntegerField(help_text='*TMC従業員は必須', verbose_name='従業員番号' ,blank=True, null=True)
    department = models.CharField(max_length=100, help_text='例) 高岡工場車体部', verbose_name='部')
    division = models.CharField(max_length=100, help_text='例) 技術員室/1ボデー課', verbose_name='室/課', blank=True, null=True)
    group = models.CharField(max_length=100, help_text='例) 1ボデーGr/KT911組', verbose_name='グループ/組', blank=True, null=True)
    phone_number = models.PositiveIntegerField(help_text='例) 数字のみ。ハイフン(-)なしで記入', verbose_name='電話番号')
    email = models.EmailField(max_length=255, unique=True, help_text='first_last@mail.toyota.co.jp', verbose_name='メールアドレス')
    is_active = models.BooleanField(default=True, verbose_name='アカウント有効')
    is_staff = models.BooleanField(default=False, verbose_name='管理画面アクセス可能')
    is_superuser = models.BooleanField(default=False, verbose_name='管理者権限')

    # ログイン時に入力する項目
    USERNAME_FIELD = 'email'
    # 管理者作成時に設定する項目
    REQUIRED_FIELDS = ['username', 'employee_number', 'department', 'division', 'group', 'phone_number'] # スーパーユーザ作成時に入力値
    # カスタマイズ方法を記載したクラスを指定
    objects = UserManager()

    # 管理画面での表記(admin.pyでlist_displayで表記定義しているのでそれが優先される)
    def __str__(self):
        return self.username + '_' + self.department + '_' + str(self.phone_number)

    def get_absolute_url(self):
        return reverse_lazy('accounts:home')

    class Meta:
        # 管理画面での表示方法の指定
        verbose_name_plural = 'ユーザーリスト'