import random  
from random import randint

from faker import Faker
from sqlalchemy.exc import SQLAlchemyError

from conf.models import session
from conf.models import Group, Teacher, Student, Subject, Grade


fake = Faker('uk-UA')


def insert_groups():
    for _ in range(1, 5):
        group = Group(
            group_name=fake.word(),
            )
        session.add(group)

def insert_teachers():
    for _ in range(1, 6):
        teacher = Teacher(
            fullname = fake.name(),
        )
        session.add(teacher)


def insert_students():
    for _ in range(1, 40):
        student = Student(
            student_name=fake.name(),
            group_id = randint(1,3),
        )
        session.add(student)


def insert_subjects():
    for _ in range(1,7):
        subject = Subject(
            subject = fake.word(),
            teacher_id = randint(1, 6),
        )
        session.add(subject)


def insert_grades():
    for st in range(1,40):
        for su in range (1, 7):
            for i in range (1, 15):
                grades = Grade(
                grade = randint(1, 6),
                grade_date = fake.date_this_decade(),
                student_id = st,
                subjects_id = su,
                )
        session.add(grades)



if __name__ == '__main__':
    try:
        insert_groups()
        insert_teachers()
        insert_students()
        insert_subjects()
        insert_grades()
        session.commit()
        # insert_rel()
        # session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
    finally:
        session.close()