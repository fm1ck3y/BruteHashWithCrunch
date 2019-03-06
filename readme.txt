This script allows you to select hash passwords. A list of words in txt format and directly from crunch can be passed to the arguments.
WARNING: Be careful with the RAM, a large number of words from crunch, can lead to bad consequences.

TYPE_HASH : sha512, sha256, md5
Version : Python3.6 Crunch3.6

chmod 777 brute_hash.py # for start python file with ./brute_hash.py *arg
python3.6 brute_hash.py arg # for start python file with python3.6 

Example for brute with txt file: ./brute_hash.py type_hash hash.txt dict_word.txt
Example for brute with crunch : crunch 5 10 abcd | ./brutehash.py type_hash hash.txt
