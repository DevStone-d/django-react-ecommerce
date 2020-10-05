from django.conf import settings
from django_hosts import patterns, host

import api.urls

# host_patterns = patterns('',
#     host(r'www', settings.ROOT_URLCONF, name='www'),
#     host(r'api', api.urls , name='api'),
#     # host(r'(\w+)', 'path.to.custom_urls', name='wildcard'),
# )

host_patterns = patterns(
    '',
    host(r"api", "api.urls", name="api"),
    #host(r"admin", "server.admin_urls", name="admin"),
    host("", settings.ROOT_URLCONF , name="home"),  # ROOT_URLCONF = 'devstone.urls'
)