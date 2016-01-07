class bcolors:
	HEADER = '\033[95m'
	OKGREEN = '\033[92m'
	ENDC = '\033[0m'

instruction = {
        'Look up a word in the dictionary:':'open dict://word',
        'Run a virtualenv:':'. venv/bin/activate',
        'Disconnect from virtualenv:':'deactivate',
        'Remove a file:':'rm -Rf /path/of/file',
        'Alter .vimrc:':'vrc',
        'View current path:':'pwd',
        'Open Applications folder:':'open /Applications', 
        'Adjust volume':'osascript -e "set volume x"',
        'Manually start Postgres':'pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start',
        'Manually stop Postgres':'pg_ctl -D /usr/local/var/postgres stop -s -m fast',
        'Rename files or move':'mv old_file new_file',
        'Copy files':'cp file directory/',
        'Forward word / Backward word / Backward-kill-word / Go back or forward one word':'ESC + f / ESC + b / ESC + DEL / ESC + b / ESC + f',
        'Compile and run Java files':'javac -g filename.java' + '\n\t' + 'java classWithTheMainFunction',
        'Stop iTunes from opening with play/pause':'launchctl unload -w /System/Library/LaunchAgents/com.apple.rcd.plist'+ '\n\t' + 'to undo, make unload, load',
        'Copy and paste directory':'cp -a /path/from /path/to',
        'Simple Python server':'python -m SimpleHTTPServer'
}

for k,v in instruction.items():
	print(k + '\n\t' + bcolors.OKGREEN + v + bcolors.ENDC)

