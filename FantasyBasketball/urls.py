# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from game.views import HomeView, TeamView
from users import views as users_views
from users.views import LoginView, RegisterView, UserInfoView, UserRulesView, UserHistoryView

urlpatterns = [
    url(r'^admin/', admin.site.urls),  # 后台管理页面
    # url(r'^captcha/', include('captcha.urls')),  # 验证码
    url(r'^$', LoginView.as_view(), name='log_in'),  # 用户登录界面(主页)
    url(r'^register/$', RegisterView.as_view(), name='register'),  # 用户注册页面
    # url(r'^register/$', users_views.register, name='register'),  # 用户注册页面
    url(r'^user_center/info/$', UserInfoView.as_view(), name='user_info'),  # 用户中心信息页面
    url(r'^user_center/history/$', UserHistoryView.as_view(), name='user_history'),  # 用户中心游戏历史页面
    url(r'^user_center/rules/$', UserRulesView.as_view(), name='user_rules'),  # 用户中心游戏规则页面
    # url(r'^user_center/rules/$', users_views.usercenter_rules, name='user_rules'),  # 用户中心游戏规则页面
    url(r'^home$', HomeView.as_view(), name='home'),  # 游戏大厅页面
    url(r'^select_team/$', TeamView.as_view(), name='select_team'),  # 组建队伍页面
    # url(r'^$', users_views.test, name='log_in')  # 测试
]
