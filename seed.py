from faker import Faker
from sqlalchemy.orm import Session
from models import Group, Student, Teacher, Subject, Grade
from config import SessionLocal
import random
from datetime import datetime, timedelta

fake = Faker('uk_UA')


def seed_database():
    db = SessionLocal()
    try:
        # Створення груп
        groups = []
        for _ in range(3):
            group = Group(name=f"Група {fake.random_number(digits=3)}")
            groups.append(group)
        db.add_all(groups)
        db.commit()

        # Створення викладачів
        teachers = []
        for _ in range(5):
            teacher = Teacher(name=fake.name())
            teachers.append(teacher)
        db.add_all(teachers)
        db.commit()

        # Створення предметів
        subjects = []
        subject_names = ['Математика', 'Фізика', 'Хімія', 'Біологія',
                         'Історія', 'Українська мова', 'Англійська мова']
        for name in subject_names:
            subject = Subject(name=name, teacher_id=random.choice(teachers).id)
            subjects.append(subject)
        db.add_all(subjects)
        db.commit()

        # Створення студентів
        students = []
        for _ in range(50):
            student = Student(
                name=fake.name(),
                group_id=random.choice(groups).id
            )
            students.append(student)
        db.add_all(students)
        db.commit()

        # Створення оцінок
        grades = []
        for student in students:
            for subject in subjects:
                for _ in range(random.randint(1, 5)):
                    grade = Grade(
                        student_id=student.id,
                        subject_id=subject.id,
                        grade=random.randint(1, 5),
                        date=fake.date_time_between(
                            start_date='-1y', end_date='now')
                    )
                    grades.append(grade)
        db.add_all(grades)
        db.commit()

    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
