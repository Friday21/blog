#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Friday'
SITENAME = u'\u6211\u7684\u7cbe\u795e\u5bb6\u56ed'
SITEURL = 'http://localhost:80'
SEARCH_URL = '/search.html'
PATH = 'content'

STATIC_PATHS = ['images']
TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'
THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME = 'cerulean'
# BOOTSTRAP_NAVBAR_INVERSE = True
BANNER = 'images/banner.PNG'
DUOSHUO_SITENAME = 'fridayhaohao'
CUSTOM_CSS = 'extra/custom.css'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
more = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('facebook', 'https://www.facebook.com/li.dongyong?ref=bookmarks'),
          ('twitter','https://twitter.com/dongyongli'),
          ('github','https://github.com/Friday21'),)

DEFAULT_PAGINATION = 5

MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra','headerid']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
# 插件
PLUGIN_PATH = u'pelican-plugins'
PLUGINS = ['sitemap', 'related_posts', 'random_article',
           'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code','tag_cloud']

# 配置sitemap插件
SITEMAP = {
     "format": "xml",
     "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
        },
     "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
        }
     }
RANDOM = 'random.html'
RELATED_POSTS_MAX = 10
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'tags')
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'
TAGS_URL = 'tags.html'
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = True

GOOGLE_CUSTOM_SEARCH_NAVBAR = True
