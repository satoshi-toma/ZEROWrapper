from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

import os
from .models import Construction


class ConstructionListView(ListView):
    model = Construction
    template_name = os.path.join('construction', 'construction_list.html')

    # フィルター機能を追加
    def get_queryset(self):
        query = super().get_queryset()
        subarea_name = self.request.GET.get('subarea_name', None)  # 何もない場合はNone
        if subarea_name:
            query = query.filter(
                subarea__name=subarea_name,
            )
        
        order_by_work_start = self.request.GET.get('order_by_work_start', 0)  # 何もない場合は0
        if order_by_work_start == '1':
            query = query.order_by('work_start')
        elif order_by_work_start == '2':
            query = query.order_by('-work_start')
        
        date_from = str(self.request.GET.get('date_from', None)) + str(' 00:00:00.000000')  # 時間の追加は同一日付が表示されない不具合対策
        date_to = str(self.request.GET.get('date_to', None)) + str(' 23:59:59.999999') # 時間の追加は同一日付が表示されない不具合対策
        if date_from and date_to:
            query = query.filter(work_start__gte=date_from, work_end__lte=date_to)
        elif date_from:
            query = query.filter(work_start__gte=date_from)
        elif date_from:
            query = query.filter(work_end__lte=date_to)
        else:
            query = query.filter(work_start__isnull=True, work_end__isnull=True)
        return query

    # フィルター検索欄に検索文字、昇降順を残す
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subarea_name'] = self.request.GET.get('subarea_name', '') # 検索されない場合は空白を返す
        order_by_work_start = self.request.GET.get('order_by_work_start', 0)
        if order_by_work_start == '1':
            context['ascending'] = True
        elif order_by_work_start == '2':
            context['descending'] = True
        context['date_from'] = self.request.GET.get('date_from', '')
        context['date_to'] = self.request.GET.get('date_to', '')
        return context