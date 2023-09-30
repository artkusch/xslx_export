from django.contrib import admin
from django.urls import path
from Robots.views import export_data_to_xlsx

urlpatterns = [
    path('admin/', admin.site.urls),
    path('export', export_data_to_xlsx, name='export-xlsx'),

]
