from django.urls import path
from . import views
from employeeapp.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

#  Django
urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload-employee'),
    path('update/<int:employee_id>', views.update_employee),
    path('delete/<int:employee_id>', views.delete_employee)
]

#
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)


'''x-html has doctype manadatory while html doesn't require you to declare doctype
xmlns type is mandatory in html
html, head, body and title is mandatory
must be properly nested
must be properly closed
must be used in lowercase

'''
