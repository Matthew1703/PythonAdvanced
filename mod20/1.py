from flask import Flask, jsonify, request
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import create_engine, Column, Integer, Text, Date, Float, Boolean, DateTime, String
import datetime

app = Flask(__name__)

engine = create_engine("sqlite:///python1.db")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Books(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    count = Column(Integer, default=1)
    release_date = Column(Date, nullable=False)
    author_id = Column(Integer, nullable=False)

    def __repr__(self):
        return f"{self.id} | {self.name} | {self.count} | {self.release_date} | {self.author_id}"

    def to_json(self):
        return {str(c.name): getattr(self, c.name) for c in self.__table__.columns}

class Authors(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    surname = Column(Text, nullable=False)

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
    scoolarship = Column(Boolean, nullable=False)

    def __repr__(self):
        return f"\t{self.id} | {self.name} | {self.surname} | {self.phone} | {self.email} | {self.average_score} | {self.scoolarship}\n"

    """Третье задание"""
    @classmethod
    def get_list_students_by_address(cls):
        return session.query(Students).filter(Students.email == "общежитие").all()

    @classmethod
    def get_list_students_by_higher_values(cls, values):
        return session.query(Students).filter(Students.average_score > values).all()

class Receiving_books(Base):
    __tablename__ = 'receiving_books'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, nullable=False)
    student_id = Column(Integer, nullable=False)
    date_of_issue = Column(DateTime, nullable=False)
    date_of_return = Column(DateTime)

    def __repr__(self):
        return f"{self.id} | {self.book_id} | {self.student_id} | {self.date_of_issue} | {self.date_of_return}"

    """Второе задание"""
    @hybrid_property
    def count_date_with_book(self):
        return datetime.datetime.now() - self.date_of_issue

"""ВТорое задание"""
# i1 = Receiving_books(id=11, book_id=11, student_id=11, date_of_issue=datetime.datetime(day=15, month=11, year=2022))
# print(i1)
# print("Книгу держали/держат уже:", i1.count_date_with_book)

"""Третье задание"""
# Base.metadata.create_all(bind=engine)
# print(Students.get_list_students_by_address())
# print(Students.get_list_students_by_higher_values(3.2))


@app.before_request
def before_request_func():
    Base.metadata.create_all(bind=engine)
@app.route("/get_all_books", methods=["GET"])
def get_all_books():
    books = session.query(Books).all()
    list_books = []
    for book in books:
        list_books.append(book.to_json())
    return jsonify(list_books=list_books), 200
@app.route("/get_debtors", methods=["GET"])
def get_debtors():
    debtors = session.query(Receiving_books).one()
    print(debtors)
    return "ff", 200

@app.route("/receive_book", methods=["POST"])
def receive_book():
    student_id = request.form.get("student_id", type=int)
    book_id = request.form.get("book_id", type=int)
    new_book = Students()

if __name__ == "__main__":
    app.run()