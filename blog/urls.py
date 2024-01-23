from django.urls import path
from .views import (index, contact, computers, mans_clothes, womans_clothes, addsdetailview, lapsdetailview,
                    laptopsdetailview, LapCreateView, lapsDetail, LapDeleteView, LapUpdateView)

urlpatterns = [
    path('computers/', computers, name='computers'),
    path('contact/', contact, name='contact'),
    path('mans_clothes/', mans_clothes, name='mans_clothes'),
    path('', index, name='index'),
    path('womans_clothes/', womans_clothes, name='womans_clothes'),
    path('adds/<int:id>', addsdetailview, name='addsDetail'),
    path('laps/<int:id>', lapsdetailview, name='lapsDetail'),
    path('laptops/<int:id>', laptopsdetailview, name='laptopsDetail'),
    path("laps/create/", LapCreateView.as_view(), name="laps_create"),
    path('laps/edit/<slug>/', LapUpdateView.as_view(),name="lapsUpdate",),
    path('laps/delete/<slug>/',LapDeleteView.as_view(), name = 'lapsDelete'),
    path('laps/<slug:laps>/',lapsDetail, name='lapsDetail'),

]





































