a = "Santhosh meets Harsha. Harsha also meets Santhosh, but they are both Busy"
split=a.split()
words = [w.strip('.,') for w in split]
m = ["Santhosh", "Harsha", "Busy"]
x = {word: words.count(word) for word in m}
print(x)



