import time

with open(r"C:\Users\kastr\OneDrive\Робочий стіл\шарага\7 семестр\Чисельні методи\ITcollege\ThirdTask\README.md", "w") as file:
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    file.write(formatted_time)

with open(r"C:\Users\kastr\OneDrive\Робочий стіл\шарага\7 семестр\Чисельні методи\ITcollege\ThirdTask\README.md", "r") as file:
    content = file.read()
    print("File content:", content)

    


