"""Local settings based on dev. Override as you need"""
from syncables.conf.dev.settings import *

DATABASE_ENGINE = 'mysql'
DATABASE_NAME = 'djsyncables'
DATABASE_USER = 'syncables'
DATABASE_PASSWORD = ''
DATABASE_HOST ='192.168.0.108'

