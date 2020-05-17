# Ship Cost Calculator  

**Introduction**  
This is a tool aimed to do away with hard to understand, easily breaking spreadsheets to work out
the cost of building ships and possibly other things in the future.

No knowledge of programming or Python is needed to run this tool. Only the requirements below.  
As a FYI, if anyone is interested and/or doesn't know and for some context (may help understanding 'installing and running').  
Python is a programming language.  
Git is a source code management tool. Github is an unrelated site to upload git repositories to as backup and
for distribution (like this).  
pwd is a small command in bash that stands for present working directory and it just prints the directory you're in.

**Requirements**  
[Python 3.7](https://www.python.org/downloads/release/python-370/)  
[Git](https://git-scm.com/downloads)

**Installation**  
Push the Windows button and type `git`.  
Launch the Git Bash app.  
Run the following commands in the Git Bash app to clone the git repository and find out what directory it's in.  

`git clone https://github.com/Jeklah/shipCostCalc.git`  
`pwd`  

You should get an output of a directory path, for me its:`/d/Projects/shipCostCalc`  

Push the Windows button and type `cmd` and launch as administrator (if you aren't already).  
Go to the directory path found out using `pwd`.  

**Navigation in cmd**  
Use `cd` to change directories. e.g `cd C:\test\shipCostCalc`. Notice that the slashes are backwards in cmd and
forwards when using Git Bash app. Using the wrong slash will result in an error.  
If you need to change drives (you're in C:\ and its been cloned somewhere in D:\ ) just type the letter of the drive
then colon to change drives. e.g to change from C:\ to D:\ type: `d:` and push enter.  

Once you're in the shipCostCalc directory in cmd we're ready to install the dependencies.  
Run the following command to install dependencies

`pip3 install -r requirements.txt`

**Using the Tool**  
Run the script by running the following command from the shipCostCalc folder in cmd.
You could also run it directly from the scripts folder using `./ships.py`.

Run it directly using:  
`scripts/ships.py`

If that doesn't work try using python directly:  
`python3 scripts/ships.py`

I've now added a few options as well as a help menu.  
`--help` for the help menu. e.g `scripts/ships.py --help`  
`-m` or`--market` to select your market ahead of the menu. e.g `scripts/ships.py -m rens`  
`-s` or `--single` for a single item price check. **__This works with any item!__** Just be sure to spell it correctly and if it has
spaces enclose it in single quotes. e.g `scripts/ships.py -s 'hobgoblin ii'`  
These options can be used together. e.g `scripts/ships.py -s 'hobgoblin ii' -m rens` for a quick price check. I hope this will
 be useful for people.

Use the --help flag for help:  
`scripts/ships.py --help`

**Notes**  
`python3` and `pip3` executable name may rely on your version installed.
If `python3`/`pip3` does not work, the following are worth trying:

`pip3.7`  
`pip3.8`  
`python3.7`  
`python3.8`

**For the Future**  
Please make an issue on what ship people would most like to see added next using 
the [templates](https://github.com/Jeklah/shipCostCalc/tree/master/.github/ISSUE_TEMPLATE) in the .github folder and make an issue on [the issue page](https://github.com/Jeklah/shipCostCalc/issues) using it so I can keep track of what's most wanted.   
Just add your name to an open ship issue to vote, to avoid duplicate ship threads.  
I plan on adding research time into this, how deep would everyone like me to go? Add your name to the issue I will create along with
any comments regarding this.
Please create issues on what else you would like to see done.  

Also, if anyone finds any problems, please create an issue :D and tag it with 'Bug' please. Thanks.

Enjoy
