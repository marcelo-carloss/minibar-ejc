from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtos/', include('produtos.urls')),
    path('pessoas/', include('pessoas.urls')),
    path('vendas/', include('vendas.urls')),
    path('', include('home.urls'))
]
