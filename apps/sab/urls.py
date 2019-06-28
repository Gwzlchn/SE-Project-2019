from django.urls import path
from apps.sab import views

app_name = 'sab'

urlpatterns = [
    path(r'AddToCart/',views.VisitAddToCart),
    path(r'ATResult/',views.VisitATResult),
    path(r'ResetCart/',views.VisitResetCart),
    path(r'CheckCart/',views.VisitCheckCart),
    path(r'CheckResult/',views.VisitCheckResult),
    path(r'Pay/',views.VisitPay),
    #模板url
    path(r'PRecharge/',views.VisitPRecharge),
    path(r'Recharge-Submit/',views.ReturnPPage),
    path(r'ParentPageR/',views.VisitPPageR),
    path(r'view-cart/',views.VisitCart),
    path(r'reset-cart/',views.ResetCart),
    path(r'pay-cart/',views.PayForCart),
]
