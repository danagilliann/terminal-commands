class bcolors:
	HEADER = '\033[95m'
	OKGREEN = '\033[92m'
	ENDC = '\033[0m'

print()
print(bcolors.HEADER + "Hello Dana!" + bcolors.ENDC)
print()
print("Here are some commands that you might find useful\nWe all forget things from time to time :)")
print()

instruction = ['Look up a word in the dictionary:',
'Run a virtualenv:',
'Disconnect from virtualenv:',
'Remove a file:',
'Alter .vimrc:',
'View current path:',
'Open Applications folder:', 
'Adjust volume',
'Manually start Postgres',
'Manually stop Postgres',
'Rename files',
'Forward word / Backward word / Backward-kill-word / Go back or forward one word',
'Compile and run Java files']

command = ['open dict://word',
'. venv/bin/activate',
'deactivate',
'rm -Rf /path/of/file',
'vim ~/.vimrc',
'pwd',
'open /Applications', 
'osascript -e "set volume x"',
'pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start',
'pg_ctl -D /usr/local/var/postgres stop -s -m fast',
'mv old_file new_file',
'ESC + f / ESC + b / ESC + DEL / ESC + b / ESC + f',
'javac -g filename.java' + '\n\t' + 'java classWithTheMainFunction']

for n in range(0, len(instruction)):
	print(instruction[n])
	print(bcolors.OKGREEN + '\t' + command[n] + bcolors.ENDC)
	print()

