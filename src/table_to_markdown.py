#!/usr/bin/env python

__author__ = "Jerome Scelza"
__credits__ = ["Matt Johnson", "Noah Zimmerman"]
__license__ = "MIT"
__version__ = "2.0.1"
__maintainer__ = "Jerome Scelza"
__email__ = "jerome.scelza@mssm.edu"
__status__ = "Prototype"

# This code is used to create the formatted markdown text the drives the README.md on this repo
# The content for the text comes from an unformatted csv called Master_List.csv, this is all of the respective
# blockchain company information that has been sourced by good old-fashioned manual labor (scouring website and transcribing)
# Finally, you will find a series of functions that are used to format the strings in MD, which is subsequently,
# stored into a dataframe. This dataframe then gets converted into pretty print via "tabulate" and saved to an .md file

from tabulate import tabulate
import pandas as pd
import glob

#pulling in the contents from the CSV as a pandas dataframe
file_name = './Master_List.csv'
df_unformatted_load = pd.read_csv(file_name)


#Defining a bunch of functions that transform the content into formatted markdown

def logo_md(im_source, site_link):
    im_md = '[<img src="' + im_source + '" width="80">]' 
    site_md = '(' + site_link + ')'
    return(im_md+site_md)

def logo_md_header(im_source, site_link):
    im_md = '[<img src="' + im_source + '" width="200">]'
    site_md = '(' + site_link + ')'
    return(im_md+site_md)

def name_md(name):
    name_front = '[' + name + ']'
    name_lower = name.lower()
    section = '(#' + name_lower + ')'
    return(name_front + section)

def git_md(git_url):
    git_icon = '[<img src="https://assets-cdn.github.com/images/modules/logos_page/GitHub-Mark.png" width="40">]'
    excl_emoji = ':exclamation:'

    if git_url == '-':
        return(excl_emoji)
    else:
        git_link = '(' + git_url + ')'
        return(git_icon + git_link)

def demo_md(demo_url, demo_type):
    # demo_styles = {'-':':exclamation:' , '0': '[:iphone:]' , '1':'[:computer:]', '2':'[:movie_camera:]', '3':'[:clipboard:]'}
    demo_styles = {'-':':exclamation:' , '0': '[:iphone:]' , '1':'[:computer:]', '2':':exclamation:', '3':':exclamation:'}

    emoji_style = demo_styles[str(demo_type)]

    if str(demo_type) != '0' and str(demo_type) !='1':
        return(emoji_style)
    else:
        demo_link = '(' + demo_url + ')'
        return(emoji_style + demo_link)

def tech_spec_md(spec_url):
    paper_emoji = '[:page_facing_up:]'
    excl_emoji = ':exclamation:'

    if spec_url == '-':
        return(excl_emoji)
    else:
        spec_link = '(' + spec_url + ')'
        return(paper_emoji + spec_link)


# creating individual stacks of formatted data that represent each of the columns
# in the final data table. This is done by looping through the length of unformatted dataframe
# of columns of interest and using the functions to format
name_stack = []
git_stack = []
site_stack = []
demo_stack = []
tech_stack = []
vc_raise_stack = []

for i in range(len(df_unformatted_load)):
    im_source, site_link = df_unformatted_load['logo_source'][i] , df_unformatted_load['Site'][i]
    name = df_unformatted_load['Name'][i]
    git_url = df_unformatted_load['Code'][i]
    demo_url = df_unformatted_load['Demo'][i]
    demo_type = df_unformatted_load['demo_type'][i]
    spec_url = df_unformatted_load['spec_url'][i]

    site_stack.append(logo_md(im_source, site_link))
    name_stack.append(name_md(name))
    git_stack.append(git_md(git_url))
    demo_stack.append(demo_md(demo_url,demo_type))
    tech_stack.append(tech_spec_md(spec_url))
    vc_raise_stack.append(df_unformatted_load['vc_raise'][i])

# Now we are ready to compile the final, fully-formatted dataframe
df_md = pd.DataFrame(columns = ['Name', 'Category' , 'Location' , 'Code', 'Demo', 'TS' ,'VC Raise(M)'], index=site_stack)
df_md.index.name = 'Site'
df_md['Name'] = name_stack
df_md['Category'] = list(df_unformatted_load['Category'])
df_md['Location'] = list(df_unformatted_load['Location'])
df_md['Code'] = git_stack
df_md['Demo'] = demo_stack
df_md['TS'] = tech_stack
df_md['VC Raise(M)'] = vc_raise_stack

# Writing the text to the md file using the file.write() feature of python

# First we open the README and write the intro text.
read_files = glob.glob("./intro.txt")
with open("../README.md", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())

# Second we re-open the README as appending to, and write the table.
f = open('../README.md', 'a')
f.write(" \n")
f.write("____\n")
f.write(" \n")
f.write("## Source List Current Total: __*%s*__ \n" % str(len(df_unformatted_load)))
f.write(" \n")
headers = ['Site']
headers.extend(list(df_md.columns))
f.write(tabulate(df_md,headers, tablefmt="pipe", stralign= "center"))
f.write(" \n")
f.write("____\n")

# Next we are looking to do a similiar process, but with the small company specific tables
detail_params  =  ['Category' , 'Location','Money Raised (M)', 'Method of Funding',
                    'Github Profile','ICO Symbol','Coin','White Paper']

for i in range(len(df_unformatted_load)):
    df_company_specific = pd.DataFrame(columns = ['Details'], index = detail_params)

    category_md = df_unformatted_load['Category'][i]
    location_md = df_unformatted_load['Location'][i]
    raise_md = df_unformatted_load['raise'][i]
    method_md = df_unformatted_load['funding_method'][i]
    spec_url = df_unformatted_load['spec_url'][i]

    git_url = df_unformatted_load['Code'][i]
    git = git_md(git_url)

    ico_symbol = df_unformatted_load['symbol'][i]
    coin_type = df_unformatted_load['platform'][i]
    spec_url = df_unformatted_load['spec_url'][i]
    tech_stack = tech_spec_md(spec_url)

    param_stack = [category_md, location_md,raise_md,method_md,git, ico_symbol, coin_type,
                    tech_stack]

    df_company_specific['Details'] = param_stack

    company_heading = "## " + df_unformatted_load['Name'][i] + "\n"

    f.write(company_heading)
    f.write(" \n")
    f.write(" \n")

    im_source, site_link = df_unformatted_load['logo_source'][i] , df_unformatted_load['Site'][i]
    active_logo = logo_md_header(im_source, site_link) + "\n"
    f.write(active_logo)

    f.write(" \n")
    f.write(" \n")

    f.write(df_unformatted_load['description'][i] + '\n')
    f.write(" \n")
    if df_unformatted_load['Notable'][i] == '-':
        pass
    else:
        f.write('*Notable: ' + str(df_unformatted_load['Notable'][i]) + '*' + '\n')


    f.write(" \n")
    f.write(" \n")

    f.write(tabulate(df_company_specific, [' ','Details'],tablefmt="pipe"))
    f.write(" \n")
    f.write("____\n")

# Finally, we close the markdown file
f.close()