cat = "Billy"

def rename(cat = "Hugo"):
    cat = "Mr. Fluffy"
    print("The function thinks that the cat is named", cat)

rename(cat)
print("The global cat is", cat)