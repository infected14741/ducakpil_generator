import os, sys

print ("\033[1;32mSYSTEM LOGIN ADMIN")

print ("\033[1;32mMASUKKAN USER & PASSWORD")

username = 'Fauzi IFC'      

password = 'IndahMewanty14741'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("username : ")

	if uname == username:

		pwd = raw_input("password : ")



		if pwd == password:

			print "\033[1;32mLogin SUCCESS...", 

			sys.exit()



		else:

			print "\032[1;32mPASSWORD YANG ANDA MASUKAN SALAH...!!!\033[00m"

			print "Back Login\n"

			restart()



	else:

		print "\033[1;32mSORRY USER ANDA SALAH...!!!\033[00m"

		print "Back Login\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()
