import datetime
import os

AUTHOR = 'TESS GI'
SITEURL = ''
PATH = 'content'
STATIC_PATHS = ['images']
SITELOGO = 'images/logos/NASA_logo_vector_lg.png'
SITELOGO_SIZE = 32
SITEURL = "https://heasarc.gsfc.nasa.gov/docs/tess"	
FULLURL = "https://heasarc.gsfc.nasa.gov/docs/tess"



SITENAME = "TESS"
HIDE_SITENAME = False


THEME = "themes/pelican-bootstrap3-kepler"
BOOTSTRAP_THEME = 'cosmo'
BOOTSTRAP_FLUID = False
FAVICON = 'images/logos/favicon.png'

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 5

HIDE_SIDEBAR = True

# Defines the "related websites" listing in the footer of all pages
RELATEDSITES = (
            ('NASA News, Media, and Education Resources',
             'https://nasa.gov/tess'),
            ('TESS @ MIT',
             'http://tess.mit.edu/'), 
            ('TESS @ MAST',
             'http://archive.stsci.edu/tess'),
            ('High Energy Astrophysics Science Archive Research Center',
             'https://heasarc.gsfc.nasa.gov/'),
            ('NASA Exoplanet Archive @ IPAC',
             'http://exoplanetarchive.ipac.caltech.edu'),
            )


MENUITEMS = (
          ('Education Resources', (
            ('What is TESS?', 'christina.html'),
            ('Outreach Materials', 'christina.html'),
            ('Citizen Science', 'christina.html'),
            ('FAQ', 'christina.html'),
                    )
        ),

        ('Science Resources', (
            ('Christina', 'christina.html'),
            ('Christina', 'christina.html'),
            ('Christina', 'christina.html'),
            ('Christina', 'christina.html'),
            ('Christina', 'christina.html'),
            ('Christina', 'christina.html'),
             )
        ),
        ('Propose for Observations', (
            ('Proposing Basics', 'proposing_basics.html'),
            ('Christina', 'christina.html'),
            ('Christina', 'christina.html'),
                    )
        ),
        ('Tutorials', (
            ('Christina', 'christina.html'),
            ('Christina', 'christina.html'),
            ('Christina', 'christina.html'),
                    )
        ),
        # For press

        )


MARKDOWN = {
  'extension_configs': {
    'markdown.extensions.toc': {}
  }
}

SHOW_ARTICLE_AUTHOR = True
DEFAULT_PAGINATION = 10

RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True

DATE_MODIFIED = datetime.datetime.now().strftime('%Y-%m-%d')
# Defines the "important dates" box on the front page
IMPORTANT_DATES = (
    ('<b>11th June 2022</b>',
             'AAS Workshop: Engaging the Public in Exoplanet Science Through the Legacy of TESS',
             'https://submissions.mirasmart.com/AAS240/itinerary/EventDetail.aspx?evt=6',),
    ('<b>13th June 2022</b>',
     'AAS Splinter Session: Future Science with TESS',
     'https://submissions.mirasmart.com/AAS240/itinerary/EventDetail.aspx?evt=76'),
     )

DISPLAY_ALERT = True
ALERT_TYPE = 'warning'
ALERT_TITLE = 'TESS Cycle 6 Proposal Deadline.'
ALERT_TEXT = "The TESS Cycle 6 Proposal Deadline is set for DATE. If you are interested in obtaining processed data products or NASA grant funding from TESS, please consider proposing. Click the Proposing tab to learn more."