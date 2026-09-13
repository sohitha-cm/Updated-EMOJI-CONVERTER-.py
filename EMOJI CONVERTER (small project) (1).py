
# EMOJI CONVERTER






message = input(">")
list_of_message = message.split(" ")
emojis = {
    ":)" : "😊" , 
    ":(" : "🙁" ,
    ":()" : "😀",
    " :|" : "😑"    
}
final_message = ""
for  words in list_of_message :
    final_message += emojis.get(words , words)  + " " 
print(final_message)




# INSIDE A FUNCTION 

def emoji_converter_message(message):
    list_of_message = message.split(" ")
    emojis = {
    ":)" : "😊" , 
    ":(" : "🙁" ,
    ":()" : "😀" ,
    " :|" : "😑"    
}
    final_message = ""
    for  words in list_of_message :
        final_message += emojis.get(words , words)  + " " 
    return final_message

message = input(">")
final_message = emoji_converter_message(message)
print(final_message)
