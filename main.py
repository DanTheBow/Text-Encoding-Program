# Die Caesar Verschlüsselung oder Cäsar Chiffre ist ein symmetrisches Verschlüsselungsverfahren,
# das auf der Verschiebung des Alphabets basiert, in diesem Programm um 13 stellen.
# Somit kann man es zum Verschlüsseln und zum Entschlüsseln benutzen.

# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# N O P Q R S T U V W X Y Z A B C D E F G H I J K L M


import codecs

message = input("Nachricht: ")
print(codecs.encode(message, "rot13"))
