from __future__ import division
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import UserModifyForm, UserRegistForm

User = get_user_model()

# ユーザーモデルの管理者画面でのカスタマイズ
class CustomizeUserAdmin(UserAdmin):
    form = UserModifyForm  # ユーザ編集画面で使うForm
    add_form = UserRegistForm  # ユーザ作成画面

    # 一覧画面で表示する
    list_display = ('id', 'username', 'department', 'phone_number', 'email', 'is_active', 'is_superuser')

    # 詳細内容へリンクフィールドの指定
    list_display_links = ('username',)

    # 検索項目の指定
    search_fields = ('username', 'employee_number', 'department', 'division', 'group', 'phone_number', 'email')

    # 検索の絞り込み方法の指定
    list_filter = ('department', 'division', 'group',)

    # 管理画面で編集可能な項目の指定
    list_editable = ('is_active',)

    # ユーザ修正画面で表示する要素
    fieldsets = (
        ('ユーザ情報', {'fields': ('username', 'password', 'employee_number', 'department', 'division',
         'group', 'phone_number', 'email',)}),
         ('パーミッション', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    
    # ユーザ追加画面で表示する要素
    add_fieldsets = (
        ('ユーザ情報', {'fields': ('username', 'password', 'confirm_password', 'employee_number', 'department', 'division',
         'group', 'phone_number', 'email',)}),
    ) # タプルの1つの場合のカンマを忘れないように


# 管理者画面に表示するテーブルの指定
admin.site.register(User, CustomizeUserAdmin)