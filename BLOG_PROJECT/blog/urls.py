from django.urls import patterns, include, url
from blogapp import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = pattern('',
    # Examples:
    # url(r'^$', 'simple_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^addblog/', views.createBlog, name ="create"),
    url(r'^',views.index),
    url(r'^admin/', include(admin.site.urls)),

)
