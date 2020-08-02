# Competitive Coding Contest Template Code Generator

A simple python script which takes in the contest link as a command line argument and it automatically generates the template codes and the input files for the contest.

## Key points to remember

* Works only for C++ files.
* template.cpp must be present in the same directory
* Currently works only for Codeforces contests. Compatibility for codechef is next in line. Stay tuned

## Software Requirements

* Python3
    * BeautifulSoup  package
        >pip3 install beautifulsoup4
    * Requests package
        >pip3 install requests

## How to run

The generator can be executed by simply running the `contestGen.py` file and passing the contest link as a command line argument
  ```sh
python3 contestGen.py <contest_link>
```

Example:

```sh
python3 contestGen.py https://codeforces.com/contest/1389
```
#### Directory structure
1. The generator first creates a contestPlatform directory i.e `codechef` or `codeforces` if it does not exists in the current directory. 

2. Inside the platform directory it will create a directory named `{contestCode}` (if it does not exists) inside which all contest problem files will be saved.
3. Inside the contest directory a .cpp file will be created for each of the problem along with the test case input file respectively. The cpp is named as `{problemCode}.cpp` and the corresponding input file will be named as `input_{problemCode}.txt`. This will also create a single `output.txt` file inside the contest directory.

The folder tree would look something like
```sh
.
├── codeforces
│   └── 1351
│       ├── A.cpp
│       ├── B.cpp
│       ├── C.cpp
│       ├── input_A.txt
│       ├── input_B.txt
│       ├── input_C.txt
│       └── output.txt
```

**It is advised to use the given template cpp file because it is configured to use the input files**

Cpp template file credits ->  [Rachit Jain](https://github.com/rachitiitr/DataStructures-Algorithms/blob/master/Library/Miscellanious/template.cpp)

Feel free to make changes to the `template.cpp` as per needs but it is advised not to change the ONLINE_JUDGE section of the template.cpp file.

You can add this small snippet to your exists template file to make it compatible with the generator.
```cpp
int main(int argc, char *argv[])
{
#ifndef ONLINE_JUDGE
    if (argc == 2)
        freopen(argv[1], "r", stdin);
    else
        freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
}
```

The input file name which will be read is to be provided as a command line argument while running the cpp file

```sh
g++ A.cpp -o A   //compile cpp code
./A input_A.txt // run the executable using input_A.txt input
```

**The code does not need any modification while submitting to codeforces.com**