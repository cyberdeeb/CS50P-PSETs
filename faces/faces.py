def main():

    #Get users message
    message = input("What is your message? ")

    #Convert emoticons
    result = convert(message)

    #Print the new message
    print(result)

def convert(emoticon):

    #Convert :)
    emoticon1 = emoticon.replace(":)","🙂")

    #Convert :(
    emoticon2 = emoticon1.replace(":(","🙁")

    #Return emoji
    return emoticon2

main()