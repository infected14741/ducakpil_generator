import os, sys

print ("\033[1;32mSYSTEM LOGIN INFORMASI")

print ("\033[1;32mMASUKKAN USER & PASSWORD")

KK  : 'KARTU KELUARGA'      

NIK : 'NOMER INDUK KEPENDUDUKAN'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("KK  : ")

	if uname == username:

		pwd = raw_input("NIK : ")



		if pwd == password:

			print "\033[1;32mLogin SUCCESS...", 

			sys.exit()



		else:

			print "\032[1;32mKK YANG ANDA MASUKAN SALAH...!!!\033[00m"

			print "Back Login\n"

			penduduk()



	else:

		print "\033[1;32mNIK YANG ANDA MASUKAN SALAH...!!!\033[00m"

		print "Back Login\n"

		penduduk()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	penduduk()
