def main():
    indoor_input = input("Tell me what to say with an indoor voice: ")
    print(indoor_voice(indoor_input))

def indoor_voice(x):
    return x.lower()

main()
