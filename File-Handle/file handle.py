'''
fa = open('students.txt', 'a')
fr = open('students.txt', 'r')
fw = open('students.txt', 'w')

contents = fr.read()
fr.close
fw.write('Sam,Ben,James,Will,Adam,Paul,Cale,Harry,Harvey,Jayden,Luke,Dan')
fw.close()

contents = fr.read()
contents_whitespace = contents.find(',')
names = contents.split(None, contents_whitespace)
print(names)

names.sort(reverse=True)
print(names)
'''


def getScore():
    testScore = int(input('Test Score: '))
    return testScore

def main():
    score = getScore()
    if score > 100 or score < 0:
        print('Score outside of range')
        getScore()
    elif score >+
