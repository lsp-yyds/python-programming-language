def word_count(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
        # msg = "Sorry, the file " + filename + " does not exists."
        # print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


filename = "alice2.txt"
word_count(filename)