#!/usr/bin/env python
from pywsd.lesk import simple_lesk
from pywsd import disambiguate
from pywsd.lesk import adapted_lesk as adaptlesk
from pywsd.lesk import cosine_lesk as coslesk
import re
import fileinput
from nltk.corpus import stopwords

with open("/root/Downloads/IndriRunQuery.queries.file.titledesc", "r+") as f1:
	with open("/root/Downloads/example", "w") as f:
		f.write("""<parameters>
<index>/home/thanos/Downloads/IR-2017-2018-Project-1/indices</index>
<rule>method:dirichlet,mu:1000</rule>
<count>1000</count>
<trecFormat>true</trecFormat>\n""")
                
		num=300        
	        for line in f1:
				
                         	
 				
				num+=1
				temp=disambiguate(line,algorithm=simple_lesk , similarity_option='wup', keepLemmas=False)
                        	temp1=['{} {}'.format(x,y) for x,y in temp] 
 				stop= stopwords.words('english')
				temp2=[var for var in temp1 if var not in stop]
				print temp2
                        	temp2 = ''.join(temp2)	
                        	f.write("<query> <type>indri</type> <number>" + str(num) + "</number> <text>" + temp2)
				endtrec = "</text></query>\n"
				endtrec.strip()
				f.write(endtrec)
                          	

			



				
