#!/usr/bin/env python

import re
import fileinput

with open("/home/thanos/Downloads/IR-2017-2018-Project-1/topics.301-450.trec", "r+") as f1:
	with open("/home/thanos/Downloads/IR-2017-2018-Project-1/IndriRunQuery.queries.file.all", "w") as f:
		f.write("""<parameters>
<index>/home/thanos/Downloads/IR-2017-2018-Project-1/indices</index>
<rule>method:dirichlet,mu:1000</rule>
<count>1000</count>
<trecFormat>true</trecFormat>\n""")
		#text = f1.readline()
		#pattern = re.compile(r'<title>+.*<desc>', re.I|re.M)
		num = 300
		copy = False
		title = "<title>"
		top1 = "<top>"
		top2 = "</top>"
		desc = "<desc>"
		narr = "<narr>"
		#lineless = text.replace("\n", "")
		for line in f1:
			if top1 in line:
				tmp2 = line[:]
				tmp2 = tmp2.replace("<top>" , "")
				tmp2 = tmp2.replace("\n", "")
				tmp2 = tmp2.strip()
				f.write(" " + tmp2)
			if top2 in line:
				tmp3 = line[:]
				tmp3 = tmp3.replace("</top>" , "")
				tmp3 = tmp3.replace("\n", "")
				tmp3 = tmp3.strip()
				f.write(" " + tmp3)
			if title in line:
				o=1
				num+=1
				titles = line[:]
				symbols = [',' , '.' , '?' , ',' , ';' , ':', '-', '/', '(', ')']
				for i in symbols:
					titles = titles.replace(i, " ")
				titles = titles.replace("<title>" , "")
				titles = titles.replace("\n", "")
				titles = titles.replace("\t", "")
				titles = titles.strip()
				f.write("<query> <type>indri</type> <number>" + str(num) + "</number> <text>" + titles)
			if desc in line:
				 
				copy = True
			if copy:
				
				tmp = line[:]
				symbols = [',' , '.' , '?' , ',' , ';' , ':', '-', '/', '(', ')']
                                for i in symbols:
                                        tmp = tmp.replace(i, " ")
                                tmp = tmp.replace("<desc> Description" , "")
				tmp = tmp.replace("\n", "")
				tmp = tmp.replace("<narr> Narrative", "")
				tmp = tmp.strip()
				f.write(" " + tmp)
			if narr in line:
				copy = True
                        if copy:
				tmp1 = line[:]
				symbols = [',' , '.' , '?' , ',' , ';' , ':', '-', '/', '(', ')']
                                for i in symbols:
                                        tmp = tmp.replace(i, " ")
                                tmp1 = tmp1.replace("<desc> Description" , "")
				tmp1 = tmp1.replace("\n", "")
				tmp1 = tmp1.replace("<narr> Narrative", "")
				tmp1 = tmp1.strip()
				f.write(" " + tmp )
			if top1 in line:
				copy = False
				endtrec = "</text></query>\n"
				endtrec.strip()
				f.write(endtrec)	

		
                          	

			



				
