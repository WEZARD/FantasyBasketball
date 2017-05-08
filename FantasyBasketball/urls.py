from django.conf.urls import url
from django.contrib import admin
from apps.message import views
import settings

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^form/$', views.getform, name='go_form'),
    url(r'^$', views.index, name='home'),
    url(r'^log_in/$', views.log_in, name='log_in'),
    url(r'^register/$', views.register, name='register'),
    url(r'^select_team/$', views.select_team, name='select_team'),
    url(r'^user_center/info/$', views.usercenter_info, name='user_info'),
    url(r'^user_center/history/$', views.usercenter_history, name='user_history'),
    url(r'^user_center/rules/$', views.usercenter_rules, name='user_rules')
]
