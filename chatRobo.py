import os


if __name__ =='__main__':
    print("Welcome to chatRobo 1.0. Created by M.Hashaam")
    while True:
        x = input("Enter What you want to speak : ")
        if x == "q":
            os.system("bye 'bye bye friend'")
            break
        command = f"say {x}"
        os.system(x)