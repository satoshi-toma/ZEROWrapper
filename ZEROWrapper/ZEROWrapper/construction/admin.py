from django.contrib import admin
from .models import SubArea, Construction
from .models import SubArea, Construction


# 管理者画面に表示するテーブルの指定
@admin.register(SubArea)
class SubAreaAdmin(admin.ModelAdmin):

    # 検索項目の指定
    search_fields = ('name',)


# 管理者画面に表示するテーブルの指定
@admin.register(Construction)
class ConstructionAdmin(admin.ModelAdmin):

    # 一覧画面で表示する
    list_display = ('id', 'person_in_charge', 'subarea', 'process', 'quality_check', 'quality_check_person', 'safety_check', 'work_start', 'work_end', 'note')

    # 詳細内容へリンクフィールドの指定
    list_display_links = ('id',)

    # 検索項目の指定
    search_fields = ('person_in_charge__username', 'subarea__name', 'process')

    # 検索の絞り込み方法の指定
    list_filter = ('subarea',)

    # 管理画面で編集可能な項目の指定
    list_editable = ('quality_check_person',)