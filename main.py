import subprocess

willContinue = True
print("******" * 10)
print("******" * 10)
print("""This is currently an alpha demo. Only the 'ICMP' function is 
operational. This was created for educational purposes only. As more 
features are created, this alpha will be updated. Please Enjoy. """)
print("******" * 10)
print("******" * 10)
print("")
while willContinue:
	requestScan = input("What type of scan? EX (ICMP, TCP): ").upper()


	if requestScan == "ICMP":
		print("")
		print("""You may enter a full Ip address or a partial Ip. A full Ip is directed towards 1 specific known target.
	An example would be '192.168.0.1'.A partial IP is missing one number so that you may index through different scans.
	An Example would be '192.168.0._'. The '_' would be the missing number not inputted.""")
		print("")
		print("What type of IP scan will you do?")

		havenNotPickedOptionCorrectly = True

		while havenNotPickedOptionCorrectly:
			inputFullOrPartialIP = input("Input 'F' for Full ip or 'P' for partial ip: ").upper()

			if inputFullOrPartialIP == "P":
				partialIP = input("Enter your partial IP address.")
				firstNumberInRange = int(input("What is your first range number: "))
				secondNumberInRange = int(input("What is your second range number: "))
				for ping in range(firstNumberInRange, secondNumberInRange):
					address = partialIP + str(ping)
					res = subprocess.call(["ping", "-c", "3", address])
					if res == 0:
						print("ping to", address, "OK")
					elif res == 2:
						print("no response from", address)

					else:
						print("ping to", address, "failed!")

				havenNotPickedOptionCorrectly = False

			elif inputFullOrPartialIP == "F":
				fullIP = input("Input full IP address: ")
				res = subprocess.call(['ping', '-c', '3', fullIP])
				if res == 0:
					print("ping to", fullIP, "OK")
				elif res == 2:
					print("no response from", fullIP)
				else:
					print("ping to", fullIP, "failed!")
				havenNotPickedOptionCorrectly = False
			willContinue = False

	elif requestScan == "TCP":
		print("That options isn't available quite yet? Please try 'ICMP'")

	else:
		print("That is not available, Please try again.")


