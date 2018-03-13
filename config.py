#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: config.example
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-05-20 12:31:46 (CST)
# Last Update: 星期日 2018-02-11 15:43:26 (CST)
#          By: jianglin
# Description:
# **************************************************************************
from datetime import timedelta
from os import path, pardir

DEBUG = True
SECRET_KEY = 'secret key'
SECURITY_PASSWORD_SALT = 'you will never guess'
SECRET_KEY_SALT = 'you will never guess'

# avatar upload directory
AVATAR_FOLDER = path.join(path.abspath(path.dirname(__file__)), 'avatar')
# avatar generate range
AVATAR_RANGE = [122, 512]

# for development use localhost:5000
# for production use xxx.com
# SERVER_NAME = 'localhost:5000'

# remember me to save cookies
PERMANENT_SESSION_LIFETIME = timedelta(days=3)
REMEMBER_COOKIE_DURATION = timedelta(days=3)
ONLINE_LAST_MINUTES = 5

# You want show how many topics per page
PER_PAGE = 12

# Use cache
CACHE_TYPE = 'simple'
CACHE_DEFAULT_TIMEOUT = 60
CACHE_KEY_PREFIX = 'cache:'
CACHE_REDIS_HOST = '127.0.0.1'
CACHE_REDIS_PORT = '6379'
CACHE_REDIS_PASSWORD = 'bbsredis'
CACHE_REDIS_DB = 2

# Redis setting
REDIS = {'db': 1, 'password': 'bbsredis', 'decode_responses': True}

# some middleware
MIDDLEWARE = ['forums.common.middleware.GlobalMiddleware',
              'forums.common.middleware.OnlineMiddleware']

# Mail such as qq
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 25
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = "your email"
MAIL_PASSWORD = "your password"
MAIL_DEFAULT_SENDER = 'your email'
# MAIL_SUPPRESS_SEND = True

SERVER_NAME = '127.0.0.1:8001'
SUBDOMAIN = {'forums': False, 'docs': True}

# logging setting
LOGGING = {
    'info': 'logs/info.log',
    'error': 'logs/error.log',
    'send_mail': False,
    'toaddrs': [],
    'subject': 'Your Application Failed',
    'formatter': '''
            Message type:       %(levelname)s
            Location:           %(pathname)s:%(lineno)d
            Module:             %(module)s
            Function:           %(funcName)s
            Time:               %(asctime)s

            Message:

            %(message)s
            '''
}

# Sql
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/your_db'
# SQLALCHEMY_DATABASE_URI = 'sqlite://'+path.join(BASE_DB_PATH, 'test.db')
SQLALCHEMY_TRACK_MODIFICATIONS=False
MSEARCH_INDEX_NAME = 'whoosh_index'
MSEARCH_BACKEND = 'whoosh'
# SQLALCHEMY_ECHO = True
# SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
SQLALCHEMY_DATABASE_URI = 'mysql://root:toor@localhost/bbsdb'

# Locale
LANGUAGES = {'en': 'English', 'zh': 'Chinese'}
SITE = {'title': 'Honmaple', 'description': '爱生活，更爱自由', 'avatar': ''}

