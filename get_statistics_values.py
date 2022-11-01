import io
from astropy.io.votable import parse
from urllib.request import urlopen
import sqlite3
import pandas as pd
import json



def get_planet_count(df):
    qname = 'https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name+from+ps+where+disc_facility+=+%27Transiting%20Exoplanet%20Survey%20Satellite%20(TESS)%27+and+default_flag+=1'
    u = urlopen(qname)
    v = parse(io.BytesIO(u.read()))
    tess_count = len(v.get_first_table().to_table())
    #f = open('~/tess-website-lite/content/statistics/planetcount.txt','w').write(str(tess_count))
    df['planetcount'] = str(tess_count)
    return df

def get_journal_count(df):
    query = sqlite3.connect('/Users/nthom/tess-website-lite/content/data/tpub.db').execute('SELECT * FROM pubs')
    cols = [column[0] for column in query.description]
    results = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)
    results = results[results['mission'] == 'tess'].reset_index(drop=True)
    df['papercount'] = str(len([json.loads(x)['doctype'] for x in results['metrics'] if json.loads(x)['doctype'] == 'article']))
    return df
    

def main():
    df = pd.DataFrame(data={'planetcount':['0'],'papercount':['0']})
    get_planet_count(df)
    get_journal_count(df)
    df.to_csv('~/tess-website-lite/content/statistics/planet_counter_stats.csv')

if __name__ == "__main__":
    main()
