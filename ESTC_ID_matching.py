# Script to retrieve the ESTC ID of files by matching the filenames
# Basically we take all filenames from https://github.com/faustusdotbe/TCP-ECCO-texts, which are TCP IDs,
# then open the corresponding notice on https://ota.ox.ac.uk/tcp/ , 
# and then parse the html to get the ESTC ID.
# Results are stored in a csv

# Simon Hengchen -- simon.hengchen@helsinki.fi
# Made for python3



import re, os, glob, urllib.request, io

dir_in = os.path.abspath(os.path.join(os.path.dirname(os.getcwd()),"TCP-ECCO-texts","txts/"))
dir_out = os.path.abspath(os.path.join(os.path.dirname(os.getcwd()),"TCP-ECCO-texts","output/"))

if not os.path.exists(dir_out):
    os.makedirs(dir_out)


output = io.open(dir_out+"/output.csv","w")
output.write("TCP_ID,ESTC_ID\n")



files = glob.glob(dir_in+"/*")

print(dir_in)

for file in files:
	#print(file[-14:-12]) 			# K000039.000.txt, we want the two digits after K
	if file[-14:-12] == "00":
		TCP_ID = file[-15:-4]
		print("https://ota.ox.ac.uk/tcp/headers/K00/"+TCP_ID+".html")		
		html = urllib.request.urlopen("https://ota.ox.ac.uk/tcp/headers/K00/"+TCP_ID+".html")
		html = html.read()
		html = html.decode()
		print(type(html))

		ESTC_ID = re.search(";\ ESTC\ \S*;",html)

		if ESTC_ID:
			
			#output.write(TCP_ID+","+ESTC_ID[7:-1],"\n")
			output.write(TCP_ID+","+ESTC_ID.group(0)[7:-1]+"\n")

		else:
			print("file",TCP_ID,"has no ESTC_ID")


	if file[-14:-12] == "01":
		TCP_ID = file[-15:-4]
		print("https://ota.ox.ac.uk/tcp/headers/K01/"+TCP_ID+".html")		
		html = urllib.request.urlopen("https://ota.ox.ac.uk/tcp/headers/K01/"+TCP_ID+".html")
		html = html.read()
		html = html.decode()
		print(type(html))

		ESTC_ID = re.search(";\ ESTC\ \S*;",html)

		if ESTC_ID:
			
			#output.write(TCP_ID+","+ESTC_ID[7:-1],"\n")
			output.write(TCP_ID+","+ESTC_ID.group(0)[7:-1]+"\n")

		else:
			print("file",TCP_ID,"has no ESTC_ID")

	if file[-14:-12] == "02":
		TCP_ID = file[-15:-4]
		print("https://ota.ox.ac.uk/tcp/headers/K02/"+TCP_ID+".html")		
		html = urllib.request.urlopen("https://ota.ox.ac.uk/tcp/headers/K02/"+TCP_ID+".html")
		html = html.read()
		html = html.decode()
		print(type(html))

		ESTC_ID = re.search(";\ ESTC\ \S*;",html)

		if ESTC_ID:
			
			#output.write(TCP_ID+","+ESTC_ID[7:-1],"\n")
			output.write(TCP_ID+","+ESTC_ID.group(0)[7:-1]+"\n")

		else:
			print("file",TCP_ID,"has no ESTC_ID")

	if file[-14:-12] == "03":
		TCP_ID = file[-15:-4]
		print("https://ota.ox.ac.uk/tcp/headers/K03/"+TCP_ID+".html")		
		html = urllib.request.urlopen("https://ota.ox.ac.uk/tcp/headers/K03/"+TCP_ID+".html")
		html = html.read()
		html = html.decode()
		print(type(html))

		ESTC_ID = re.search(";\ ESTC\ \S*;",html)

		if ESTC_ID:
			
			#output.write(TCP_ID+","+ESTC_ID[7:-1],"\n")
			output.write(TCP_ID+","+ESTC_ID.group(0)[7:-1]+"\n")

		else:
			print("file",TCP_ID,"has no ESTC_ID")

	if file[-14:-12] == "04":
		TCP_ID = file[-15:-4]
		print("https://ota.ox.ac.uk/tcp/headers/K04/"+TCP_ID+".html")		
		html = urllib.request.urlopen("https://ota.ox.ac.uk/tcp/headers/K04/"+TCP_ID+".html")
		html = html.read()
		html = html.decode()
		print(type(html))

		ESTC_ID = re.search(";\ ESTC\ \S*;",html)

		if ESTC_ID:
			
			#output.write(TCP_ID+","+ESTC_ID[7:-1],"\n")
			output.write(TCP_ID+","+ESTC_ID.group(0)[7:-1]+"\n")

		else:
			print("file",TCP_ID,"has no ESTC_ID")

	if file[-14:-12] == "05":
		TCP_ID = file[-15:-4]
		print("https://ota.ox.ac.uk/tcp/headers/K05/"+TCP_ID+".html")		
		html = urllib.request.urlopen("https://ota.ox.ac.uk/tcp/headers/K05/"+TCP_ID+".html")
		html = html.read()
		html = html.decode()
		print(type(html))

		ESTC_ID = re.search(";\ ESTC\ \S*;",html)

		if ESTC_ID:
			
			#output.write(TCP_ID+","+ESTC_ID[7:-1],"\n")
			output.write(TCP_ID+","+ESTC_ID.group(0)[7:-1]+"\n")

		else:
			print("file",TCP_ID,"has no ESTC_ID")


	if file[-14:-12] == "06":
		TCP_ID = file[-15:-4]
		print("https://ota.ox.ac.uk/tcp/headers/K06/"+TCP_ID+".html")		
		html = urllib.request.urlopen("https://ota.ox.ac.uk/tcp/headers/K06/"+TCP_ID+".html")
		html = html.read()
		html = html.decode()
		print(type(html))

		ESTC_ID = re.search(";\ ESTC\ \S*;",html)

		if ESTC_ID:
			
			#output.write(TCP_ID+","+ESTC_ID[7:-1],"\n")
			output.write(TCP_ID+","+ESTC_ID.group(0)[7:-1]+"\n")

		else:
			print("file",TCP_ID,"has no ESTC_ID")

	if file[-14:-12] == "07":
		TCP_ID = file[-15:-4]
		print("https://ota.ox.ac.uk/tcp/headers/K07/"+TCP_ID+".html")		
		html = urllib.request.urlopen("https://ota.ox.ac.uk/tcp/headers/K07/"+TCP_ID+".html")
		html = html.read()
		html = html.decode()
		print(type(html))

		ESTC_ID = re.search(";\ ESTC\ \S*;",html)

		if ESTC_ID:
			
			#output.write(TCP_ID+","+ESTC_ID[7:-1],"\n")
			output.write(TCP_ID+","+ESTC_ID.group(0)[7:-1]+"\n")

		else:
			print("file",TCP_ID,"has no ESTC_ID")

	if file[-14:-12] == "08":
		TCP_ID = file[-15:-4]
		print("https://ota.ox.ac.uk/tcp/headers/K08/"+TCP_ID+".html")		
		html = urllib.request.urlopen("https://ota.ox.ac.uk/tcp/headers/K08/"+TCP_ID+".html")
		html = html.read()
		html = html.decode()
		print(type(html))

		ESTC_ID = re.search(";\ ESTC\ \S*;",html)

		if ESTC_ID:
			
			#output.write(TCP_ID+","+ESTC_ID[7:-1],"\n")
			output.write(TCP_ID+","+ESTC_ID.group(0)[7:-1]+"\n")

		else:
			print("file",TCP_ID,"has no ESTC_ID")

	if file[-14:-12] == "09":
		TCP_ID = file[-15:-4]
		print("https://ota.ox.ac.uk/tcp/headers/K09/"+TCP_ID+".html")		
		html = urllib.request.urlopen("https://ota.ox.ac.uk/tcp/headers/K09/"+TCP_ID+".html")
		html = html.read()
		html = html.decode()
		print(type(html))

		ESTC_ID = re.search(";\ ESTC\ \S*;",html)

		if ESTC_ID:
			
			#output.write(TCP_ID+","+ESTC_ID[7:-1],"\n")
			output.write(TCP_ID+","+ESTC_ID.group(0)[7:-1]+"\n")

		else:
			print("file",TCP_ID,"has no ESTC_ID")

	if file[-14:-12] == "10":
		TCP_ID = file[-15:-4]
		print("https://ota.ox.ac.uk/tcp/headers/K10/"+TCP_ID+".html")		
		html = urllib.request.urlopen("https://ota.ox.ac.uk/tcp/headers/K10/"+TCP_ID+".html")
		html = html.read()
		html = html.decode()
		print(type(html))

		ESTC_ID = re.search(";\ ESTC\ \S*;",html)

		if ESTC_ID:
			
			#output.write(TCP_ID+","+ESTC_ID[7:-1],"\n")
			output.write(TCP_ID+","+ESTC_ID.group(0)[7:-1]+"\n")

		else:
			print("file",TCP_ID,"has no ESTC_ID")

	if file[-14:-12] == "11":
		TCP_ID = file[-15:-4]
		print("https://ota.ox.ac.uk/tcp/headers/K11/"+TCP_ID+".html")		
		html = urllib.request.urlopen("https://ota.ox.ac.uk/tcp/headers/K11/"+TCP_ID+".html")
		html = html.read()
		html = html.decode()
		print(type(html))

		ESTC_ID = re.search(";\ ESTC\ \S*;",html)

		if ESTC_ID:
			
			#output.write(TCP_ID+","+ESTC_ID[7:-1],"\n")
			output.write(TCP_ID+","+ESTC_ID.group(0)[7:-1]+"\n")

		else:
			print("file",TCP_ID,"has no ESTC_ID")

	if file[-14:-12] == "12":
		TCP_ID = file[-15:-4]
		print("https://ota.ox.ac.uk/tcp/headers/K12/"+TCP_ID+".html")		
		html = urllib.request.urlopen("https://ota.ox.ac.uk/tcp/headers/K12/"+TCP_ID+".html")
		html = html.read()
		html = html.decode()
		print(type(html))

		ESTC_ID = re.search(";\ ESTC\ \S*;",html)

		if ESTC_ID:
			
			#output.write(TCP_ID+","+ESTC_ID[7:-1],"\n")
			output.write(TCP_ID+","+ESTC_ID.group(0)[7:-1]+"\n")

		else:
			print("file",TCP_ID,"has no ESTC_ID")


	if file[-14:-12] == "13":
		TCP_ID = file[-15:-4]
		print("https://ota.ox.ac.uk/tcp/headers/K13/"+TCP_ID+".html")		
		html = urllib.request.urlopen("https://ota.ox.ac.uk/tcp/headers/K13/"+TCP_ID+".html")
		html = html.read()
		html = html.decode()
		print(type(html))

		ESTC_ID = re.search(";\ ESTC\ \S*;",html)

		if ESTC_ID:
			
			#output.write(TCP_ID+","+ESTC_ID[7:-1],"\n")
			output.write(TCP_ID+","+ESTC_ID.group(0)[7:-1]+"\n")

		else:
			print("file",TCP_ID,"has no ESTC_ID")