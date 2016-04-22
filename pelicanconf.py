#!/usr/bin/env python
# coding: utf-8
from datetime import date

# Author info
AUTHOR = 'Evandro Myller'
SITENAME = 'Evandro Myller\'s blog'
SITEURL = ''

# Content settings
PATH = 'content'
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 10
THEME = 'themes/Flex'

# Feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = []

# Social widget
SOCIAL = [
    ('github', 'https://github.com/emyller'),
    ('twitter', 'https://twitter.com/eMyller'),
    ('linkedin', 'https://www.linkedin.com/in/emyller'),
    ('stack-overflow', 'http://stackoverflow.com/users/307511/emyller'),
]

# Theme-specific settings
SITETITLE = AUTHOR
SITESUBTITLE = 'Python Engineer, World Explorer'
SITELOGO = '//s.gravatar.com/avatar/1820571c2e448ff37c5843d4c8e007c3?s=200'
COPYRIGHT_YEAR = date.today().year
MAIN_MENU = True
FAVICON = SITELOGO
DISQUS_SITENAME = 'emyller'
GOOGLE_ANALYTICS = 'UA-76793413-1'
