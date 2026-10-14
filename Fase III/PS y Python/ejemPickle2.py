import pickle

pickle_file = open('todo2026.pickle', 'rb')
todo = pickle.load(pickle_file)
pickle_file.close()
print(type(todo),'\t',todo)
for element in todo:
    print(type(element),'\t',element)
