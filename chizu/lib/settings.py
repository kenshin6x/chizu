from unipath import Path

# app
APP_NAME = 'chizu'
APP_NAME_DISPLAY = u'Chizu'
APP_SHORT_DESCRIPTION = u'Cross-plataform TCG score manager.'
APP_WEBSITE = 'http://www.seisxis.com'
APP_VERSION = '1.0'
APP_AUTHOR_NAME = 'Junior Andrade'
APP_AUTHOR_EMAIL = 'seisxis@gmail.com'

# dirs
DIR_APP = Path(__file__).parent.parent
DIR_STATIC = DIR_APP.child('static')
DIR_ICONS = DIR_STATIC.child('icons')
DIR_ICONS_TOOLBAR = DIR_ICONS.child('toolbar')
DIR_ICONS_MENUBAR = DIR_ICONS.child('menubar')

# icons
ICON_APP = DIR_ICONS.child('%s.png' % APP_NAME)

# icons : menubar
ICON_TOOLBAR_EXIT = DIR_ICONS_TOOLBAR.child('exit.png')
ICON_TOOLBAR_HOME = DIR_ICONS_TOOLBAR.child('home.png')
ICON_TOOLBAR_PLAYERS = DIR_ICONS_TOOLBAR.child('players.png')