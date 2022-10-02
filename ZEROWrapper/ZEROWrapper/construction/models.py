from tabnanny import verbose
from django import db
from django.db import models
from accounts.models import User

class SubArea(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    class Meta:
        db_table = 'subarea'
        verbose_name_plural = 'サブリスト'

    def __str__(self):
        return self.name


class Construction(models.Model):
    danger_choices = (
        ('挟まれ', '挟まれ/Actuator'),
        ('重量物', '重量物/Block'), 
        ('車両', '車両/Car'), 
        ('転落', '転落/Drop'), 
        ('感電', '感電/Electric Shock'), 
        ('火災', '火災/Fire'), 
        )

    quality_choices = (
        ('溶接', '溶接'),
        ('面', '面'),
        ('仕様', '仕様'),
        ('錆', '錆'),
        ('板合せ', '精度'),
        ('組付', '組付'),
        ('打刻', '打刻'),
        ('その他', 'その他'),
    )
    
    simple_choices = (
        ('○', '○'),
    )

    status_choices = (
        ('工事前', '工事前'),
        ('進行中', '進行中'),
        ('完了', '完了'),
    )

    person_in_charge = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name='計画者'
    )
    subarea = models.ForeignKey(
        SubArea, on_delete=models.PROTECT, verbose_name='サブエリア'
    )
    process = models.CharField(max_length=100, verbose_name='工程')
    construction_name = models.CharField(max_length=255, verbose_name='工事名称')
    danger_list = models.CharField(max_length=30, verbose_name='危険項目', choices=danger_choices)
    environmental_risk = models.CharField(max_length=100, verbose_name='環境リスク', blank=True, null=True)
    work_content = models.CharField(max_length=255, verbose_name='作業内容')
    work_company = models.CharField(max_length=100, verbose_name='作業部署/仕入先')
    work_person = models.CharField(max_length=20, verbose_name='工事担当')
    quality_check = models.CharField(max_length=20, verbose_name='品質確認項目', choices=quality_choices, blank=True, null=True)
    quality_check_person = models.CharField(max_length=20, verbose_name='品質確認担当', blank=True, null=True)
    safety_check = models.CharField(max_length=10, verbose_name='安全立会', choices=simple_choices, blank=True, null=True)
    safety_check_person = models.CharField(max_length=20, verbose_name='安全立会担当', blank=True, null=True)
    work_start = models.DateTimeField(verbose_name='開始日時')
    work_end = models.DateTimeField(verbose_name='終了日時')
    note = models.TextField(max_length=1000, verbose_name='依頼事項/備考', blank=True, null=True)
    dummy = models.CharField(max_length=10, verbose_name='生産指示ダミー', choices=simple_choices, blank=True, null=True)
    goguchi_change = models.CharField(max_length=10, verbose_name='号口変化点', choices=simple_choices, blank=True, null=True)
    seijun_change = models.CharField(max_length=10, verbose_name='生準変化点', choices=simple_choices, blank=True, null=True)
    status = models.CharField(max_length=10, verbose_name='進捗', choices=status_choices, blank=True, null=True)

    class Meta:
        db_table = 'construction'
        verbose_name_plural = '工事リスト'
        ordering = ('work_start',)

    def __str__(self):
        return str(self.work_start) + '-' + self.construction_name + '-' + str(self.person_in_charge)