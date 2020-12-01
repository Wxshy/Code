import time

ts = 'Capital letters are used frequently - learning to type them efficiently is "key" to excellent typing! QWERTY keyboards have two large size SHIFT keys, which make it very convenient. Just make sure to utilize the opposite hand to hold the shift key when you type a capital letter. It\'s much easier this way.'

if input('Press 1 to show the text and start: ') == '1':
    print(ts)
    print()
    start = time.perf_counter()
    userInput = input()

end = time.perf_counter()

total = end - start

words = len(ts.split())
avg = words/(total/60)

if userInput == ts:
    print(total)
    print(avg)