"""
Staging settings for PharmaLink Backend
This file ensures staging environment mirrors production configuration
"""

import os
import dj_database_url
from .settings import *

# Override DEBUG for staging
DEBUG = False

# Staging-specific database configuration
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600
    )
}

# Staging-specific allowed hosts
ALLOWED_HOSTS = [
    'pharmalink-backend-staging.onrender.com',
    '127.0.0.1',
    'localhost'
]

# Staging-specific logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'staging.log',
            'formatter': 'verbose',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
        'apps': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

# Staging-specific CORS settings (more restrictive than development)
CORS_ALLOWED_ORIGINS = [
    "https://pharmalink-frontend-staging.onrender.com",
    "http://localhost:3000",  # For local frontend testing
]

# Staging-specific security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Staging-specific email configuration (if needed)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Staging-specific cache configuration
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'staging-cache',
    }
}

# Staging-specific session configuration
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True

# Staging-specific static files configuration
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Staging-specific media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Staging-specific admin configuration
ADMIN_URL = 'staging-admin/'

# Staging-specific API configuration
REST_FRAMEWORK.update({
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
})

# Staging-specific JWT configuration
from datetime import timedelta

SIMPLE_JWT.update({
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
})

# Staging-specific database connection settings
DATABASES['default'].update({
    'CONN_MAX_AGE': 600,
    'OPTIONS': {
        'connect_timeout': 10,
        'options': '-c default_transaction_isolation=read_committed'
    }
})

# Staging-specific environment validation
def validate_staging_environment():
    """Validate that staging environment is properly configured"""
    required_env_vars = [
        'SECRET_KEY',
        'DATABASE_URL',
    ]
    
    missing_vars = [var for var in required_env_vars if not os.environ.get(var)]
    
    if missing_vars:
        raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
    
    # Validate database URL format
    db_url = os.environ.get('DATABASE_URL')
    if db_url and not db_url.startswith('postgresql://'):
        raise ValueError("DATABASE_URL must be a PostgreSQL connection string for staging")

# Run validation on startup
validate_staging_environment()
