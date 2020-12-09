from django.conf.urls import url 
from app import views, views2
 
urlpatterns = [ 
    # url(r'^api/tutorials$', views.tutorial_list),
    # url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    # url(r'^api/tutorials/published$', views.tutorial_list_published)
    url(r'^api/login$', views.login_request),
    url(r'^api/register_doctor$', views.register_doctor),
    url(r'^api/register_establishment$', views.register_establishment),
    url(r'^api/get_code$', views.get_qr_code),
    url(r'^api/logout$', views.logout_request),
    url(r'^api/get_device_id$', views.get_device_id),
    url(r'^api/sendMobileScan$', views.handle_scanned_request),
    url(r'^api/contactServer$', views2.handle_app_launched),
    url(r'^api/insert_users_for_dev$', views2.insert_users_for_dev),
    url(r'^api/get_list$', views.get_qr_list),
]
