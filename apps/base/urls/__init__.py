"""uRLs para base
"""
# Librerias Django
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

# Librerias en carpetas locales
from ..views import (
    ChangePasswordForm, CustomerListView, UserDeleteView, DoChangePassword,
    Install, ProviderListView, UpdateBaseConfigView, UserCreateView,
    UserDetailView, UserListView, UserUpdateView)
from ..views.base_config import LoadData
from ..views.cron import (
    CronCreateView, CronDetailView, CronListView, CronUpdateView, CronDeleteView)
from ..views.home import erp_home
from ..views.log import (
    LogDeleteView, LogCreateView, LogDetailView, LogListView, LogUpdateView)
from ..views.post import (
    PostDeleteView, PostCreateView, PostDetailView, PostListView, PostUpdateView)
from ..views.product_category import (
    ProductCategoryDeleteView, ProductCategoryCreateView,
    ProductCategoryDetailView, ProductCategoryListView,
    ProductCategoryUpdateView)
from ..views.product_webcategory import (
    ProductWebCategoryDeleteView, ProductWebCategoryCreateView,
    ProductWebCategoryDetailView, ProductWebCategoryListView,
    ProductWebCategoryUpdateView)
from ..views.website_config import UpdateWebsiteConfigView

app_name = 'base'

urlpatterns = [
    path('', erp_home, name='home'),
    path('install', Install, name='install'),
    # path('install-erp', InstallPyERP, name='install-erp'),


    path(
        'logout/',
        auth_views.LogoutView.as_view(template_name='base/login.html'),
        name='logout'
    ),
    # path('logoutmodal/', LogOutModalView.as_view(), name='logout-modal'),
    path('config/<int:pk>', UpdateBaseConfigView.as_view(), name='base-config'),
    path('load-data', LoadData, name='load-data'),

    path('website-config/<int:pk>', UpdateWebsiteConfigView.as_view(), name='website-config'),

    path('users', UserListView.as_view(), name='users'),
    path('user/add/', UserCreateView.as_view(), name='user-add'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('user/<int:pk>/update', UserUpdateView.as_view(), name='user-update'),
    path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
    path('user/change-password/<int:pk>', ChangePasswordForm, name='password-change'),
    path('user/change-password-confirm/<int:pk>', DoChangePassword, name='do-change-password'),

    path('partners', CustomerListView.as_view(), name='partners'),
    path('provider', ProviderListView.as_view(), name='provider'),

    path('product-category', ProductCategoryListView.as_view(), name='product-category'),
    path('product-category/add/', ProductCategoryCreateView.as_view(), name='product-category-add'),
    path('product-category/<int:pk>/', ProductCategoryDetailView.as_view(), name='product-category-detail'),
    path('product-category/<int:pk>/update', ProductCategoryUpdateView.as_view(), name='product-category-update'),
    path('product-category/<int:pk>/delete/', ProductCategoryDeleteView.as_view(), name='product-category-delete'),

    path('product-webcategory', ProductWebCategoryListView.as_view(), name='product-webcategory'),
    path('product-webcategory/add/', ProductWebCategoryCreateView.as_view(), name='product-webcategory-add'),
    path('product-webcategory/<int:pk>/', ProductWebCategoryDetailView.as_view(), name='product-webcategory-detail'),
    path('product-webcategory/<int:pk>/update', ProductWebCategoryUpdateView.as_view(), name='product-webcategory-update'),
    path('product-webcategory/<int:pk>/delete/', ProductWebCategoryDeleteView.as_view(), name='product-webcategory-delete'),

    path('logs', LogListView.as_view(), name='logs'),
    path('log/add/', LogCreateView.as_view(), name='log-add'),
    path('log/<int:pk>/', LogDetailView.as_view(), name='log-detail'),
    path('log/<int:pk>/update', LogUpdateView.as_view(), name='log-update'),
    path('log/<int:pk>/delete/', LogDeleteView.as_view(), name='log-delete'),

    path('crons', CronListView.as_view(), name='crons'),
    path('cron/add/', CronCreateView.as_view(), name='cron-add'),
    path('cron/<int:pk>/', CronDetailView.as_view(), name='cron-detail'),
    path('cron/<int:pk>/update', CronUpdateView.as_view(), name='cron-update'),
    path('cron/<int:pk>/delete/', CronDeleteView.as_view(), name='cron-delete'),

    path('post', PostListView.as_view(), name='post-backend'),
    path('post/add/', PostCreateView.as_view(), name='post-add'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),


    # ============================ New URLs ============================ #
    path('', include('apps.base.urls.usercustom')),
    path('attribute/', include('apps.base.urls.attribute')),
    path('bi/', include('apps.base.urls.bi')),
    path('channel/', include('apps.base.urls.channel')),
    path('comment/', include('apps.base.urls.comment')),
    path('company/', include('apps.base.urls.company')),
    path('country/', include('apps.base.urls.country')),
    path('currency/', include('apps.base.urls.currency')),
    path('faq/', include('apps.base.urls.faq')),
    path('image/', include('apps.base.urls.image')),
    path('meta/', include('apps.base.urls.meta')),
    path('page/', include('apps.base.urls.page')),
    path('parameter/', include('apps.base.urls.parameter')),
    path('partner/', include('apps.base.urls.partner')),
    path('plugin/', include('apps.base.urls.plugin')),
    path('product/', include('apps.base.urls.product')),
    path('product_brand/', include('apps.base.urls.product_brand')),
    path('product_category_uom/', include('apps.base.urls.product_category_uom')),
    path('sequence/', include('apps.base.urls.sequence')),
    path('shop/', include('apps.base.urls.shop')),
    path('tag/', include('apps.base.urls.tag')),
    path('tax/', include('apps.base.urls.tax')),
    path('uom/', include('apps.base.urls.uom')),
    path('variant/', include('apps.base.urls.variant')),
    path('wparameter/', include('apps.base.urls.wparameter')),
    path('wpayment/', include('apps.base.urls.wpayment')),
    path('email/', include('apps.base.urls.email')),
    path('file/', include('apps.base.urls.file')),
    path('message/', include('apps.base.urls.message')),
    path('note/', include('apps.base.urls.note')),
    path('event/', include('apps.base.urls.event')),
    path('menu/', include('apps.base.urls.menu')),
]
