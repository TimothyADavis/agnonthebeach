from astropy.table import Table

t=Table.read("AOB_participant_list.csv")


rb='\n'

for row in t:
    text2=r'---'+rb
    text2+='name: '+row['\ufeffFull_name']+rb
    text2+='first_name: '+row['First_name']+rb
    text2+='last_name: '+row['Last_name']+rb
    text2+=r'---'+rb
    text2+=rb+row['Other_info']
        
    with open('../_speakers/'+row['\ufeffFull_name'].replace(' ','')+".md", 'w') as f:
        f.write(text2)      
