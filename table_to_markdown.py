from tabulate import tabulate
import pandas as pd
import glob

file_name = './Master_List.csv'

df_unformatted_load = pd.read_csv(file_name)

# converting simple csv txt inot formatted markdown
# each function represents the complete set inside table pipes

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
    demo_styles = {'-':':exclamation:' , '0': '[:iphone:]' , '1':'[:computer:]', '2':'[:movie_camera:]', '3':'[:clipboard:]'}
    emoji_style = demo_styles[str(demo_type)]
    
    if demo_url == '-':
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


#compiling the new df, listxlist

name_stack = []
git_stack = []
site_stack = []
demo_stack = []
tech_stack = []

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


df_md = pd.DataFrame(columns = ['Name', 'Category' , 'Location' , 'Code', 'Demo', 'TS' ], index=site_stack)
df_md.index.name = 'Site'
df_md['Name'] = name_stack
df_md['Category'] = list(df_unformatted_load['Category'])
df_md['Location'] = list(df_unformatted_load['Location'])
df_md['Code'] = git_stack
df_md['Demo'] = demo_stack
df_md['TS'] = tech_stack


headers = ['Site']
headers.extend(list(df_md.columns))

read_files = glob.glob("./intro.txt")

with open("README.md", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())

f = open('./README.md', 'a')
f.write("____\n")
            


f.write(tabulate(df_md,headers, tablefmt="pipe"))

f.write(" \n")





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
    f.write(" \n")

    f.write(tabulate(df_company_specific, [' ','Details'],tablefmt="pipe"))
    f.write("____\n")











f.close()