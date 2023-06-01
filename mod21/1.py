from flask import Flask, jsonify, request
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, backref
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import create_engine, Column, Integer, Text, Date, Float, Boolean, DateTime, String, ForeignKey
from sqlalchemy import update, delete
import datetime

app = Flask(__name__)
engine = create_engine("sqlite:///python1.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Books(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    count = Column(Integer, default=1)
    release_date = Column(Date, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)

    author = relationship("Authors", backref=backref("books", cascade="all, "
                                                                      "delete-orphan", lazy="select"))
    students = relationship("Receiving_books", back_populates="book")
    def __repr__(self):
        return f"{self.id} | {self.name} | {self.count} | {self.release_date} | {self.author_id}"

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Authors(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    surname = Column(Text, nullable=False)

    books = relationship("Books")

    def __repr__(self):
        return f"{self.id} | {self.name} | {self.surname}"

class Students(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    surname = Column(Text, nullable=False)
    phone = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    average_score = Column(Float, nullable=False)
    scholarship = Column(Boolean, nullable=False)

    books = relationship("Receiving_books", back_populates="student")

    def __repr__(self):
        return f"\t{self.id} | {self.name} | {self.surname} | {self.phone} | {self.email}" \
               f" | {self.average_score} | {self.scholarship}\n"
    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    @classmethod
    def get_list_students_by_address(cls):
        return session.query(Students).filter(Students.email == "общежитие").all()

    @classmethod
    def get_list_students_by_higher_values(cls, values):
        return session.query(Students).filter(Students.average_score > values).all()

class Receiving_books(Base):
    __tablename__ = 'receiving_books'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    date_of_issue = Column(DateTime, nullable=False)
    date_of_return = Column(DateTime)

    student = relationship("Students", back_populates="books")

    book = relationship("Books", back_populates="students")

    def __repr__(self):
        return f"{self.id} | {self.book_id} | {self.student_id} | {self.date_of_issue} | {self.date_of_return}"

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @hybrid_property
    def count_date_with_book(self):
        if self.date_of_return is not None:
            return self.date_of_return - self.date_of_issue
        return datetime.datetime.now() - self.date_of_issue

def insert_data():
    authors = [Authors(name="Александр", surname="Пушкин"),
               Authors(name="Лев", surname="Толстой"),
               Authors(name="Михаил", surname="Булгаков")
    ]
    authors[0].books.extend([
        Books(name="Капитанская дочка", count=5, release_date=datetime.date(1836, 1, 1)),
        Books(name="Евгений Онегин", count=3, release_date=datetime.date(1838, 1, 1))
    ])
    authors[1].books.extend([
        Books(name="Война и мир", count=10, release_date=datetime.date(1867, 1, 1)),
        Books(name="Анна Каренина", count=7, release_date=datetime.date(1877, 1, 1))
    ])
    authors[2].books.extend([
        Books(name="Морфий", count=5, release_date=datetime.date(1926, 1, 1)),
        Books(name="Собачье сердце", count=3, release_date=datetime.date(1925, 1, 1))
    ])
    students = [
        Students(name="Ivan", surname="Borisov", phone=1, email=2, average_score=3.7, scholarship=True),
        Students(name="Matvey", surname="Bachurin", phone=2, email=3, average_score=4.7, scholarship=True)
    ]
    session.add_all(authors)
    session.add_all(students)
    session.commit()

@app.route("/get_all_books", methods=["GET"])
def get_all_books():
    books = session.query(Books).all()
    books_list = []
    for book in books:
        books_list.append(book.to_json())
    return jsonify(books_list), 200
@app.route("/get_debtors", methods=["GET"])
def get_debtors():
    debtors = session.query(Receiving_books).all()
    list_students = []
    for debtor in debtors:
        if debtor.count_date_with_book > datetime.timedelta(days=14) and debtor.date_of_return is None:
            list_students.append(debtor.student_id)
    list_res = []
    for id_student in list_students:
        student = session.query(Students).filter(id_student==Students.id).one()
        list_res.append(student.to_json())
    return jsonify(list_res), 200

@app.route("/receive_book", methods=["POST"])
def receive_book():
    student_id = request.form.get("student_id", type=int)
    book_id = request.form.get("book_id", type=int)
    new_book = Receiving_books(book_id=book_id, student_id=student_id, date_of_issue=datetime.datetime.now().date())
    session.query(Books).filter(Books.id == book_id).update({Books.count: Books.count-1})
    session.add(new_book)
    session.commit()
    return "Книга выдана"

@app.route("/hand_over_book", methods=["POST"])
def hand_over_book():
    student_id = request.form.get("student_id", type=int)
    book_id = request.form.get("book_id", type=int)

    try:
        flag = session.query(Receiving_books).filter(
            (Receiving_books.book_id == book_id) & (Receiving_books.student_id == student_id)).one()
        print(flag)
        if not flag.date_of_return or not flag:
            session.query(Receiving_books).filter((Receiving_books.book_id == book_id) & (Receiving_books.student_id == student_id)).update({Receiving_books.date_of_return: datetime.datetime.now().date()})
            session.query(Books).filter(book_id==Books.id).update({Books.count: Books.count+1})
            session.commit()
            return "Книга возвращена"
        else:
            return "Такой связки нет"
    except:
        return "Такой связки нет"

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    c1 = Books(id=1, name="War and Piece", count=5, release_date=datetime.date(year=1848, month=11, day=11), author_id=1)
    c2 = Books(id=2, name="Crime and punishment", count=10, release_date=datetime.date(year=1888, month=12, day=22), author_id=2)
    c3 = Receiving_books(book_id=1, student_id=1, date_of_issue=datetime.date(day=15, month=11, year=2022), date_of_return=datetime.date(day=16, month=12, year=2022))
    c4 = Receiving_books(book_id=2, student_id=2, date_of_issue=datetime.date(day=2, month=5, year=2023))
    c5 = Students(id=1, name="Matvey", surname="Bachurin", phone=89034552728, email="общежитие", average_score=4.7, scoolarship=True)
    c6 = Students(id=2, name="Ivan", surname="Ivanov", phone=89034552728, email="дом", average_score=3.6, scoolarship=True)
    session.add_all([c1, c2, c3, c4, c5, c6])
    session.commit()
    app.run()