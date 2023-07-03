class Bookstore:
    def __init__(self, title, genre, price):
        self.title = title
        self.genre = genre
        self.price = price

    def __str__(self):
        return f"Title: {self.title}, Genre: {self.genre}, Price: {self.price}"
    
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Book Management System")
window.geometry("600x200")


book_list = []

# adding book
def add_book():
    title_entry = title.get()
    genre_entry = genre.get()
    price_entry = price.get()

    if title_entry == "" or genre_entry == "" or  price_entry == "":
        messagebox.showerror("Add Book", "Please enter all three blank space")
    else:
        new_book = Bookstore(title_entry, genre_entry, int(price_entry))
        book_list.append(new_book)
        list_books()
        messagebox.showinfo("Book added", f"Added {new_book}")

# removing books
def delete_books():
    delete_title = title.get()
    found_book = False 
    
    if delete_title == "":
        messagebox.showerror("Delete Book","Please enter book title!!!")
    else:
        for i in range(len(book_list)):
            if book_list[i].title == delete_title:
                del book_list[i]
                list_books()
                messagebox.showinfo("Delete Book", f"Delete{delete_title} succesfully")
                found_book = True
                break
                
            if found_book == False:
                messagebox.showerror("Delete Book", "Cannot find this book!!")

# searching for books
def search_books():
    search_book = title.get()
    check = False
    
    if search_book == "":
        messagebox.showerror("Search Book", "Please enter book title!!!")
    else:
        for book in book_list:
            if book.title == search_book:
                list_books()
                messagebox.showinfo("Search Book", f"Name: {book.title}, genre: {book.genre}, price: {book.price}")
                check = True
                break
            
        if check == False: 
            messagebox.showerror("Search Book", "Cannot find this book!!!")

# updating book prices
# def update_price_books():
    # book_title_price_update = title.get()
    # price_update = price.get()                                
    # found_books = False

#     if book_title_price_update == "" or price_update == "" :
#         messagebox.showerror("Update Book Prices", "Please enter book title and price needed to be update")
#     else:
#         for book in book_list:
#             if book.title == book_title_price_update:
#                 book.price = int(price_update)
#                 list_books()
#                 messagebox.showinfo("Update Book Prices", f"Updated price of {book_title_price_update} to {price_update}.")
#                 found_books = True
#             else:
#                 messagebox.showinfo("Update Book Prices", "No books found.")

def update_price_dialog():
    book_title_price_update = title.get()
    price_update = price.get()                                
    found_books = False
    
    
    if book_title_price_update == "" or price_update == "":
        messagebox.showerror("Update Book Prices", "Please enter book title and price needed to be update")
    else:
        update_window = Tk()
        update_window.title("Update Price")
        update_window.geometry("400x200")
        update_price = Entry(update_window)
        
        original_price = price.get()
        original_price_label = Label(update_window, text=f"Old Price: {original_price}")
        original_price_label.grid(row=0, column=0)
        
        update_price_label = Label(update_window, text="Update To:")
        update_price_label.grid(row=1, column=0)
        update_price.grid(row=1, column=1)


        
        # update_price_entry = update_price.get()

        def update_price_books():
            book_title_price_update = title.get()
            update_price_entry = update_price.get()
            price_update = price.get()                                
            found_books = False

            for book in book_list:
                if book.title == book_title_price_update:
                    print('Book price:', book.price)
                    print('Ol')
                    print('Update price entry', update_price_entry)
                    book.price = int(update_price_entry)
                    list_books()
                    messagebox.showinfo("Update Book Prices", f"Updated price of {book_title_price_update} to {update_price_entry}.")
                    found_books = True
                    update_window.destroy()
                else:
                    messagebox.showinfo("Update Book Prices", "No books found.")

        update_price_button = Button(update_window, text="Update Book Prices", command=update_price_books)
        update_price_button.grid(row=3, column=0)
        
        print(original_price)
        update_window.mainloop()



# reset to beginning
def reset():
    title.delete(0, "end")
    genre.delete(0,"end")                                    
    price.delete(0,"end")
    search_name.delete(0,"end")  

# listing all books in console
def list_books():
    for book in book_list:
        print('*' * 20, end="\n")
        print('Title:', book.title)
        print('Genre:', book.genre)
        print('Price:', book.price)
      
        
title_label = Label(window, text="Title:")
genre_label = Label(window, text="Genre:")
price_label = Label(window, text="Price:")

title = Entry(window)
genre = Entry(window)
price = Entry(window)

search_name = Entry(window)

add_button = Button(window, text="Add Book", command=add_book)
search_button = Button(window, text="Search Books", command=search_books)
delete_button = Button(window, text="Delete Books", command=delete_books)
update_price_dialog_button = Button(window, text="Update Book Prices", command=update_price_dialog)
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
update_price_dialog_button.grid(row=3, column=2)
reset_button.grid(row=3, column=3)
search_button.grid(row=4, column=1)

window.mainloop()