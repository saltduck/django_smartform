from django.conf.urls.defaults import *

urlpatterns = patterns('sample.views',
    # Example:
    # (r'^django_smartform/', include('django_smartform.foo.urls')),
    (r'^normal/$', 'sample1'),
    (r'^ajax/$', 'sample2'),
    (r'^ok/$', 'ok'),

)
