books_list=[]
author_set= set()
books_dict={}

books_list.append("Python Programming")
author_set.add("John Smith")
books_dict["Python Programming"] = "John Smith"

books_list.append("Data Structures and Algorithm")
author_set.add("Jane Doe")
books_dict["Data Structures and Algorithm"] = "Jane Doe"

books_list.append("Machine Learning Basics")
author_set.add("Alice Johnson")
books_dict["Machine Learning Basics"] = "Alice Johnson"

search_title = input("Enter the title of the book to search:")
if search_title in books_list:
    print(f"Book found!Author: {books_dict[search_title]}")
else:
    print("Book found!")
#DIsplay all book
print("List of Books")
for book in books_list:
    print(book)

#Remove a book
remove_title= input("Enter the title of the book to remove or else enter to skip:")
if remove_title in books_list:
    remove_author=books_dict[remove_title]
    books_list.remove(remove_title)
    author_set.remove(remove_author)
    del books_dict[remove_title]
    print("Book removed successfully!")
    print("Books available: ", books_list)
else:
    print("Book not found")

