import matplotlib.pyplot as plt
import time as t

time = []
mistakes = 0

print("This program will help you to type faster. You will to type the word 'programming' as fast as you can for five times")
input("Press enter to continue.")

while len(time) < 5:
    start = t.time()
    word = input("Type the word: ")
    end = t.time()
    time_elapsed = end - start

    time.append(time_elapsed)

    if (word.lower() != "programming"):
        mistakes += 1

print("You made " + str(mistakes) + " mistakes.")
print("Now let's see your evolution")
t.sleep(3)

x = [1,2,3,4,5]
y = time
plt.plot(x,y)
legend = ["1", "2", "3", "4", "5"]
plt.xticks(x,legend)
plt.ylabel('Time in seconds')
plt.xlabel('Attempts')
plt.title('Your typing evolution')
plt.show()
