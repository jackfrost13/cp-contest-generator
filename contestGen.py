import sys
import re
import os
import requests
from bs4 import BeautifulSoup
import shutil


def generateCFBoilerplate(problemLink, contestPath):
    if os.path.isfile("template.cpp") == False:
        print("Cannot find template.cpp\nPlease check whether template.cpp exists in the" +
              "current directory or not\nExiting...")
        sys.exit(-1)
    problemCodeRegex = re.compile(r'.+/(\w+)')
    problemCode = problemCodeRegex.findall(problemLink)[0]
    print("Please wait fetching problem "+problemCode+"...")
    res = requests.get(problemLink, allow_redirects=False)
    soup = BeautifulSoup(res.text, "html.parser")
    inputTestcases = soup.select('.input > pre')
    outputTestcases = soup.select('.output > pre')
    inputFile = open(os.path.join(
        contestPath, "input_"+problemCode+".txt"), "w")
    for i in range(len(inputTestcases)):
        newLineRegex = re.compile(r'<br>|<br/>')
        removePreRegex = re.compile(r'<pre>|</pre>')
        testcaseInput = newLineRegex.sub('\n', str(inputTestcases[i]))
        testcaseInput = removePreRegex.sub('', testcaseInput)
        testcaseOutput = newLineRegex.sub('\n', str(outputTestcases[i]))
        testcaseOutput = removePreRegex.sub('', testcaseOutput)
        generatedTestcase = testcaseInput.strip()+"\n\nExpected Output:\n" + \
            testcaseOutput.strip() + "\nEnd of testcase #"+str(i+1)+"\n"
        inputFile.write(generatedTestcase)
    shutil.copy('template.cpp', os.path.join(contestPath, problemCode+".cpp"))


contestLink = str(sys.argv[1])
platformRegex = re.compile(r'((.+/(www.)?(\w+).com/(\w+))/?(\w+)?)')
regSearch = re.findall(platformRegex, contestLink)[0]
contestPlatform = regSearch[3]
contestLink, contestCode = "", ""
if contestPlatform == 'codeforces':
    contestLink = regSearch[0]
    contestCode = regSearch[5]
    res = requests.get(contestLink, allow_redirects=False)
    if res.status_code != 200:
        print("Contest is not yet live or the server did not respont")
        sys.exit(1)
    if os.path.isdir(contestPlatform) == False:
        os.mkdir(contestPlatform)
    contestPath = os.path.join(contestPlatform, contestCode)
    # print(contestPath)
    if os.path.isdir(contestPath) == False:
        os.mkdir(contestPath)
    linkRegex = re.compile(r'href="([a-zA-Z0-9/]+)"')
    found = re.findall(linkRegex, str(BeautifulSoup(
        res.text, "html.parser").select('.id > a')))
    platformRegex = re.compile(r'^http.*com')
    platform = re.findall(platformRegex, contestLink)
    problemsList = [platform[0] + s for s in found]
    open(os.path.join(contestPath, "output.txt"), "w")
    # print(problemsList)
    for p in problemsList:
        generateCFBoilerplate(p, contestPath)

elif contestPlatform == 'codechef':
    contestLink = regSearch[1]
    contestCode = regSearch[4]
    print(contestPlatform + " is not yet supported\nStay tuned! It will be added soon")
    exit(0)
else:
    print(contestPlatform + " is not yet supported\nStay tuned! It will be added soon")
    exit(0)
