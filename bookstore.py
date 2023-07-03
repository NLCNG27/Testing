from tkinter import *
from tkinter import messagebox

class Bookstore:
    def __init__(self, title, genre, price):
        self.title = title
        self.genre = genre
        self.price = price

    def __str__(self):
        return f"Title: {self.title}, Genre: {self.genre}, Price: {self.price}"

window = Tk()
window.title("Book Management System")
window.geometry("700x200")

book_list = []
def add_book():
    title_entry = title.get()
    genre_entry = genre.get()
    price_entry = price.get()

    if title_entry == "" or genre_entry == "" or  price_entry == "":
        messagebox.showerror("Add Book", "Please enter all three blank space")
    else:
        new_book = Bookstore(title_entry, genre_entry, int(price_entry))
        book_list.append(new_book)
        # print([book.title for book in book_list])
        list_books()

        messagebox.showinfo("Book added", f"Added {new_book}")


def list_books():
    for book in book_list:
        print('*' * 20, end="\n")
        print('Title:', book.title)
        print('Genre:', book.genre)
        print('Price:', book.price)

def delete_books():
    delete_title = title.get()
    found_book = False 
    
    if delete_title == "":
        messagebox.showerror("Delete Book","Please enter book title!!!")
    else:
        for i in range(len(book_list)):
            if (book_list[i].title) == delete_title:
                del book_list[i]
                print([book.title for book in book_list])
                messagebox.showinfo("Delete Book", f"Delete{delete_title} succesfully")
                found_book = True
                break
                
            if found_book == False:
                messagebox.showerror("Delete Book", "Cannot find this book!!")


def search_books():
    search_book = title.get()
    check = False
    
    if search_book == "":
        messagebox.showerror("Search Book", "Please enter book title!!!")
    else:
        for i in book_list:
            print('searching book:', i)
            if i.title == search_book:
                print([book.title for book in book_list])
                messagebox.showinfo("Search Book", f"Name: {i.title}, genre: {i.genre}, price: {i.price}")
                check = True
                break
            
        if check == False: 
            messagebox.showerror("Search Book", "Cannot find this book!!!")

def update_price_books():
    book_title_price_update = title.get()
    price_update = price.get()                                
    found_books = False

    if book_title_price_update == "" or price_update == "" :
        messagebox.showerror("Update Book Prices", "Please enter book title and price needed to be update")
    else:
        for i in book_list:
            if i.title == book_title_price_update:
                i.price = int(price_update)
                print([book.title for book in book_list])
                messagebox.showinfo("Update Book Prices", f"Updated price of {book_title_price_update} to {price_update}.")
                found_books = True
            else:
                messagebox.showinfo("Update Book Prices", "No books found.")

def reset():
    title.delete(0, "end")
    genre.delete(0,"end")                                    
    price.delete(0,"end")
    search_name.delete(0,"end")        
        
        
title_label = Label(window, text="Title")
genre_label = Label(window, text="Genre")
price_label = Label(window, text="Price")

title = Entry(window)
genre = Entry(window)
price = Entry(window)
search_name = Entry(window)

add_button = Button(window, text="Add Book", command=add_book)
search_button = Button(window, text="Search Books", command=search_books)
delete_button = Button(window, text="Delete Books", command=delete_books)
update_price_button = Button(window, text="Update Book Prices", command=update_price_books)
reset_button = Button(window, text = "Reset", command = reset)

title_label.grid(row=0, column=0) 
genre_label.grid(row=1, column=0) 
price_label.grid(row=2, column=0)
title.grid(row=0, column=1)
genre.grid(row=1, column=1) 
price.grid(row=2, column=1) 
search_name.grid(row=4, column=0)
add_button.grid(row=3, column=0)
delete_button.grid(row=3, column=1)
update_price_button.grid(row=3, column=2)
reset_button.grid(row=3, column=3)
search_button.grid(row=4, column=1)

list_books()

window.mainloop()