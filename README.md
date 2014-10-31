# Random Datatype Generator

This contains 2 scripts: *generator.py* and *reader.py*.

*generator.py* generates four(4) types of printable random objects and store them in a single file.
Each object will be separated by a comma(,).
These are the 4 objects:
 * alphabetical strings
 * real numbers
 * integers
 * alphanumerics

The alphanumerics contains a random number of spaces before and after it (not exceeding 10 spaces).
The output file(random.txt) is 10MB in size.

Sample generated output:
'''
hisadfnnasd, 126263, assfdgsga12348fas, 13123.123, 
lizierdjfklaasf, 123192u3kjwekhf, 89181811238,122, 
nmarcysfa900jkifh  , 3.781, 2.11, ....
'''
*reader.py* reads the generated file and prints to the console the object and its type.
Spaces before and after the alphanumeric object are stripped.

Sample output:
'''
youruasdifafasd - alphabetical strings
127371237 - integer
asdfka12348fas - alphanumeric
13123.123 - real numbers
asjdfklasdjfklaasf - alphabetical strings
123192u3kjwekhf - alphanumeric
'''

