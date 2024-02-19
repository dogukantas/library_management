

class Library:
    def __init__(self):
        #books.txt dosyasını read ve append modunda aç
        self.file = open('books.txt', 'a+')

    def __del__(self):
        #books.txt dosyasını kapat
        self.file.close()

    def list_books(self):  
        # dosya ve kitapları listele
        self.file.seek(0)  
        books = self.file.read().splitlines()
        for book in books:
            title, author, year, pages = book.split(',')
            print(f"Title: {title}, Author: {author}")

    def add_book(self):
        #books.txt dosyasına kitap ekle
        title = input("Enter the book title: ")
        author = input("Enter the author: ")
        year = input("Enter the first release year: ")
        pages = input("Enter the number of pages: ")
        self.file.write(f"{title},{author},{year},{pages}\n")

    def remove_book(self):
        #books.txt dosyasından kitap sil
        title_to_remove = input("Enter the book title to remove: ")
        self.file.seek(0)
        books = self.file.read().splitlines()

        #Silinecek kitabın indexini bul
        book_index = None
        for index, book in enumerate(books):
            title, _, _, _ = book.split(',')
            if title == title_to_remove:
                book_index = index
                break

        if book_index is not None:
            #kitabı listeden sil
            books.pop(book_index)
            self.file.seek(0)
            self.file.truncate()
            for book in books:
                self.file.write(book + "\n")
            print(f"Book titled '{title_to_remove}' has been removed.")
        else:
            print("Book not found.")

    def update_book(self):
        #Mevcut herhangi kitabn bilgilerini güncelle
        title_to_update = input("Enter the book title to update: ")
        self.file.seek(0)
        books = self.file.read().splitlines()

        #Güncellenecek kitabın indexini bul
        book_index = None
        for index, book in enumerate(books):
            title, _, _, _ = book.split(',')
            if title == title_to_update:
                book_index = index
                break

        if book_index is not None:
            #Güncellenecek kitabın yeni bilgilerini al
            new_title = input("Enter new book title: ")
            new_author = input("Enter new author: ")
            new_year = input("Enter new release year: ")
            new_pages = input("Enter new number of pages: ")

            #Güncellenmiş bilgileri hazırla
            book_data = books[book_index].split(',')
            if new_title:
                book_data[0] = new_title
            if new_author:
                book_data[1] = new_author
            if new_year:
                book_data[2] = new_year
            if new_pages:
                book_data[3] = new_pages

            #Güncellenmiş kitabı listeye ekle
            books[book_index] = ','.join(book_data)

            #Dosyayı güncelle
            self.file.seek(0)
            self.file.truncate()
            for book in books:
                self.file.write(book + "\n")
            print(f"Book titled '{title_to_update}' has been updated.")
        else:
            print("Book not found.")


lib = Library()

# Kullanıcı menüsü
while True:
    print("*** MENU ***\n1) List Books\n2) Add Book\n3) Remove Book\n4) Update Book")
    choice = input("Enter your choice: ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == '4':
        lib.update_book()
    else:
        print("Invalid choice")

    if input("Do you want to continue? (y/n): ").lower() != 'y':
        break

del lib  # dosyayı kapat


# __init__: Library sınıfının bir örneği oluşturulduğunda, books.txt dosyasını hem okuma hem de yazma modunda açar. Dosya mevcut değilse bu mod yeni bir dosya oluşturur.
# __del__: Nesne silindiğinde books.txt dosyasını kapatır.

# list_books Metodu:
# Dosyanın içeriğini okur ve her satırı bir kitabın bilgilerini içeren bir liste elemanına dönüştürür.
# Kitapların başlıklarını ve yazarlarını ekrana basar.

# add_book Metodu:
# Kullanıcıdan kitabın başlığı, yazarı, ilk yayın yılı ve sayfa sayısı bilgilerini alır.
# Bu bilgileri, belirtilen formatta dosyaya ekler.

# remove_book Metodu:
# Kullanıcıdan silinecek kitabın başlığını alır.
# Dosyayı okuyarak kitapları bir listeye ekler ve silinecek kitabın indeksini bulur.
# Kitabı listeden siler ve dosyanın içeriğini günceller.


#######Çeşitlilik olması adına eklenmiştir#################
# update_book Metodu:
# Kullanıcıdan güncellenecek kitabın mevcut başlığını alır.
# Dosyadan kitapların listesini alır ve güncellenecek kitabın indeksini bulur.
# Kullanıcıdan kitabın yeni bilgilerini alır ve bu bilgilerle kitabı günceller.
# Temel gereksinimler arasında yer almıyor ama kullanışlı bir özellik sunuyor.

# Kullanıcı Menüsü:
# Kullanıcılara kitap listeleme, ekleme, silme ve güncelleme seçenekleri sunan bir döngü içerir.
# Kullanıcının seçimine göre ilgili Library metodunu çağırır.