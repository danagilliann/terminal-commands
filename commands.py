class bcolors:
	HEADER = '\033[95m'
	OKGREEN = '\033[92m'
	ENDC = '\033[0m'

print()
print(bcolors.HEADER + "Hello Dana!" + bcolors.ENDC)
print()
print("Here are some commands that you might find useful\nWe all forget things from time to time :)")
print()

print("Look up a word in the dictionary:")
print(bcolors.OKGREEN + "\topen dict://word" + bcolors.ENDC)

print("Run a virtualenv:")
print(bcolors.OKGREEN + "\t. venv/bin/activate" + bcolors.ENDC)

print("Disconnect from virtualenv:")
print(bcolors.OKGREEN + "\tdisconnect" + bcolors.ENDC)

print("Remove a file:")
print(bcolors.OKGREEN + "\trm -Rf /path/of/file" + bcolors.ENDC)

print("Alter .vimrc:")
print(bcolors.OKGREEN + "\tvim ~/.vimrc" + bcolors.ENDC)

print("View current path:")
print(bcolors.OKGREEN + "\tpwd" + bcolors.ENDC)

print()
