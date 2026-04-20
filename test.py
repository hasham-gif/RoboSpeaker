import pyttsx3

engine = pyttsx3.init()

# Test 1: Kya engine kaam kar raha hai?
print("Test 1: Speaking 'Hello'")
engine.say("Hello")
engine.runAndWait()
print("Test 1 done")

# Test 2: Loop test
print("Test 2: Loop test")
for i in range(3):
    print(f"Speaking: {i+1}")
    engine.say(f"Number {i+1}")
    engine.runAndWait()
print("Test 2 done")

print("All tests passed!")