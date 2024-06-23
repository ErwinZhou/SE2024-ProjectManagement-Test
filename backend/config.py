#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Project ：GitHub 
@File    ：config.py
@IDE     ：PyCharm 
@Author  ：ErwinZhou
@Date    ：2024/5/10 23:14 
"""
# TODO: Use hierarchical toml file to store configs
from datetime import timedelta
import os
from urllib.parse import quote

password = '53468896Aa@'
encoded_password = quote(password)


DATABASE_URL = f"mysql://root:{encoded_password}@localhost:3306/softwareengineering"
# Security Settings
SECRETE_KEY = 'YuchenZhouNB'
JWT_ENCODE_ALGORITHM = 'HS256'
TOKEN_EXPIRE_MINUTES = timedelta(minutes=1800)


# xwf
# DATABASE_URL = 'mysql://root:@127.0.0.1:3306/softwareengineering'
# JWT_ENCODE_ALGORITHM = 'HS256'
# TOKEN_EXPIRE_MINUTES = timedelta(minutes=1800)