from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views, password_validation
from .forms import LoginForm, MyPasswordchangeForm,MyPasswordResetForm,MySetPasswordForm,CustomerProfileForm


urlpatterns = [
    # path('', views.home),
    path('',views.productview.as_view(),name="home"),
    # path('product-detail/', views.product_detail, name='product-detail'),
    path('product-details/<int:pk>',views.productdetailview.as_view(), 
     name='product-detail'),
    # path('cart/', views.add_to_cart, name='add-to-cart'),

    path('minuscart/', views.minuscart, name='minuscart'),
    path('pluscart/', views.pluscart, name='pluscart'),
    path('show_cart/',views.show_cart, name='show_cart'),
    path('add-to-cart/',views.add_to_cart,name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    # path('profile/', views.profile, name='profile'),

    path('profile/',views.ProfileView.as_view(), name='profile'),
    path('profile_img/',views.profile_imgView, name='pic'),

    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),


    path('changepassword/',auth_views.PasswordChangeView.as_view (template_name=
        'app/changepassword.html',form_class=MyPasswordchangeForm,
          success_url='/passwordchangedone/'),name='changepassword'),

    # path('/passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name=
    #     'app/passwordchangedone.html'),name='passwordchangedone'),    
    # 
     path('passwordchangedone/',views.passwordchangedone, 
      name='passwordchangedone'),

     path('password-reset/',auth_views.PasswordResetView.as_view
     (template_name='app/password_reset.html',form_class=MyPasswordResetForm, success_url='/password_reset_confirm/'), 
      name='password-reset'), 
      
      path('password_reset/done/',auth_views.PasswordResetDoneView.as_view
     (template_name='app/password_reset_done.html'), 
      name='password_reset_done'),

       path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view
     (template_name='app/password_reset_confirm.html',form_class=MySetPasswordForm), 
      name='password_reset_confirm'),

      path('password_reset/complete/',auth_views.PasswordResetCompleteView.as_view
     (template_name='app/password_reset_complete.html'), 
      name='password_reset_complete'),
            




    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>',views.mobile, name='mobiledata'),

    path('laptop/', views.laptop, name='laptop'),
    path('laptop/<slug:data>',views.laptop, name='laptopdata'),

    path('topwear/', views.topwear, name='topwear'),
    path('topwear/<slug:data>',views.topwear, name='topweardata'),

    path('bottamwear/', views.bottamwear, name='bottamwear'),
    path('bottamwear/<slug:data>',views.bottamwear, name='bottamweardata'),

    # path('accounts/login/', views.login, name='login'),

    path('accounts/login/', auth_views.LoginView.as_view (template_name='app/login.html' , authentication_form=LoginForm), name='login'),

    path('logout/',auth_views.LogoutView.as_view(next_page='login'), name='logout'),
   
    path("registration/",views.customerRegistrationView.as_view(), name="customerregistration"),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/',views.paymentdone, name='paymentdone'),

    path('search/',views.search, name='search'),

] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
