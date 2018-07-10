class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("The email address for user " + self.user + "has been changed to " + self.email)

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        total_rating = 0
        num_books = 0
        #total_rating = 0
        for value in self.books.values():
            if value:
                total_rating += value
                num_books += 1
        avg = total_rating / num_books  
        return avg

    def __repr__(self):
        return self.name + ", email: " + self.email + ", books read: " + str(len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user and self.email == other_user.email:
            return True
        else:
            return False

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("The book: " + self.title + " has been updated with isbn: " + str(self.isbn))

    def add_rating(self, rating):
        if rating and rating > 0 and rating <= 4:
            print(rating)
            self.ratings.append(rating)
        else:
            return "Invalid Rating"

    def get_average_rating(self):
        avg = 0
        #rated_books = 0
        for rating in self.ratings:
                avg += rating
        avg = avg/len(self.ratings)
        return avg

    def __eq__(self, compare_book):
        if self.title == compare_book.title and self.isbn == compare_book.isbn:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return(self.title)


class Fiction(Book):
    def __init__(self, title, author, isbn):
        Book.__init__(self, title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return str(self.title) + " by " + str(self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        Book.__init__(self, title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return self.title + ", a " + self.level + " on " + self.subject

class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        #self.title = title
        #self.isbn = isbn 
        new_book = Book(title, isbn)
        return new_book

    def create_novel(self, title, author, isbn):
        #self.title = title
        #self.author = author
        #self.isbn = isbn 
        new_book = Fiction(title, author, isbn)
        return new_book

    def create_non_fiction(self, title, subject, level, isbn):
        #self.title = title
        #self.subject = subject
        #self.level = level
        new_book = Non_Fiction(title, subject, level, isbn)
        return new_book

    def add_book_to_user(self, book, email, rating=None):
        user = self.users.get(email, None)
        if user:
            user.read_book(book, rating)
            if book not in self.books:
                self.books[book] = 0
            self.books[book] += 1  
            book.add_rating(rating) 
            print("Adding rating " + str(rating) + " to book " + str(book)) 
        else:
            print("No user with email " + email)


    def add_user(self, name, email, user_books=None):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books:
            print(str(book))

    def print_ratings(self):
        for book in self.books:
            print(book +" Rating: " + str(rating))

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        highest_read = 0
        book_most_read = None
        for book in self.books:
            num_read = self.books[book]
            if num_read > highest_read:
                num_read = highest_read
                book_most_read = book
        return book_most_read

    def highest_rated_book(self):
        highest_rating = float("-inf")
        book_highest_rating = None
        for book in self.books:
            book_rating = book.get_average_rating()
            if book_rating > highest_rating:
                highest_rating = book_rating
                book_highest_rating = book
        return book_highest_rating

    def most_positive_user(self):
        highest_rating = float("-inf")
        user_highest_rating = None
        for user in self.users.values():
            user_rating = user.get_average_rating()
            if user_rating > highest_rating:
                highest_rating = user_rating
                user_highest_rating = user
        return user_highest_rating

#Adding comment 
#Adding another comment











