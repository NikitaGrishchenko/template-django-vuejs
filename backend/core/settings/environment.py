import os

import environ

from .common import ENV_FILE

env = environ.Env(
    DEBUG=(bool, True)
)

if os.path.isfile(ENV_FILE):
    env.read_env(ENV_FILE)
