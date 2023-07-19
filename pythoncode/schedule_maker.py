from astropy.table import Table

t=Table.read("AOB_schedule.csv")

rb='\n'
for row in t:
    text=r'---'+rb
    text+='name: '+row['\ufeffTitle'].replace(":",";")+rb
    if str(row['Speaker'])!='--':
        text+=r'speakers:'+rb
        if ',' in row['Speaker']:
             for name in row['Speaker'].split(','):
                 text+=r'  - '+str(name)+rb
        else:
            text+=r'  - '+str(row['Speaker'])+rb
    if str(row['Category'])!='--':        
        text+=r'categories:'+rb
        text+=r'  - '+str(row['Category'])+rb
        #text+=r'  - '+row['Contribution Type:']+rb
    text+=r'session_start: '+row['Session_start']+rb
    text+=r'---'+rb
    # if row['Collaborators (if any):']!='':
    #     text+=rb+'Collaborators: '+row['Collaborators (if any):']+rb
    if str(row['Abstract'])!='--':
        if '<p>' in row['Abstract']:
             for sec,aut in zip(row['Abstract'].split('<p>'),row['Speaker'].split(',')):
                 text+=rb+str(aut)+': '+str(sec)+rb
        else:
            text+=rb+str(row['Abstract'])         
    
    # text2=r'---'+rb
    # text2+='name: '+row['First Name:']+' '+row['Surname:']+rb
    # text2+='first_name: '+row['First Name:']+rb
    # text2+='last_name: '+row['Surname:']+rb
    # text2+=r'---'+rb
    # text2+='('+row['Pronouns:']+')'+rb
    # text2+=rb+row['Affiliation:']
    #

    if str(row['Speaker'])!='--':
        fname=row['Speaker'].replace(" ","").replace(",","")
    else:
        fname=row['\ufeffTitle'].replace(" ","")
        
   
    with open('../_talks/'+fname+".md", 'w') as f:
        f.write(text)  
    

text='days:'+rb
day=['Monday','Tuesday','Wednesday','Thursday','Friday']
abrev=['Mo','Tu','We','Th','Fr']
date=['2023-09-11','2023-09-12','2023-09-13','2023-09-14','2023-09-15']
for da,ab,dat in zip(day,abrev,date):
    text+=r'- name: '+da+rb
    text+=r'  abbr: '+ab+rb
    text+=r'  date: '+dat+rb
    text+=r'  rooms:'+rb
    text+=r'  - name: Palazzo Santa Chiara'+rb
    text+=r'    talks:'+rb
    
    tab=t[t['Day']==da]
    for row in tab:
        text+=r'      - name: '+row['\ufeffTitle'].replace(":",";")+rb
        text+=r"        time_start: '"+row['Time_start']+"'"+rb
        text+=r"        time_end: '"+row['Time_end']+"'"+rb   
    
    text+=r'  - name: Tropea'+rb
    text+=r'    talks:'+rb
    text+=r'      - name: Lunch'+rb
    text+=r"        time_start: '13:00'"+rb
    text+=r"        time_end: '14:30'"+rb    
    
with open('program_filled.yml', 'w') as f:
     f.write(text)
