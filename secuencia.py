import pandas as pd

file = "/home/juancho270/Descargas/GCA_000005845.2_ASM584v2_feature_table.txt"
datos = "/home/juancho270/Descargas/GCA_000005845.2_ASM584v2_genomic.fna"
archi1=open(datos, "r", encoding="utf-8")
data=archi1.read()

df = pd.read_csv(file,sep='\t')
dp = pd.DataFrame(df,columns = list(df))

codificante = ""
no_codificante = ""

columnas = len(df.index)
hola = "hola mundo"

for i in range(len(df.index)):
	if df['# feature'][i] == 'gene':
		codificante = codificante + (data[df['start'][i]: df['end'][i]])
		if i != len(df.index):
			no_codificante = no_codificante + (data[df['end'][i]:df['start'][i+1]])
		else:
			if df['end'][i] != len(data):
				no_codificante = no_codificante + (data[df['end'][i]:len(data)])



print("codificante" + codificante)
print("no codificante" + no_codificante)


