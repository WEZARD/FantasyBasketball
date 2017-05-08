# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from apps.message import views as message_views
from apps.game import views as game_views
from apps.users import views as users_views
from apps.users.views import LoginView
import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),  # 后台管理页面
    url(r'^form/$', message_views.getform, name='go_form'),  # 测试页面
    url(r'^$', game_views.index, name='home'),  # 游戏大厅页面
    url(r'^log_in/$', LoginView.as_view(), name='log_in'),  # 用户登录页面
    url(r'^register/$', users_views.register, name='register'),  # 用户注册页面
    url(r'^select_team/$', game_views.select_team, name='select_team'),  # 组建队伍页面
    url(r'^user_center/info/$', users_views.usercenter_info, name='user_info'),  # 用户中心信息页面
    url(r'^user_center/history/$', users_views.usercenter_history, name='user_history'),  # 用户中心游戏历史页面
    url(r'^user_center/rules/$', users_views.usercenter_rules, name='user_rules')  # 用户中心游戏规则页面
]
