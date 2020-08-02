#Competitive Coding Contest Template Code Generator

A simple python script which takes in the contest link as a command line argument and it automatically generates the template codes and the input files for the contest.

##Key points to remember

* Works only for C++ files.
* template.cpp must be present in the same directory
* Currently works only for Codeforces contests

## Software Requirements

* Python3
    * BeautifulSoup  package
        >pip3 install beautifulsoup4
    * Requests package
        >pip3 install requests

## Executing script

The generator can be executed by simply running the `contestGen.py` file and passing the contest link as a command line argument
   > python3 contestGen.py https://codeforces.com/contest/1379/problem/A
