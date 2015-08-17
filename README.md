# Terminal Commands
### Problem:
I always forget a bunch of commands. It's not a problem. I'm human. BUT I do waste time Googling them. 
### Solution:
Have a ready list of FFC (Frequently Forgotten Commands)!
#### What I did:
##### 1. Create a Python Script
I created a Python Script which had a list of commands that I forget. I also included ANSI escape colors because I wanted it to looks pretty. Oh and a friendly message too! Mistakes aren't a bad thing after all.
##### 2. Make an alias using `~/.bash_profile`
Here's the fun part. Open up your `~/.bash_profile` using your favorite text editor. For me, it's vim so I entered the following on my command line:
```
vim ~/.bash_profile
```
Now go to the bottom of your `~/.bash_profile` and create an alias. I want the name of my alias to be `cmds` so I entered this on my `~/.bash_profile`:
```
alias cmds="python3 ~/path/to/my/file"
```
The `~` is important because it tells your computer to go back to your `Users` directory (or what I like to call "homebase") so your path can start fresh. Obviously the `python3` command is important because it runs the file you want using `python3`. If you didn't know that, well now ya do! 
##### 3. Refresh and use!
Now save and exit (or write and quit for vim) and reload your `~/.bash_profile` using this command:
`source ~/.bash_profile`
If nothing happens, then that's good! Now enter your alias on your command line and see the little instruction guide you wrote:
```
cmds
```
I entered `cmds` because that was the alias I made.
##### 4. PARTY!
:D If you have questions, [let me know](https://twitter.com/danagilliann)!
