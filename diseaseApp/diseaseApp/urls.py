from django.urls import path
from .views import (
    main_page,
    CountryListView, CountryCreateView, CountryUpdateView, CountryDeleteView
)

urlpatterns = [
    path('', main_page, name='main_page'),
    path('country/', CountryListView.as_view(), name='country_list'),
    path('country/create/', CountryCreateView.as_view(), name='country_create'),
    path('country/<pk>/update/', CountryUpdateView.as_view(), name='country_update'),
    path('country/<pk>/delete/', CountryDeleteView.as_view(), name='country_delete'),
]
