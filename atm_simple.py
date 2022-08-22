import os,sys
saldo = 100000000
def atm():
	os.system("clear")
	print("""
Atm Simple

1. Cek Saldo
2. Tarik Tunai
3. Isi Tunai""")
	c = input("\nPilih : ")
	if c in[""]:
		print("isi yang benar")
	elif c in["1","01"]:
		print(int(saldo))
	elif c in["2","02"]:
		tarik = int(input("Ingin Tarik Berapa : "))
		sisa = tarik-saldo
		print("Total Saldo Sebelumnya : %s"%(saldo))
		print("Jumlah Total Yang Di Tarik : %s"%(tarik))
		print("Total Saldo Yang Tersisa : %s"%(sisa))
	elif c in["3","03"]:
		isi = int(input("Ingin Isi Saldo Berapa : "))
		nambah = isi+saldo
		print("Total Saldo Sebelumnya : %s"%(saldo))
		print("Total Saldo Bertambah Menjadi : %s"%(nambah))
	else:
		print()


atm()
