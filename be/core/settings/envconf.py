import os
import sys

_CONFIG_PARAMS = [
    ('DEBUG', bool, '0'),
    ('LOG_LEVEL', str, 'INFO'),
    ('DJANGO_SECRET_KEY', str, None),
    # Postgres Database
    ('BM_DB_HOST', str, None),
    ('BM_DB_PORT', int, 5432),
    ('BM_DB_NAME', str, None),
    ('BM_DB_USER', str, None),
    ('BM_DB_PASSWORD', str, None)
]

_module = sys.modules[__name__]

for config_param_name, ctype, default in _CONFIG_PARAMS:
    value = os.environ.get(config_param_name, default)

    if value is None:
        raise RuntimeError('Missing required parameter: ' + config_param_name)

    if type == bool:
        value = value == '1'
    else:
        value = ctype(value)

    setattr(_module, config_param_name, value)
