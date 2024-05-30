from datetime import datetime
import sys


class HeapNode:
    def __init__(self, book_id, patron_id, priority_number, time_of_reservation=None):
        self.book_id = book_id
        self.patron_id = patron_id
        self.priority_number = priority_number
        self.time_of_reservation = time_of_reservation

    def __lt__(self, other):
        return self.priority_number < other.priority_number
    
    def __str__(self):
        return f"({self.patron_id},{self.priority_number},{self.time_of_reservation})"



       
# self.color = 'RED'  # New nodes are always red


class RBNode:
    def __init__(self, book_id, book_name, author_name, availability_status, borrowed_by, reservation_heap=None, color='B', parent=None, left=None, right=None):
        self.book_id = book_id
        self.book_name = book_name
        self.author_name = author_name
        self.availability_status = availability_status
        self.borrowed_by = borrowed_by
        self.reservation_heap = reservation_heap if reservation_heap is not None else BinaryMinHeap()
        self.color = color  # 'R' for red, 'B' for black
        self.parent = parent
        self.left = left
        self.right = right


    def insert_reservation(self, patron_id, priority_number, time_of_reservation):
        reservation_node = HeapNode(self.book_id, patron_id, priority_number, time_of_reservation)
        self.reservation_heap.insert(reservation_node)

    def extract_min_reservation(self):
        return self.reservation_heap.extract_min()
    
    def print_book_details(self):
        details = (
            f"BookID = {self.book_id}\n"
            f"Title = {self.book_name}\n"
            f"Author = {self.author_name}\n"
            f"Availability = {self.availability_status}\n"
            f"BorrowedBy = {self.borrowed_by}\n"
        )

        reservations = self.reservation_heap.heap
        reservations = [reservation for reservation in reservations if reservation is not None]
        reservations = sorted(reservations, key=lambda reservation: (reservation.priority_number, reservation.time_of_reservation) )
        if any(reservations):
            details += "Reservations = ["
            details += ", ".join(str(reservation.patron_id) for reservation in reservations if reservation is not None)
            details += "]\n"
        else:
            details += "Reservations = []\n"

        return details

    def print_reservations(self):
        """
        Print information about reservations for the book.
        """
        if not self.reservation_heap.is_empty():
            print("Reservations:")
            for reservation in self.reservation_heap.heap:
                print(f"Patron ID: {reservation.patron_id}, Priority: {reservation.priority_number}, Reservation Time: {reservation.time_of_reservation}")
        else:
            print("No reservations for this book.")

class BinaryMinHeap:
    def __init__(self, max_size=20):
        self.max_size = max_size
        self.size = 0
        self.heap = [None] * (max_size + 1)  # 1-indexed heap for easier calculations

    def is_empty(self):
        return self.size == 0

    def find_min(self):
        if self.is_empty():
            return None
        return self.heap[1]

    def get_size(self):
        return self.size

    def insert(self, node):
        if self.size == self.max_size:
            print("Heap is full. Cannot insert more reservations.")
            return

        self.size += 1
        i = self.size
        self.heap[i] = node
        
        self.heapify_up(i)
       


    def extract_min(self):

        if self.is_empty():
            return None

        min_node = self.heap[1]
        last_node = self.heap[self.size]
        self.size -= 1
        self.heap[1] = last_node
        self.heap[self.size+1]=None
        self.heapify_down(1)



        return min_node

    def heapify_up(self, i):
        while i > 1 and self.heap[i // 2].priority_number > self.heap[i].priority_number:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i //= 2

    def heapify_down(self, i):
        while i * 2 <= self.size:
            child = i * 2
            if child + 1 <= self.size and self.heap[child + 1].priority_number < self.heap[child].priority_number:
                child += 1

            if self.heap[i].priority_number > self.heap[child].priority_number:
                self.heap[i], self.heap[child] = self.heap[child], self.heap[i]
            else:
                break

            i = child

        

    def print_heap(self):
        print("Reservation Heap:")
        for i in range(1, self.size + 1):
            node = self.heap[i]
            print(f"Patron ID: {node.patron_id}, Priority: {node.priority_number}, Reservation Time: {node.time_of_reservation}")

    def find_existing_reservation(self, patron_id):
        for node in self.heap[1:]:
            if node and node.patron_id == patron_id:
                return node
        return None



class RedBlackTree:
    def __init__(self):
        self.NIL = RBNode(None, None, None, None, None, None, 'B')  # NIL node for leaves
        self.root = self.NIL
        self.color_flips = 0  # Initialize color flip count


    def left_rotate(self, x):
        y = x.right
        x.right = y.left

        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent

        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y
        # Increment color flip count after rotation
        self.color_flip_count()

    def right_rotate(self, y):
        x = y.left
        y.left = x.right

        if x.right != self.NIL:
            x.right.parent = y

        x.parent = y.parent

        if y.parent == self.NIL:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        x.right = y
        y.parent = x
        # Implementing color_flip_count for rotation methods
        self.color_flip_count()  



    def insert(self, z):
        y = self.NIL
        x = self.root

        while x != self.NIL:
            y = x
            if z.book_id < x.book_id:
                x = x.left
            else:
                x = x.right

        z.parent = y

        if y == self.NIL:
            self.root = z
        elif z.book_id < y.book_id:
            y.left = z
        else:
            y.right = z

        z.left = self.NIL
        z.right = self.NIL
        z.color = 'R'  # New nodes are always colored red
        self.insert_fixup(z)

    def insert_fixup(self, z):
        while z.parent.color == 'R':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'R':
                    z.parent.color = 'B'
                    y.color = 'B'
                    z.parent.parent.color = 'R'
                    z = z.parent.parent
                    self.color_flip_count()  # Increment color flip count
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                        self.color_flip_count()  # Increment color flip count

                    z.parent.color = 'B'
                    z.parent.parent.color = 'R'
                    self.right_rotate(z.parent.parent)
                    self.color_flip_count()  # Increment color flip count
            else:
                y = z.parent.parent.left
                if y.color == 'R':
                    z.parent.color = 'B'
                    y.color = 'B'
                    z.parent.parent.color = 'R'
                    z = z.parent.parent
                    self.color_flip_count()  # Increment color flip count
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                        self.color_flip_count()  # Increment color flip count

                    z.parent.color = 'B'
                    z.parent.parent.color = 'R'
                    self.left_rotate(z.parent.parent)
                    self.color_flip_count()  # Increment color flip count

        self.root.color = 'B'
        



    def transplant(self, u, v):
        if u.parent == self.NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        v.parent = u.parent

    def delete(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == 'B':
            self.delete_fixup(x)

    
    def delete_fixup(self, x):
        while x != self.root and x.color == 'B':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'R':
                    w.color = 'B'
                    x.parent.color = 'R'
                    self.left_rotate(x.parent)
                    w = x.parent.right
                    self.color_flip_count()  # Increment color flip count

                if w.left.color == 'B' and w.right.color == 'B':
                    w.color = 'R'
                    x = x.parent
                else:
                    if w.right.color == 'B':
                        w.left.color = 'B'
                        w.color = 'R'
                        self.right_rotate(w)
                        w = x.parent.right
                        self.color_flip_count()  # Increment color flip count

                    w.color = x.parent.color
                    x.parent.color = 'B'
                    w.right.color = 'B'
                    self.left_rotate(x.parent)
                    x = self.root
                    self.color_flip_count()  # Increment color flip count
            else:
                w = x.parent.left
                if w.color == 'R':
                    w.color = 'B'
                    x.parent.color = 'R'
                    self.right_rotate(x.parent)
                    w = x.parent.left
                    self.color_flip_count()  # Increment color flip count

                if w.right.color == 'B' and w.left.color == 'B':
                    w.color = 'R'
                    x = x.parent
                else:
                    if w.left.color == 'B':
                        w.right.color = 'B'
                        w.color = 'R'
                        self.left_rotate(w)
                        w = x.parent.left
                        self.color_flip_count()  # Increment color flip count

                    w.color = x.parent.color
                    x.parent.color = 'B'
                    w.left.color = 'B'
                    self.right_rotate(x.parent)
                    x = self.root
                    self.color_flip_count()  # Increment color flip count

        x.color = 'B'
        


    def search(self, key):
        return self._search(self.root, key)

    def _search(self, x, key):
        if x == self.NIL or key == x.book_id:
            return x
        if key < x.book_id:
            return self._search(x.left, key)
        return self._search(x.right, key)

    def minimum(self, x):
        while x.left != self.NIL:
            x = x.left
        return x

    def print_tree(self, x, indent=0, title="Root"):
        if x != self.NIL:
            print("  " * indent + title + f" ({x.color}): {x.book_id}")
            print("  " * (indent + 1) + f"Title: {x.book_name}")
            print("  " * (indent + 1) + f"Author: {x.author_name}")
            print("  " * (indent + 1) + f"Availability: {x.availability_status}")
            print("  " * (indent + 1) + f"Borrowed By: {x.borrowed_by}")
            print("  " * (indent + 1) + "Reservations: ", end="")
            for reservation in x.reservation_heap.heap:
                print(reservation.patron_id, end=" ")
            print()
            self.print_tree(x.left, indent + 1, "Left")
            self.print_tree(x.right, indent + 1, "Right")

   

    def delete_node(self, book_id):
        z = self.search(book_id)
        if z != self.NIL:
            self.delete(z)
            print(f"Book {book_id} is no longer available.")
        else:
            print(f"Book {book_id} not found in the Library.")

    def successor(self, x):
        if x.right != self.NIL:
            return self.minimum(x.right)

        y = x.parent
        while y != self.NIL and x == y.right:
            x = y
            y = y.parent
        return y

    def find_closest_book(self, target_id):
        x = self.root
        closest_left = None
        closest_right = None

        while x != self.NIL:
            if x.book_id == target_id:
                return x

            # Check both sides of the target ID
            if target_id < x.book_id:
                closest_right = x
                x = x.left
            else:
                closest_left = x
                x = x.right

        # Check which side is closer
        if closest_left is not None and closest_right is not None:
            distance_left = abs(target_id - closest_left.book_id)
            distance_right = abs(target_id - closest_right.book_id)

            # return closest_left if distance_left < distance_right else closest_right
            return (closest_left, closest_right) if distance_left == distance_right else closest_left if distance_left < distance_right else closest_right

        elif closest_left is not None:
            return closest_left
        elif closest_right is not None:
            return closest_right

        return None  # No closest node found


    def color_flip_count(self):
        self.color_flips += 1

    
    def get_all_books(self):
        books = []
        self._get_all_books(self.root, books)
        return books

    def _get_all_books(self, node, book_list):
        if node != self.NIL:
            self._get_all_books(node.left, book_list)
            book_list.append(node)
            self._get_all_books(node.right, book_list)

    def get_books_in_range(self, low, high):
        books = []
        self._get_books_in_range(self.root, low, high, books)
        return books

    def _get_books_in_range(self, node, low, high, book_list):
        if node != self.NIL:
            if low <= node.book_id <= high:
                self._get_books_in_range(node.left, low, high, book_list)
                book_list.append(node)
                self._get_books_in_range(node.right, low, high, book_list)
            elif node.book_id < low:
                self._get_books_in_range(node.right, low, high, book_list)
            else:
                self._get_books_in_range(node.left, low, high, book_list)



class GatorLibrary:
    def __init__(self):
        self.red_black_tree = RedBlackTree()

    def print_book(self, book_id):
        book = self.red_black_tree.search(book_id)
        if book != self.red_black_tree.NIL:
            return book.print_book_details()
        else:
            return f"Book {book_id} not found in the Library"

    def print_books(self, book_id1, book_id2):
        books = self.red_black_tree.get_books_in_range(int(book_id1), int(book_id2))
        return books
    
    def insert_book(self, book_id, book_name, author_name, availability_status, borrowed_by, reservation_heap=None):
        book = self.red_black_tree.search(book_id)

        if book == self.red_black_tree.NIL:
            # Book not found, create and insert a new book
            new_book = RBNode(book_id, book_name, author_name, availability_status, borrowed_by, reservation_heap)
            self.red_black_tree.insert(new_book)
            # No print statement here
    
    def borrow_book(self, patron_id, book_id, patron_priority):
        book = self.red_black_tree.search(book_id)

        if book != self.red_black_tree.NIL:
            if book.availability_status == '"Yes"':
                # Book is available, allow borrowing
                book.availability_status = '"No"'
                book.borrowed_by = patron_id
                return f"Book {book_id} Borrowed by Patron {patron_id}"
            else:
                # Book is not available, check if there's an existing reservation
                existing_reservation = book.reservation_heap.find_existing_reservation(patron_id)

                if existing_reservation:
                    # Update the existing reservation priority
                    existing_reservation.priority_number = patron_priority
                else:
                    # Add a new reservation
                    reservation_node = HeapNode(book_id, patron_id, patron_priority, datetime.now())
                    book.reservation_heap.insert(reservation_node)

                return f"Book {book_id} Reserved by Patron {patron_id}"
        else:
            return f"Book {book_id} not found in the Library"

    def return_book(self, patron_id, book_id):
        book = self.red_black_tree.search(book_id)

        if book != self.red_black_tree.NIL:
            if book.borrowed_by == patron_id:
                # Book is returned by the patron

                # Check if there are reservations
                if not book.reservation_heap.is_empty():
                    # There are reservations, assign the book to the next patron in line
                    top_reservation = book.reservation_heap.extract_min()
                    book.borrowed_by = top_reservation.patron_id
                    book.availability_status = '"No"'
                    return f"Book {book_id} Returned by Patron {patron_id}\nBook {book_id} Allotted to Patron {top_reservation.patron_id}"
                else:
                    # No reservations, set the availability status to 'Yes'
                    book.availability_status = '"Yes"'
                    book.borrowed_by = None
                    return f"Book {book_id} Returned by Patron {patron_id}"
            else:
                return f"Book {book_id} not borrowed by Patron {patron_id}"
        else:
            return f"Book {book_id} not found in the Library"

    def delete_book(self, book_id):
        book = self.red_black_tree.search(book_id)
        if book != self.red_black_tree.NIL:
            if not book.reservation_heap.is_empty():
                reservations = [reservation.patron_id for reservation in book.reservation_heap.heap if reservation is not None]
                if len(reservations) > 1:
                    self.red_black_tree.delete(book)
                    return f"Book {book_id} is no longer available. Reservations made by Patrons {', '.join(map(str, reservations))} have been cancelled!"
                elif len(reservations) == 1:
                    self.red_black_tree.delete(book)
                    return f"Book {book_id} is no longer available. Reservation made by Patron {reservations[0]} has been cancelled!"
                else:
                    self.red_black_tree.delete(book)
                    return f"Book {book_id} is no longer available."
            else:
                self.red_black_tree.delete(book)
                return f"Book {book_id} is no longer available."
        else:
            return f"Book {book_id} not found in the Library"

    def find_closest_book(self, target_id):
        closest_books = self.red_black_tree.find_closest_book(target_id)

        if isinstance(closest_books, tuple):
            return "\n".join(book.print_book_details() for book in closest_books)
        elif closest_books != self.red_black_tree.NIL:
            return closest_books.print_book_details()
        else:
            return "No closest book found"
        
    def quit_program(self):
        print("Program Terminated!!")

    def color_flip_count(self):
        print(f"Colour Flip Count: {self.red_black_tree.color_flips}")

    def get_all_books(self):
        books = self.red_black_tree.get_all_books()
        for book in books:
            print(book.print_book_details())





def parse_command(line):
    parts = line.strip().split("(")
    if len(parts) < 2:
        # Handle cases where there are not enough parts
        return None, None
    command = parts[0]
    args = "".join(parts[1:])  # Concatenate all parts after the command
    args = args.rstrip(";")  # Remove semicolon, if present
    args = args.rstrip(")")  # Remove the closing parenthesis
    args_list = [arg.strip() for arg in args.split(",")]
    return command, args_list


def main(input_filename):
    library = GatorLibrary()
    quit_flag=0

    # Read input from the file
    with open(input_filename, "r") as file:
        lines = file.readlines()
        output_lines = []
        
        for line in lines:
            command, args = parse_command(line)
            # print(line)
            output_line = None
            if(quit_flag==0):
                if command == "Quit":
                    library.quit_program()
                    output_line = "Program Terminated!!"
                    quit_flag=1

                elif command == "InsertBook":
                    book_id, title, author, availability = map(str.strip, args[:4])
                    library.insert_book(int(book_id), title, author, availability, None, BinaryMinHeap())
                    output_line = "" 
                    # No output for InsertBook command

                elif command == "PrintBook":
                    book_id = args[0]
                    book_details = library.print_book(int(book_id))
                    output_line = book_details if book_details is not None else f"Book {book_id} not found in the Library"

                elif command == "PrintBooks":
                    book_id1, book_id2 = map(int, args)
                    books = library.print_books(book_id1, book_id2)
                    output_line=""
                    output_lines.extend([f"{book.print_book_details()}" for book in books])


                elif command == "BorrowBook":
                    patron_id, book_id, priority = map(int, args)
                    output_line = library.borrow_book(patron_id, book_id, priority)

                elif command == "ReturnBook":
                    patron_id, book_id = map(int, args)
                    output_line = library.return_book(patron_id, book_id)

                elif command == "DeleteBook":
                    book_id = int(args[0])
                    output_line = library.delete_book(book_id)

                elif command == "FindClosestBook":
                    target_id = int(args[0])
                    output_line = library.find_closest_book(target_id)

                elif command == "ColorFlipCount":
                    output_line = f"Colour Flip Count: {library.red_black_tree.color_flips}"
            if(output_line!=None):
                output_lines.append(output_line)

    # Write output to a text file
    output_filename = f"{input_filename.split('.')[0]}_output_file.txt"
    with open(output_filename, "w") as output_file:
        for output_line in output_lines:
            print(output_line, file=output_file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python your_script.py input_filename")
        sys.exit(1)

    input_filename = sys.argv[1]
    main(input_filename)











