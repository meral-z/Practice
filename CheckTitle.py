def checktitle(Instring):
    words = Instring.split()
    for word in words:
        if word != word.capitalize():
            return  False
    return True

print(checktitle("A Mind Boggling Achievement"))
print(checktitle("A Simple C++ Program!"))
print(checktitle("Water is transparent"))