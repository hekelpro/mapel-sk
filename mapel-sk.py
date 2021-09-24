import os, math

def createMap(bin_oct_map):
	bin_oct_map["000"] = '0'
	bin_oct_map["001"] = '1'
	bin_oct_map["010"] = '2'
	bin_oct_map["011"] = '3'
	bin_oct_map["100"] = '4'
	bin_oct_map["101"] = '5'
	bin_oct_map["110"] = '6'
	bin_oct_map["111"] = '7'

def convertBinToOct(bin):
	l = len(bin)
	t = -1
	if '.' in bin:
		t = bin.index('.')
		len_left = t
	else:
		len_left = l
	for i in range(1, (3 - len_left % 3) % 3 + 1):
		bin = '0' + bin
	if (t != -1):
		len_right = l - len_left - 1
		for i in range(1, (3 - len_right % 3) % 3 + 1):
			bin = bin + '0'
	bin_oct_map = {}
	createMap(bin_oct_map)
	i = 0
	octal = ""
	while (True) :
		octal += bin_oct_map[bin[i:i + 3]]
		i += 3
		if (i == len(bin)):
			break
		if (bin[i] == '.'):
			octal += '.'
			i += 1
	return octal

def binCvhexa(bnum):
	hex = 0
	mul = 1
	chk = 1
	i = 0
	hnum = []
	while bnum!=0:
		rem = bnum%10
		hex = hex + (rem*mul)
		if chk%4==0:
			if hex<10:
				hex = hex+48
				val = chr(hex)
				hnum.insert(i, val)
			else:
				hex = hex+55
				val = chr(hex)
				hnum.insert(i, val)
			mul = 1
			hex = 0
			chk = 1
			i = i+1
		else:
			mul = mul*2
			chk = chk+1
		bnum = int(bnum/10)

	if chk!=1:
		hex = hex+48
		val = chr(hex)
		hnum.insert(i, val)
	if chk==1:
		i = i-1
	print("Hexadecimalnya: ", end="")
	while i>=0:
		print(end=hnum[i])
		i = i-1
	print()

def cvHex(hex):
	oct = ""
	dec = i = 0
	c = len(hex) - 1
	while i < len(hex):
		d = hex[i]
		if d == '0' or d == '1' or d == '2' or d == '3' or d == '4' or d == '5':
			dec = dec + int(d) * int(math.pow(16, c))
		elif d == '6' or d == '7' or d == '8' or d == '9':
			dec = dec + int(d) * int(math.pow(16, c))
		elif (d == 'A') or (d == 'a'):
			dec = dec + 10 * int(math.pow(16, c))
		elif (d == 'B') or (d == 'b'):
			dec = dec + 11 * int(math.pow(16, c))
		elif (d == 'C') or (d == 'c'):
			dec = dec + 12 * int(math.pow(16, c))
		elif (d == 'D') or (d == 'd'):
			dec = dec + 13 * int(math.pow(16, c))
		elif (d == 'E') or (d == 'e'):
			dec = dec + 14 * int(math.pow(16, c))
		elif (d == 'F') or (d == 'f'):
			dec = dec + 15 * int(math.pow(16, c))
		else:
			print("invalid input")
			break
		i += 1
		c -= 1
	while (dec > 0):
		oct = "".join([str(int(dec % 8)) , oct])
		dec = int(dec / 8)

	return oct


def biner():
	print("""
  (1) binary ke decimal
  (2) binary ke octal
  (3) binary ke hexadecimal
  (0) Kembali
	""")
	pil = input(">>> ")
	while pil == "" or not pil.isdigit():
		pil = input(">>> ")
	if pil == "1":
		num = input("\nMasukan binary: ")
		hsl = int(num, 2)
		print("Decimalnya: "+str(hsl)+"\n")
		biner()
	elif pil == "2":
		num = input("\nMasukan binary: ")
		hsl = convertBinToOct(num)
		print("Octalnya: "+hsl+"\n")
		biner()
	elif pil == "3":
		num = input("\nMasukan binary: ")
		binCvhexa(int(num)); biner()
	else:
		main_menu()

def decim():
	print("""
  (1) decimal ke binary
  (2) decimal ke octal
  (3) decimal ke hexadecimal
  (0) Kembali
	""")
	pil = input(">>> ")
	while pil == "" or not pil.isdigit():
		pil = input(">>> ")
	if pil == "1":
		num = input("\nMasukan decimalnya: ")
		hsl = bin(int(num))[2:]
		print("Binary-nya: "+str(hsl)+"\n")
		decim()
	elif pil == "2":
		num = input("\nMasukan decimalnya: ")
		hsl = oct(int(num))[2:]
		print("Octalnya: "+str(hsl)+"\n")
		decim()
	elif pil == "3":
		num = input("\nMasukan decimalnya: ")
		hsl = hex(int(num))[2:]
		print("Hexadecimal-nya: "+str(hsl)+"\n")
		decim()
	else:
		main_menu()

def octal():
	print("""
  (1) octal ke binary
  (2) octal ke decimal
  (3) octal ke hexadecimal
  (0) Kembali
	""")
	pil = input(">>> ")
	while pil == "" or not pil.isdigit():
		pil = input(">>> ")
	if pil == "1":
		num = input("\nMasukan octal: ")
		hsl = int(num, 8)
		hsl = bin(int(hsl))[2:]
		print("binary-nya: "+str(hsl))
		octal()
	elif pil == "2":
		num = input("\nMasukan octal: ")
		hsl = int(num, 8)
		print("Decimalnya: "+str(hsl))
		octal()
	elif pil == "3":
		num = input("\nMasukan octal: ")
		hsl = int(num, 8)
		hsl = hex(hsl)[2:]
		print("Hexadecimalnya: "+str(hsl))
		octal()
	else:
		main_menu()


def hexa():
	print("""
  (1) hexa ke binary
  (2) hexa ke decimal
  (3) hexa ke octal
  (0) kembali
	""")
	pil = input(">>> ")
	while pil == "" or not pil.isdigit():
		pil = input(">>> ")
	if pil == "1":
		num = input("\nMasukan hexa: ")
		hsl = bin(int(num, 16))[2:]
		print("Binary-nya: "+str(hsl))
		hexa()
	elif pil == "2":
		num = input("\nMasukan hexa: ")
		hsl = int(num, 16)
		print("Decimalnya: "+str(hsl))
		hexa()
	elif pil == "3":
		num = input("\nMasukan hexa: ")
		hsl = cvHex(num)
		print("Octalnya: "+str(hsl))
		hexa()
	else:
		main_menu()


def main_menu():
	os.system("clear")
	print("""
_________                       __
\_   ___ \  _______  __________/  |_
/    \  \/ /    \  \/ /\_  __ \   __\\
\     \___|   |  \   /  |  | \/|  |
 \______  /___|  /\_/   |__|   |__|
        \/     \/

	[ CONVERSI SISTEM BILANGAN KOMPUTER ]


  (1) Binary
  (2) Decimal
  (3) Octal
  (4) Hexadecimal
  (0) Exit
""")
	pil = input(">>> ")
	while pil == "" or not pil.isdigit():
		pil = input(">>> ")
	if pil == "1":
		biner()
	elif pil == "2":
		decim()
	elif pil == "3":
		octal()
	elif pil == "4":
		hexa()
	elif pil == "0":
		exit(">_  Bye...\n")


if __name__=="__main__":
	main_menu()
