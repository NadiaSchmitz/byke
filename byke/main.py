# Den has two four-digit combination locks for protecting his bicycle from thieves.
# Every evening he arms the bicycle antitheft alarm and fastens the bicycle to a special
# stand with one of the locks. Den never uses the same lock two evenings in a row.
# One night a thief tried to open the lock using the code 0000.
# The alarm went off and the thief hurried away. The next night the thief decided
# to try the code 0001, then 0002, and so on in ascending order of the number.
# Den never changes the codes of his locks. On the night when the thief came for
# the first time the bicycle was fastened with the first lock.
# Input
# The first line contains the combination that opens the first lock and the second
# line contains the combination that opens the second lock.
# Both combinations are strings consisting of four digits from 0 to 9.
# Output
# Output “yes” if the thief will open the lock sooner or later and “no” otherwise.

i = 0
check = 0
result = ''

while check == 0:
    lock_1 = int(input("Enter a number 0000 - 9998: "))
    lock_2 = int(input("Enter a number 0001 - 9999: "))
    if lock_1 < 0 or lock_1 > 9998 or lock_2 < 1 or lock_2 > 9999:
        print("Wrong number.")
    else:
        check = 1
        while i <= lock_1:
            if lock_1 % 2 > 0:
                result = 'No'
                i += 2
            else:
                result = 'Yes'
                i += 2

print(result)
