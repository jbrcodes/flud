# File: docker1/app/jinja.py

import re

from app import app



def formatContent(con):
    return re.sub("\n", "<br>", con)


def formatStamp(td):
    if td:
        out = td.strftime( '%d %b %Y' )
    else:
        out = '--'

    return out
  
    
app.jinja_env.filters['formatContent'] = formatContent
app.jinja_env.filters['formatStamp'] = formatStamp