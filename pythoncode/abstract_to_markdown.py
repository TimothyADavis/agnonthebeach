from astropy.table import Table

t=Table.read("AGN on the Beach - abstract submission.csv")
t['catagory']='Extragalactic'
t['Pronouns:']='They/Them'

rb='\n'

for row in t:
    text=r'---'+rb
    text+='name: '+row['Contribution title:']+rb
    text+=r'speakers:'+rb
    text+=r'  - '+row['First Name:']+' '+row['Surname:']+rb
    text+=r'categories:'+rb
    text+=r'  - '+row['catagory']+rb
    text+=r'  - '+row['Contribution Type:']+rb
    text+=r'session_start: False'+rb
    text+=r'---'+rb
    if row['Collaborators (if any):']!='':
        text+=rb+'Collaborators: '+row['Collaborators (if any):']+rb
    text+=rb+row['Abstract:']
    
    text2=r'---'+rb
    text2+='name: '+row['First Name:']+' '+row['Surname:']+rb
    text2+='first_name: '+row['First Name:']+rb
    text2+='last_name: '+row['Surname:']+rb
    text2+=r'---'+rb
    text2+='('+row['Pronouns:']+')'+rb
    text2+=rb+row['Affiliation:']
    
    
with open('../_talks/'+row['First Name:']+'_'+row['Surname:']+".md", 'w') as f:
    f.write(text)  
    
with open('../_speakers/'+row['First Name:']+'_'+row['Surname:']+".md", 'w') as f:
    f.write(text2)      
