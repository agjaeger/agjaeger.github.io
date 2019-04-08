#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import entities

AUTHOR = 'Alexander Jaeger'
SITENAME = "Alexander Jaeger"
SITEURL = 'http://localhost::8000/'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'
LOAD_CONTENT_CACHE = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = (('blog', '/'),
         ('projects', 'projects/'),
         ('interesting links', 'coollinks/'),
         ('research notes', 'researchnotes/'),
         ('about me', 'aboutme/'),
    )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "theme"

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["jinja2content", "sitemap"]
STATIC_PATHS = ['images']

