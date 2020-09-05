import csv 

from nltk.corpus import stopwords
from thesaurus import Word

en_stops = set(stopwords.words('english'))
#print(en_stops)

l=['happy','happiness','pleasure','joy','glad']			#happy list 
s=['sad','cry','tears','unhappy','pain','wounded','sadness','depressing','depression']	#sad list 
fl=['fear','threatened']								
a=['anger','angry']
b=['boredom','boring','boresome','bore']
e=['excited','excitement','excited','exciting']

neg=['not','doesn\'t']
hy=Word('happy').synonyms()
sd=Word('sad').synonyms()
ay=Word('angry').synonyms()
fr=Word('fear').synonyms()
br=Word('bore').synonyms()
ex=Word('excited').synonyms()

#print(hy,sd,ay,fr,br,ex)

c,counth,counts,counta,countf,counte,countb,n=0,0,0,0,0,0,0,0

print("Enter file name:")
f="para.txt"
try:
	with open(f, 'r') as csvFile:
		reader=csv.reader(csvFile)
		for row in reader:
			row=list(filter(None, row))				#eliminate empty entries
			print("\n",row,"\n")
			for word in row:
				c+=1                            		#count including stop words
				if word in neg:
						n=1
				if word.lower() not in en_stops: 			#remove stop words
					if word.lower() in l or word.lower() in hy:	#check in list defined ,if word not present goto thesaurus
						if n==1:
							print("--:(")
							counts+=1
							n=0
						else:
							print("-- :)",word)
							counth=counth+1
					if word.lower() in s or word.lower() in sd:
						if n==1:
							print("--:)")
							counth+=1
							n=0
						else:
							print("-- :(",word)
							counts=counts+1
					if word.lower() in a or word.lower() in ay:
							print("---:<",word)
							counta=counta+1
					if word.lower() in fl or word.lower() in fr:
							print("---#0",word)
							countf=countf+1
					if word.lower() in b or word.lower() in br:
							print("---:O",word)
							countb=countb+1
					if word.lower() in e or word.lower() in ex:
							print("---:D",word)
							counte=counte+1

										

	csvFile.close()

	m=counth+counts+counta+countf+countb+counte+1
	print("\nHappiness percentage is ",round((counth/m)*100,3) ,"%")
	print("Sadness percentage is ",round((counts/m)*100,3)," %")
	print("Angry percentage is ",round((counta/m)*100,3)," %")
	print("Fear percentage is ",round((countf/m)*100,3)," %")
	print("Bore percentage is ",round((countb/m)*100,3)," %")
	print("Excited percentage is ",round((counte/m)*100,3)," %")
	
	emotion=max(counth,counts,counta,countf,countb,counte)
	#print(emotion)

	if emotion==0:
		print("\n\nThe emotion of the paragraph is neutral\n") 	
	elif counth==emotion:
		print("\n\nThe emotion of the paragraph is happiness\n")
	elif counts==emotion:
		print("\n\nThe emotion of the paragraph is sadness\n")
	elif counte==emotion:
		print("\n\nThe emotion of the paragraph is excitement\n")
	elif countf==emotion:
		print("\n\nThe emotion of the paragraph is fear\n")
	elif countb==emotion:
		print("\n\nThe emotion of the paragraph is boredom\n")
	elif counta==emotion:
		print("\n\nThe emotion of the paragraph is angry\n")
	else:
		print("\n\n")
except:
	print("No such file")
