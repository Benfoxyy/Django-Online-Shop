from core.settings import *
import socket

# Additional Installed Apps
INSTALLED_APPS += [
    "debug_toolbar",
    "drf_yasg",
]

# Additional Middleware
MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]


hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + [
    "127.0.0.1",
    "10.0.2.2",
]

SITE_ID = 1
