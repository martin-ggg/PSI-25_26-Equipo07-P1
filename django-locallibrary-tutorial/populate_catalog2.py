"""
Script intended to populate the DB (extended version)
Based on populate_catalog.py (original authors/books retained)
Adds extra *real* authors/books and significantly more BookInstance rows (>= 300% more than original).

Created by JAMI (original)
Extended by MG
EPS-UAM 2026
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'locallibrary.settings')

import django
django.setup()

from catalog.models import Book, BookInstance, Language, Genre, Author

from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
import warnings

# Dummy Privileged user for restricted operations: Library Supervisor
DP_USER     = "LibSupervisor"
DP_PASSWORD = "LibSupervisor_234"


def clean_db():
    # IMPORTANT: this wipes existing catalog data
    BookInstance.objects.all().delete()
    Book.objects.all().delete()
    Author.objects.all().delete()
    Genre.objects.all().delete()
    Language.objects.all().delete()


def populate():
    # --- Languages ---
    languages = [
        {'name': 'English'},
        {'name': 'Spanish'},
        {'name': 'French'},
        {'name': 'German'},
        {'name': 'Japanese'},
    ]

    # --- Genres ---
    genres = [
        {'name': 'Horror'},
        {'name': 'Thriller'},
        {'name': 'Science Fiction'},
        {'name': 'Historical'},
        {'name': 'Fantasy'},
        {'name': 'Mystery'},
        {'name': 'Romance'},
        {'name': 'Classics'},
        {'name': 'Magical Realism'},
        {'name': 'Dystopian'},
    ]

    # --- Authors (original + extra real authors) ---
    authors = [
        # Original authors
        {'first_name': 'Stephen', 'last_name': 'King', 'date_of_birth': '1947-09-21', 'date_of_death': ''},
        {'first_name': 'Isaac', 'last_name': 'Asimov', 'date_of_birth': '1920-01-02', 'date_of_death': '1992-05-06'},

        # Extra real authors
        {'first_name': 'George', 'last_name': 'Orwell', 'date_of_birth': '1903-06-25', 'date_of_death': '1950-01-21'},
        {'first_name': 'Jane', 'last_name': 'Austen', 'date_of_birth': '1775-12-16', 'date_of_death': '1817-07-18'},
        {'first_name': 'Agatha', 'last_name': 'Christie', 'date_of_birth': '1890-09-15', 'date_of_death': '1976-01-12'},
        {'first_name': 'J.R.R.', 'last_name': 'Tolkien', 'date_of_birth': '1892-01-03', 'date_of_death': '1973-09-02'},
        {'first_name': 'J.K.', 'last_name': 'Rowling', 'date_of_birth': '1965-07-31', 'date_of_death': ''},
        {'first_name': 'Gabriel', 'last_name': 'García Márquez', 'date_of_birth': '1927-03-06', 'date_of_death': '2014-04-17'},
        {'first_name': 'Haruki', 'last_name': 'Murakami', 'date_of_birth': '1949-01-12', 'date_of_death': ''},
        {'first_name': 'Mary', 'last_name': 'Shelley', 'date_of_birth': '1797-08-30', 'date_of_death': '1851-02-01'},
    ]

    # Helper to reference author names cleanly
    def A(fn, ln):
        return {'first_name': fn, 'last_name': ln}

    # --- Books (original + extra real books) ---
    # NOTE: Ensure 'genre' is ALWAYS a list to avoid accidental per-character iteration.
    books = [
        # Original books
        {
            'title': 'The Shining',
            'summary': 'A writer becomes winter caretaker of the isolated Overlook Hotel; unsettling forces test his sanity and his family.',
            'author': A(authors[0]['first_name'], authors[0]['last_name']),
            'isbn': '9780345806789',
            'genre': ['Horror', 'Thriller'],
            'language': 'English',
        },
        {
            'title': 'Cementerio de Animales',
            'summary': 'Un médico descubre un cementerio inquietante: lo que entierra allí puede volver… pero no igual.',
            'author': A(authors[0]['first_name'], authors[0]['last_name']),
            'isbn': '9780450057694',
            'genre': ['Horror'],
            'language': 'Spanish',
        },
        {
            'title': 'I, Robot',
            'summary': 'A collection of stories exploring the Three Laws of Robotics and the impact of robots on human society.',
            'author': A(authors[1]['first_name'], authors[1]['last_name']),
            'isbn': '9780194242363',
            'genre': ['Science Fiction'],
            'language': 'English',
        },
        {
            'title': 'Viaje Alucinante',
            'summary': 'Una misión de miniaturización en plena Guerra Fría se convierte en una carrera contra el tiempo dentro del cuerpo humano.',
            'author': A(authors[1]['first_name'], authors[1]['last_name']),
            'isbn': '9780553275728',
            'genre': ['Science Fiction'],
            'language': 'Spanish',
        },

        # Extra real books
        {
            'title': '1984',
            'summary': 'A dystopian novel about surveillance, propaganda, and the struggle for truth under a totalitarian regime.',
            'author': A('George', 'Orwell'),
            'isbn': '9780451524935',
            'genre': ['Dystopian', 'Classics'],
            'language': 'English',
        },
        {
            'title': 'Animal Farm',
            'summary': 'An allegorical novella where farm animals stage a revolution—only to face new forms of oppression.',
            'author': A('George', 'Orwell'),
            'isbn': '9780451526342',
            'genre': ['Classics'],
            'language': 'English',
        },
        {
            'title': 'Pride and Prejudice',
            'summary': 'A classic romance exploring manners, upbringing, and love in early 19th-century England.',
            'author': A('Jane', 'Austen'),
            'isbn': '9780141439518',
            'genre': ['Romance', 'Classics'],
            'language': 'English',
        },
        {
            'title': 'Murder on the Orient Express',
            'summary': 'Detective Hercule Poirot investigates a murder aboard the luxurious Orient Express.',
            'author': A('Agatha', 'Christie'),
            'isbn': '9780062693662',
            'genre': ['Mystery', 'Classics'],
            'language': 'English',
        },
        {
            'title': 'The Hobbit',
            'summary': 'Bilbo Baggins is swept into an epic quest with dwarves to reclaim their homeland from a dragon.',
            'author': A('J.R.R.', 'Tolkien'),
            'isbn': '9780547928227',
            'genre': ['Fantasy', 'Classics'],
            'language': 'English',
        },
        {
            'title': "Harry Potter and the Philosopher's Stone",
            'summary': 'A boy discovers he is a wizard and begins his first year at Hogwarts School of Witchcraft and Wizardry.',
            'author': A('J.K.', 'Rowling'),
            'isbn': '9780747532699',
            'genre': ['Fantasy'],
            'language': 'English',
        },
        {
            'title': 'Cien años de soledad',
            'summary': 'La historia de la familia Buendía en Macondo: memoria, destino y realismo mágico.',
            'author': A('Gabriel', 'García Márquez'),
            'isbn': '9780307474728',
            'genre': ['Magical Realism', 'Classics'],
            'language': 'Spanish',
        },
        {
            'title': 'Norwegian Wood',
            'summary': 'A nostalgic story of love and loss set against the backdrop of 1960s Tokyo.',
            'author': A('Haruki', 'Murakami'),
            'isbn': '9780375704024',
            'genre': ['Romance'],
            'language': 'English',
        },
        {
            'title': 'Frankenstein',
            'summary': 'A young scientist creates life—then must face the consequences of his ambition and responsibility.',
            'author': A('Mary', 'Shelley'),
            'isbn': '9780141439471',
            'genre': ['Science Fiction', 'Classics'],
            'language': 'English',
        },
    ]

    # --- BookInstances ---
    # Original had 5 instances. We generate MANY more (>= 300% more than original, i.e., >= 20).
    book_instances = []

    def add_instances_for_book(title, base_imprint, due_back_1='2026-03-10'):
        # 1) On loan
        book_instances.append({
            'book': title,
            'imprint': f'{base_imprint} (copy A)',
            'due_back': due_back_1,
            'status': 'o',
        })
        # 2) Available
        book_instances.append({
            'book': title,
            'imprint': f'{base_imprint} (copy B)',
            'due_back': '',
            'status': 'a',
        })
        # 3) Reserved
        book_instances.append({
            'book': title,
            'imprint': f'{base_imprint} (copy C)',
            'due_back': '',
            'status': 'r',
        })

    # Create 3 copies for every book
    for i, bo in enumerate(books, start=1):
        add_instances_for_book(
            bo['title'],
            base_imprint=f'Library imprint #{i}',
            due_back_1=f'2026-03-{(i % 20) + 1:02d}'
        )

    # --- Insert languages ---
    for lan in languages:
        lang = Language(name=lan['name'])
        lang.save()

    # --- Insert genres ---
    for gen in genres:
        genr = Genre(name=gen['name'])
        genr.save()

    # --- Insert authors ---
    for aut in authors:
        dod = None if not aut['date_of_death'] else aut['date_of_death']
        auth = Author(
            first_name=aut['first_name'],
            last_name=aut['last_name'],
            date_of_birth=aut['date_of_birth'],
            date_of_death=dod
        )
        auth.save()

    # --- Insert books ---
    for bo in books:
        t    = bo['title']
        s    = bo['summary']
        isb  = bo['isbn']
        l    = bo['language']
        g    = bo['genre']
        a_fn = bo['author']['first_name']
        a_ln = bo['author']['last_name']

        aut  = Author.objects.filter(first_name__contains=a_fn, last_name__contains=a_ln).first()
        lang = Language.objects.filter(name__contains=l).first()
        new_book = Book(title=t, isbn=isb, summary=s, author=aut, language=lang)
        new_book.save()  # save before M2M

        for ge in g:
            gen = Genre.objects.filter(name__contains=ge).first()
            if gen is not None:
                new_book.genre.add(gen)

        new_book.save()

    # --- Insert book instances ---
    for bi in book_instances:
        bok = Book.objects.filter(title__contains=bi['book']).first()
        db  = None if not bi['due_back'] else bi['due_back']
        new_book_instance = BookInstance(
            book=bok,
            imprint=bi['imprint'],
            due_back=db,
            status=bi['status']
        )
        new_book_instance.save()


def create_dummy_privileged_user():
    u, created = User.objects.get_or_create(username=DP_USER)
    if created:
        u.set_password(DP_PASSWORD)  # encrypts password

    u.is_staff = True

    try:
        for codename in ['add_book', 'change_book', 'delete_book', 'can_mark_returned']:
            permission = Permission.objects.get(codename=codename)
            u.user_permissions.add(permission)
    except Permission.DoesNotExist:
        warnings.warn(
            "Permissions are defined later. For now, some or all of these assignments are omitted."
        )

    u.save()

    # Borrower example: assign the first instance of "The Shining" to the dummy user
    bi = BookInstance.objects.filter(book__title='The Shining').first()
    if bi is not None:
        bi.borrower = u
        bi.save()


if __name__ == '__main__':
    print("Starting catalog population script (extended)...")
    print("Removing existing objects ...")
    clean_db()
    print("Done!")
    print("Populating the db ...")
    populate()
    create_dummy_privileged_user()
    print("Done!")
