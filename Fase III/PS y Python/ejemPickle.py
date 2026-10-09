import pickle
 
todo = ['write blog post', 'reply to email', 'read in a book', 42]
pickle_file = open('todo2024.pickle', 'wb')
pickle.dump(todo, pickle_file)
pickle_file.close()
