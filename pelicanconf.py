#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Greg Rolan'
SITENAME = 'AiLECS Lab'
SITESUBTITLE = 'Artificial Intelligence for Law Enforcement and Community Safety<br/> - A collaboration between Monash University and the Australian Federal Police -'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Australia/Melbourne'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
         ('AiLECS @ Monash', 'https://www.monash.edu/it/ailecs'),
        )

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
    'lazy_ol': False 
}

DISPLAY_PAGES_ON_MENU = False

DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = (
  ('About The Lab','/pages/about.html'),
  ('Publications','/pages/publications.html'),
  ('Code','https://github.com/AiLECS'),
  ('Contact','/pages/contact.html')
)

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["tag_cloud"]

#THEME = 'notmyidea'
THEME = './themes/voidy'

######################################################################
# VOIDY
######################################################################
SITETAG = "AiLECS Lab"

BOOTSTRAP_STYLESHEET = 'bootstrap-flatly.css'

# Extra stylesheets, for bootstrap overrides or additional styling.
STYLESHEET_FILES = ("pygment.css", "voidybootstrap.css","tagcloud.css")

# Put taglist at end of articles, and use the default sharing button implementation.
CUSTOM_ARTICLE_FOOTERS = ("taglist.html", "sharing.html", )
CUSTOM_SCRIPTS_ARTICLE = "sharing_scripts.html"

# Default sidebar template. Omit this setting for single column mode without sidebar.
SIDEBAR = "sidebar.html"

CUSTOM_SIDEBAR_MIDDLES = ("sb_tagcloud.html", "sb_links.html")

TAG_CLOUD_STEPS = 4	
TAG_CLOUD_MAX_ITEMS = 100
TAG_CLOUD_SORTING = 'random'
TAG_CLOUD_BADGE = False

#SOCIAL = (('Twitter', 'https://twitter.com/username',
#         'fa fa-twitter-square fa-fw fa-lg'),
#        ('LinkedIn', 'http://linkedin-url',
#         'fa fa-linkedin-square fa-fw fa-lg'),
#        ('GitHub', 'https://github.com/AiLECS',
#         'fa fa-github-square fa-fw fa-lg'),
#        )
######################################################################