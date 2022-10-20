#Author: Nicole Schanche
#Updated Oct 12, 2022
#This script makes the TESS statistics plots for tess-website-lite. This is very much a work in progress

import pandas as pd
import sqlite3
import json
import re
import numpy as np
#import geograpy
import itertools
import plotly.graph_objects as go
import plotly.express as px
from datetime import date, datetime
from dateutil import rrule
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import defaultdict
from collections import Counter


# Get all of the data you will need to make the TESS statistics plots later on

# Read in the latest database file from tpub (Note that this is static for now, but can be adjusted later when we decide how we want to get tpub data for the website. 
query = sqlite3.connect('content/data/tpub.db').execute('SELECT * FROM pubs')

cols = [column[0] for column in query. description]
results = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)
results = results[results['mission'] == 'tess'].reset_index(drop=True)


# We will want to pull in some information on the author's affiliation (country and state (if applicable))
# CSV from Christina
countries = pd.read_csv("content/data/countries_codes_and_coordinates.csv")
for column in countries.columns[1:]:
    countries[column] = [c.strip().replace('"', "") for c in countries[column]]
countries['Country'] = countries['Country'].replace('Jersey','Bailiwick of Jersey') #Getting confused with New Jersey
countries.head()

states = (
    pd.read_csv("content/data/states.csv")
    .sort_values("State")
    .reset_index(drop=True)
)
states.head()

###################################################################
#                Interactive journal count Plot
###################################################################

# Makes a plot of the number of refereed papers over time, broken up by tpub category

 #restrict this plot to entries that are journal articles (vs book chapter, eptrints, conference proceeding, etc)
is_article = [json.loads(results['metrics'][x])['doctype'] == 'article' for x in range(len(results))]
article = results[is_article]

article['month'] = pd.to_datetime(article['month'], format="%Y-%m", errors='coerce')

start_date = datetime(2018, 4, 1) #Month of first TESS paper
end_date = max(article['month']) 

months = rrule.rrule(rrule.MONTHLY, dtstart=start_date, until=end_date) 

labels = ['exoplanets','astrophysics']

# Cumulative count of number of papers by month
ex_count = np.zeros(int(months.count()))
as_count = np.zeros(int(months.count()))
for ii in range(int(months.count())):
    ex_count[ii] = len(article[(article['month'] <= months[ii])& (article['science'] == 'exoplanets')])
    as_count[ii] = len(article[(article['month'] <= months[ii])& (article['science'] == 'astrophysics')])

    
layout = go.Layout(
    title='TESS journal publications over time',
    plot_bgcolor='rgb(255,255,255)', # set the background colour
    #width=1024,
    #height=756
    
) 

# Interactive plot to tell you how many articles there are when you hover over the points
fig = go.Figure(layout=layout)
fig.add_trace(go.Scatter(x=months[:], y=ex_count,
                    mode='lines',
                    name='exoplanet',
                    line=dict(color="royalblue", width=5),
                    hovertemplate='Date: %{x}'+'<br>Count: %{y:.0f}'+"<extra></extra>"))
fig.add_trace(go.Scatter(x=months[:], y=as_count,
                    mode='lines',
                    name='astrophysics',
                    line=dict(color="tomato", width=5),
                    hovertemplate='Date: %{x}'+'<br>Count: %{y:.0f}'+"<extra></extra>"))
fig.update_xaxes(range=[min(months),max(months)])
fig.add_vline(x=min(months), line_width=2, line_dash="solid", line_color="black")
fig.update_xaxes(gridwidth=0,zeroline=True,automargin=False)
fig.update_yaxes(gridwidth=1, gridcolor='gray',linecolor='black', zeroline=True,zerolinecolor='Black', zerolinewidth=2,automargin=False)
fig.update_layout(
    title="<b>TESS-related Journal Publications",
    yaxis_title="Number of articles",
     xaxis = go.layout.XAxis( tickangle = 45),
    legend_title="Subject",
    legend=dict(orientation='h',yanchor='bottom', y=0.05, xanchor='right', x=1),
    font=dict(
        size=18,
        color="slategray"
    ),
    hoverlabel=dict(
        font_size=18,
    ),
    width=1024,
    height=560,
    
)

#Save the file as an html. Include a pointer to plotly-latest.min.js. 
fig.write_html('themes/pelican-bootstrap3-kepler/templates/includes/papers_over_time.html', include_plotlyjs="{{ SITEURL }}/theme/js/plotly-latest.min.js",
               default_width='100%',default_height='100%')
	       


###################################################################
#                    Static publication Bar Chart
###################################################################

# Makes a plot of the number of refereed papers over time, broken up by tpub category

# DONT restrict this plot to entries that are journal articles (vs book chapter, eptrints, conference proceeding, etc)
article = results.copy()
article['month'] = pd.to_datetime(article['month'], format="%Y-%m", errors='coerce')

start_date = min(article['month'])# #Month of first TESS paper
end_date = max(article['month']) 

years = rrule.rrule(rrule.YEARLY, dtstart=start_date, until=end_date) 


# Cumulative count of number of papers by month
journal_count = np.zeros(int(years.count())-1)
for ii in range(int(years.count())-1):
    journal_count[ii] = len(article[(article['month'] <= years[ii+1])&(article['month'] > years[ii])])

extrapolation = journal_count[-1]*((365-max(article['month']).timetuple().tm_yday)/365.)
fig, ax= plt.subplots(1, figsize=(12,7))
ax.yaxis.grid()
plot_years= [y.year for y in years][1:]
ax.bar(plot_years,journal_count, color ='royalblue',width = 0.8,zorder=3, label='TESS')
ax.bar(plot_years[-1], extrapolation,width= 0.8, color='gray',bottom=journal_count[-1],label='Expected', zorder=3)
ax.tick_params(axis='both', which='major', labelsize=18)
ax.set_xticks(plot_years, fontsize=22)
ax.set_ylabel('Publications per year', fontsize=22)
plt.legend(bbox_to_anchor=(.3, 1.04, .45, 0.06), loc="upper left",
                mode="expand", borderaxespad=0, ncol=2, fontsize=20, framealpha=0.0)
plt.savefig('content/images/publications_barchart.png')
plt.close()


###################################################################
#             Static Journal-by-Subject Pie Plot
###################################################################

colors = ['royalblue', 'tomato']
explode = (0.01, 0.01)
labels = ['exoplanets','astrophysics']

# One random paper was not classified, so just kick it out. 
df = results[(results['science'] == 'exoplanets') | (results['science'] == 'astrophysics')]


fig, ax = plt.subplots(figsize=(8,8))

# Capture each of the return elements.
patches, texts, pcts = ax.pie(
    df['science'].value_counts(normalize=True),  autopct='%.0f%%',
    wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'},
    textprops={'size': 'x-large'}, labeldistance=None, colors=colors, 
    labels=df['science'].value_counts(normalize=True).keys(), startangle=60)
# Style just the percent values.
plt.setp(pcts, color='white', fontweight='bold', fontsize=45)

ax.legend(bbox_to_anchor=(.0, 1.0, 1., 0.01),loc="upper left",
                mode="expand", borderaxespad=0, ncol=2, fontsize=20, framealpha=0.0)
plt.tight_layout()


plt.savefig('content/images/publications_piechart.png')
plt.close()



###################################################################
#                     Wordcloud from Titles
###################################################################


# Make a wordcloud from the titles of all entries (not just journal articles)
title = [json.loads(x)['title'][0] for x in results['metrics'] if json.loads(x)['title'] is not None]

word_cloud = WordCloud(colormap='flag',collocations = False, background_color = 'white', min_word_length=2,width=1200, height=500, min_font_size=8).generate((" ").join(title))

plt.figure(figsize=(24, 10))
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis("off")
plt.savefig("content/images/wordcloud_title.png", bbox_inches='tight')
plt.close()




###################################################################
#                     Interactive Geography plots
###################################################################

#The affiliations in the tpub files often don't contain the actual location names. Here are some common omissions I have found
#Place to put common name variations
country_override = {
    "USA": "United States",
    "UK": "United Kingdom",
    "Suisse": "Switzerland",
    "Northern Ireland": "United Kingdom",
    "Republic Of Korea": "Korea, Republic of",
    "People's Republic of China": "China",
    "Iran": "Iran, Islamic Republic of",
    "Slovak Republic": "Slovakia",
    "Polska":"Poland",
    "UAE": "United Arab Emirates",
    "México": "Mexico",
    "Türkiye":"Turkey",
}

#Some affiliations don't give the country. These are ones I found in the current archive
common_mistakes_country = {'Massachusetts Institute of Technology':"United States",
                "Harvard-Smithsonian":"United States",
                "Kavli":"United States",
                "Space Telescope Science Institute":"United States",
                "Stanford":"United States",
                "Vanderbilt":"United States",
                "AAVSO":"United States",                
                "Caltech":"United States",
                "Moorhead":"United States",
                "Los Alamos":"United States",
                "San Diego":"United States",
                "Annnapolis":"United States",   
                "Louisiana State":"United States",
                "Harper College":"United States",                           
                "Chicago":"United States",   
                "Texas":"United States",
                "American Museum of Natural History":"United States",  
                "SETI":"United States",
                "Ames":"United States",
                "Space Telescope Science Insitute":"United States",
                "Annapolis":"United States",
                "Goddard":"United States",
                "University of Maryland":"United States",
                "Fisk University":"United States",
                "Budapest":"Hungary",
                "Santiago":"Chile",
                "Goettingen":"Germany",
                "Korea":"South Korea", #hot take
                #Crimea is also on the list. Not sure how to handle this. 
                "University of Southampton":"United Kingdom",
                "University of St Andrews":"United Kingdom",
                "University of Leicester":"United Kingdom",
                "University College London":"United Kingdom",
                "University of Oxford":"United Kingdom",
                "University of Manchester":"United Kingdom",
                "Geneva":"Switzerland",
                "Zurich":"Switzerland",
                "New South Wales":"Australia",
                "Tokyo":"Japan",
                "Akdeniz University":"Turkey",
                "University of Colombo":"Sri Lanka",
                "Berlin":"Germany"
                          }

#Many affiliations just contain the University or organization, so this links them to the state
common_mistakes_state = {"Princeton":"New Jersey",
                        "Goddard":"Maryland",
                        "GSFC":"Maryland",
                        "Noqsi":"Colorado",
                        "Lowell":"Arizona",
                        "Ames":"California",
                        "UCB Space Sciences Lab":"California", #Berkeley
                        "Cornell":"New York",
                        "Space Telescope Science Institute":"Maryland",
                        "Lehigh":"Pennsylvania",
                        "Vanderbilt":"Tennessee",
                        "SETI Institute":"California",
                        "Hawai'i":"Hawaii",
                        "Mikulski":"Maryland",
                        "Kitt Peak":"Arizona",
                        "Adler Planetarium":"Illinois",
                        "American Museum of Natural History":"New York",
                        "Harvard-Smithsonian":"Massachusetts",
                        "San Diego":"California",
                        "Chicago":"Illinois",
                        "Fisk University":"Tennessee",
                        "Space Telescope Science Insitute":"Maryland"
                        }

#Some functions to get the demographic info
def findCountry(affil):
    
    for country in countries['Country'].values: #for each country in the csv file
        if country.lower() in affil.lower():
            if country.lower() == 'oman': #Oman comes first, so romania is getting wrongly classified. 
                if 'romania' in affil.lower():
                    return 'Romania'     
            if country.lower() == 'ireland': #Should Northern Ireland be seperate? 
                if 'northern ireland' in affil.lower():
                    return 'United Kingdom'  
            if country.lower() == 'georgia': #I expect these are really the state.
                if ("united states" in affil.lower()) | ("usa" in affil.lower() ):
                    return "United States"     
            return country
        
    for country in country_override:
        if country.lower() in affil.lower():
            return country_override[country]
            
    for country in common_mistakes_country:
        if country.lower() in affil.lower():
            return common_mistakes_country[country]
    #Uncomment this if you want it to print out every affiliation where a country couldn't be found.
    #I used this to identify what to put in the common_mistakes_county dictionary above
    #if affil != '-':
    #    print('No Country identified: %s'%affil)  
    return None 
         
            
def findState(affil, country):
    if country: #If a country was identified
        if (country.lower() == 'united states') or (country.lower() == 'usa'): #If that country is the US find the state
            for state in states.itertuples():
                if ((state.State.lower() in affil.lower()) | (state.Postal in affil)): #Look for either the state name spelled out or the two-letter postal code
                    return state.State

            for state in common_mistakes_state:
                if state.lower() in affil.lower(): 
                    return common_mistakes_state[state]
                
            if affil != '-':
                print('No State identified: %s'%affil)      

    return None


        
def get_latlong(country, state):
    if country:
        #if self.country in country_override.keys():
        #    self.country = country_override[self.country]
        if (country.lower() == 'united states') or (country.lower() == 'usa'):
            if state:
                lat = states[states['State'] == state]["Latitude"].values[0]
                long = states[states['State'] == state]["Longitude"].values[0]
            else:
                lat = None
                long = None
        else:
            lat = countries[countries['Country'] == country]["Latitude"].values[0]
            long = countries[countries['Country'] == country]["Longitude"].values[0]
    else:
        lat = None
        long = None
    return [lat, long]


#This author class makes an object for each author. 
class author:
    def __init__(self, paper_dict, author_number):
        
        self.name = paper_dict['author_norm'][author_number].lower()
        if paper_dict['author_norm'][author_number] == paper_dict['first_author_norm']:
            self.lead_author = 1 
        else:
            self.lead_author = 0
        
        self.bibcode = paper_dict['bibcode']
        self.year = paper_dict['year']
        self.science = paper_dict['science']
        #There could be multiple affiliations. If so, split them up. 
        #This makes the resulting affiliations, countries, states, lat, and longs a list
        
        aff_list = paper_dict['aff'][author_number]
        
        
        if aff_list[-1] == ';':
            aff_list = aff_list[:-1]#Sometimes it ends with a ; which throws off the string split
        affil_split=re.split(';',aff_list.replace('lt;','<').replace('amp;','&')) 
        
        self.affiliation = affil_split
        self.country = [findCountry(affil) for affil in affil_split] #paper_dict['aff'][author_number]
        self.state = [findState(affil_split[ii], self.country[ii]) for ii in range(len(affil_split))]
        
        latlongs = [get_latlong(self.country[ii], self.state[ii]) for ii in range(len(affil_split))]
        self.lat = [coord[0] for coord in latlongs]
        self.long = [coord[1] for coord in latlongs]


#Make a list containing author objects
author_list=[]
for paper_num in range(len(results['metrics'])): #for each paper
    for author_num in range(len(json.loads(results['metrics'][paper_num])['author_norm'])): #for each author
        author_list.append(author(json.loads(results['metrics'][paper_num]), author_num))

#Group these to get a new list where each item is a collection of instances of the same author
author_groups = defaultdict(list)
for obj in author_list:
    author_groups[obj.name].append(obj)

#Uncomment if you want to print out how many papers each author led or contributed to. Can do more with this later if needed. Not being used for statistics plots at the moment. 
'''for group in author_groups.keys():
    
    unique_countries = set([item for item in list(itertools.chain(*[x.country for x in author_groups[group]])) if item is not None])
    unique_states = set([item for item in list(itertools.chain(*[x.state for x in author_groups[group]])) if item is not None])
    lead_author_count = sum([item.lead_author for item in author_groups[group]])
    total_papers = len(author_groups[group])
    #if (len(unique_countries) > 1) & ('United States' in unique_countries):

    print('{:<20} led: {:<4} on: {}'.format(group, sum([item.lead_author for item in author_groups[group]]), len(author_groups[group])))
    print(unique_countries, unique_states)
    print()'''


#Plot number of unique America-based authors (regarless of position on author list) in each state 
#Find unique authors (if they have multiple affiliations they will be counted twice)
unique_author_df = pd.DataFrame(data={'name':[obj.name for obj in author_list], 'author_flag':[obj.lead_author for obj in author_list],'country':[obj.country[0] for obj in author_list],'state':[obj.state[0] for obj in author_list]}).drop_duplicates()

state_counts = Counter(unique_author_df.state)
sc_df = pd.DataFrame({'state':state_counts.keys(), 'Authors':state_counts.values()}).dropna()
sc_df['State'] = [states[states['State'] == ss]['Postal'].values[0] for ss in sc_df['state']]

fig = px.choropleth(sc_df, 
            locations='State',
             color="Authors",
            color_continuous_scale=['mistyrose','tomato','red'],#Set the colors manually as the "reds" colorbar looked bad.
              locationmode="USA-states",
               scope="usa",
             range_color=(0,max(sc_df['Authors'])),
             title='Number of unique authors from US states',

            )

fig.update_layout(
    title_text = '<b>TESS Contributing authors by state',
    title_font_size=24,
    #title_x=0.15,
    showlegend = False,
    dragmode=False,
    hoverlabel=dict(
        font_size=18,
        bgcolor='white'
    ),
    width=1024,
    height=700,
    coloraxis_colorbar_x=0.,
    margin=dict(t=50, r=0,  l=10),
    )
fig.update_coloraxes(colorbar_tickfont={'size':16})

fig.write_html('themes/pelican-bootstrap3-kepler/templates/includes/US_author_count.html', include_plotlyjs="{{ SITEURL }}/theme/js/plotly-latest.min.js",default_width='80vw',default_height='80vh')
#Uncomment if you want to save out a static imge instead
#fig.write_image("any_author_count_USonly.png", height=512, scale=10)






#Make a plot showing where all LEAD authors are from
lead_author_country = [obj.country[0] for obj in author_list if obj.lead_author == 1]
country_counts = Counter(lead_author_country)
cc_df = pd.DataFrame({'country':country_counts.keys(), 'count':country_counts.values()}).dropna()
cc_df['count_normalized'] = cc_df['count']/sum(cc_df['count'])


fig = px.choropleth(cc_df, 
            locations='country',
             color="count",
            color_continuous_scale=['skyblue','royalblue','mediumblue'],#Custom color scale as the "Blues" colorbar didn't go with the theme
              locationmode="country names",
               scope="world",
             range_color=(0,max(cc_df['count'])),
             title='Lead author affiliation',
            height=600,
            width=1024,   
            )

fig.update_layout(
    title_text = '<b>TESS Lead author affiliation',
    title_font_size=24,
    #title_x=0.15,
    showlegend = False,
    dragmode=False,
    hoverlabel=dict(
        font_size=18,
        bgcolor='white'
    ),
    margin=dict(t=40, r=0,  l=10),

)
fig.update_coloraxes(colorbar_tickfont={'size':16})
fig.write_html('themes/pelican-bootstrap3-kepler/templates/includes/Lead_author_affiliation.html', include_plotlyjs="{{ SITEURL }}/theme/js/plotly-latest.min.js",default_width='80vw',default_height='80vh')
#Uncomment if you want to save a static image of the plot
#fig.write_image("lead_author_affiliations.png", width=1024, scale=10)


###################################################################
#                  Author connection "flight map"
###################################################################
#Kind of redundant to what was done above, but it made sorting the data for this a lot easier
paper_list=[]
for paper_num in range(len(results['metrics'])): #for each paper
    paper_list.append([author(json.loads(results['metrics'][paper_num]), ii) for ii in range(len(json.loads(results['metrics'][paper_num])['author_norm']))])

fig = go.Figure()

fig.add_trace(go.Scattergeo(
    locationmode = 'country names',
    lon = countries['Longitude'],
    lat = countries['Latitude'],
    hoverinfo = 'text',
    text = countries['Country'],
    mode = 'markers',
    marker = dict(
        size = 2,
        color = 'rgb(220, 220, 220)',
        line = dict(
            width = 3,
            color = 'rgba(68, 68, 68, 0)'
        )
    )))

flight_paths = []
for paper_num in range(len(results['metrics'])):
    objs = paper_list[paper_num]
    paper_country = [x.country[0] for x in objs] #Note this only takes the primary affiliation
    paper_state = [x.state[0] for x in objs]
    #if paper_country.count('United States') == 0:

    for i in range(len(objs)-1):
        if (objs[0].long[0] != None) & (objs[i+1].long[0] != None):
            if objs[0].long[0] != objs[i+1].long[0]:
                fig.add_trace(
                    go.Scattergeo(
                        #locationmode = 'country names',
                        lon = [objs[0].long[0], objs[i+1].long[0]],
                        lat = [objs[0].lat[0], objs[i+1].lat[0]],
                        mode = 'lines',
                        
                        line = dict(width = 1,color = 'royalblue'),

                        opacity = 0.02,
                        

                    )
                )

fig.update_layout(
    title_text = '<b>Author connections',
    title_font_size=24,
    showlegend = False,
    width=1024,
    height=600,
    geo = dict(
        scope = 'world',
        projection_type = 'natural earth',#'mollweide',
        showland = True,
        landcolor = 'rgb(243, 243, 243)',
        countrycolor = 'rgb(204, 204, 204)',
    ),
    hoverlabel=dict(
        font_size=18,
        bgcolor='white'
    ),
    dragmode=False,
    margin=dict(t=50, r=50,  l=10),
     
)
#This worked a lot better as a static image. The interactive plot was way too messy. 
fig.write_image("content/images/author_connections.png", width=1024)
