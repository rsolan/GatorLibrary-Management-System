# GatorLibrary-Management-System
## Advanced Data Structures Python Programming Project 


# Introduction

The GatorLibrary Management System is a sophisticated software solution designed to streamline the
operations of a fictional library. It employs a Red-Black tree for organized book inventory management and
Binary Min-heaps for efficient book reservation prioritization. With a suite of functionalities, the system
ensures smooth library operations, covering book management, patron registration, borrowing, and
reservation handling.

Developed using Python, the system leverages advanced data structures and modular programming
principles to manage books, patrons, and reservations seamlessly. This comprehensive report provides an
in-depth analysis of the system's architecture, functionalities, technical implementation, and its impact on
library operations.

# System Architecture

1. Red-Black Tree
The core of the system is a Red-Black tree, a self-balancing binary search tree. This data structure is
chosen for its logarithmic search time, ensuring optimal storage and retrieval of book information.
The Red-Black tree provides an organized and efficient structure for managing the library's vast
inventory.

2. Binary Min-Heap
To handle book reservations, the system incorporates a Binary Min-Heap, a priority queue that
efficiently manages patrons' reservation priorities. This structure ensures that patrons with higher
priority numbers are notified first when a book becomes available, enhancing the reservation
system's effectiveness.

# Detailed System Analysis

1. Book Management-
The system's Book Management module effectively handles the addition, deletion, and retrieval of
books. The Red-Black tree data structure provides efficient storage and search capabilities, ensuring
that book information can be accessed quickly and accurately. The module's ability to maintain
unique bookIDs and availability statuses further enhances book management capabilities.
2. Patron Management-
The Patron Management module effectively manages patron registration and authentication. The
system likely employs a secure database to store patron information and implement authentication
mechanisms to prevent unauthorized access. This ensures the integrity and confidentiality of patron
data.
3. Borrowing Management-
The Borrowing Management module seamlessly handles borrowing and returning of books. The
system's ability to check book availability, update book statuses, and manage patron borrowing
histories demonstrates its effectiveness in tracking book movements within the library.
4. Reservation Management-
The Reservation Management module effectively utilizes Binary Min-heaps to prioritize book
reservations. The system's ability to assign reservations based on patron priority ensures that
patrons with higher priorities are notified first when a book becomes available.

# System Operations

The GatorLibrary Management System provides a comprehensive set of operations for managing books,
patrons, and borrowing operations:
1. PrintBook: Prints information about a specific book identified by its unique bookID.
2. PrintBooks: Prints information about all books with bookIDs in the specified range.
3. InsertBook: Adds a new book to the library, ensuring its unique bookID and availability status.
4. BorrowBook: Allows a patron to borrow a book that is available and updates the status of the book.
If the book is currently unavailable, creates a reservation node in the heap as per the patron's
priority.
5. ReturnBook: Allows a patron to return a borrowed book, updates the book's status, and assigns the
book to the patron with the highest priority in the Reservation Heap if there is a reservation.
6. DeleteBook: Deletes the book from the library and notifies the patrons in the reservation list that the
book is no longer available to borrow.
7. FindClosestBook: Finds the book with an ID closest to the given ID (checking on both sides of the
ID) and prints all its details. In case of ties, prints both books ordered by bookIDs.
8. ColorFlipCount: Tracks the occurrence of color changes in the Red-Black tree nodes during tree
operations, such as insertion, deletion, and rotations.

# Implementation Details

The GatorLibrary Management System is implemented using a modular approach, promoting
maintainability and scalability. The code is well-commented, following established coding standards, and
adopts a clear structure for readability. The system's technical implementation showcases a thoughtful
design, ensuring ease of understanding and future enhancements.

●  Each book is represented as a node in the Red-Black tree, containing BookId, BookName,
AuthorName, AvailabilityStatus, BorrowedBy, and ReservationHeap.

●  ReservationHeap is implemented as a Binary Min-heap, storing (patronID, priorityNumber,
timeOfReservation) for each reservation.

●  Timestamps are used for precise tracking of reservation times.

●  The system terminates when the Quit() operation is encountered.


Clarification for Colorflip count:-

Reservations Handling:
Upon careful inspection, it was observed that the handling of reservations during book borrowing,
returning, and deletion might be contributing to the discrepancy in the Color Flip Count. Specifically, the
logic for canceling reservations and updating the Red-Black Tree needs thorough scrutiny.
In Deletion logic, in the code related to book deletion, especially when a book has reservations the deletion
process adheres to Red-Black Tree properties and effectively manages the cancellation of reservations.
Further in Borrow and Return Logic , The implementation of borrowing and returning books is maintaining
the correct state of the Red-Black Tree and book availability and handling reservations and updating the tree
accordingly. Edge cases such as deleting a node with one child or managing reservations for borrowed
books are also resolving for accurate Color Flip Count calculations. To facilitate the identification of
discrepancies, additional debugging output statements have been strategically introduced in the code. These
statements trace the sequence of operations, the state of the Red-Black Tree, and book statuses.

# Technologies Used:

● Python: The code is implemented using the Python programming language.

● VS Code: The development environment used for writing and debugging the code.

# Steps to Run:
1) Unzip folder and open the folder.
2) Run Terminal in that directory and run one of the following command:
   python your_script.py
<Input_FileName>

python gatorLibrary.py test.txt

python3 gatorLibrary.py test.txt

3) Find the output file test_output_file.txt generated by the code

# Code structure

The code implements a library management system with features for managing books, patrons, and
reservations. It utilizes a Red-Black Tree for efficient book management and a Binary Min-Heap to
prioritize and manage book reservations.
1. HeapNode
● Represents a node in the Binary Min-Heap used for managing reservations.
● Contains attributes such as book_id, patron_id, priority_number, and time_of_reservation.
● Implements the less-than (__lt__) method for comparison based on priority.

2. RBNode
● Represents a node in the Red-Black Tree used for efficient book storage.
● Contains attributes like book_id, book_name, author_name, availability_status, borrowed_by, and
reservation_heap.
● Implements methods for inserting and extracting reservations, printing book details, and managing
reservations.

3. BinaryMinHeap
● Implements a Binary Min-Heap for managing reservations.
● Contains methods for insertion, extraction of the minimum reservation, and heapifying up and
down.
● Also includes methods for printing the heap and finding existing reservations.

4. RedBlackTree
● Manages the Red-Black Tree used for efficient book storage and retrieval.
● Implements methods for left and right rotation, inserting, fixing up after insertion, transplanting
nodes, deleting nodes, fixing up after deletion, searching, finding the minimum, printing the tree,
and finding the closest book.

5. GatorLibrary
● Serves as the main interface for the library management system.
● Utilizes the Red-Black Tree for book management.
● Implements methods for printing book details, borrowing, returning, deleting books, finding the
closest book, and handling program termination.

# Conclusion

The GatorLibrary Management System stands as a testament to efficient and well-organized library
management. By leveraging advanced data structures and incorporating a comprehensive set of
functionalities, the system caters to the diverse needs of libraries. Its modular design, clear codebase, and
impactful features position it as a valuable tool for libraries seeking to optimize their operations and
enhance the overall user experience. The GatorLibrary Management System is a testament to the power of
thoughtful software design in the realm of library management.
