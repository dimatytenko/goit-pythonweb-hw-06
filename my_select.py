from sqlalchemy import func
from sqlalchemy.orm import Session
from models import Student, Group, Teacher, Subject, Grade
from config import SessionLocal


def select_1():
    """Знайти 5 студентів із найбільшим середнім балом з усіх предметів."""
    db = SessionLocal()
    try:
        result = db.query(
            Student.name,
            func.avg(Grade.grade).label('average_grade')
        ).join(Grade).group_by(Student.id).order_by(func.avg(Grade.grade).desc()).limit(5).all()
        return result
    finally:
        db.close()


def select_2(subject_name):
    """Знайти студента із найвищим середнім балом з певного предмета."""
    db = SessionLocal()
    try:
        result = db.query(
            Student.name,
            func.avg(Grade.grade).label('average_grade')
        ).join(Grade).join(Subject).filter(Subject.name == subject_name)\
            .group_by(Student.id).order_by(func.avg(Grade.grade).desc()).first()
        return result
    finally:
        db.close()


def select_3(subject_name):
    """Знайти середній бал у групах з певного предмета."""
    db = SessionLocal()
    try:
        result = db.query(
            Group.name,
            func.avg(Grade.grade).label('average_grade')
        ).select_from(Group)\
            .join(Student, Group.id == Student.group_id)\
            .join(Grade, Student.id == Grade.student_id)\
            .join(Subject, Grade.subject_id == Subject.id)\
            .filter(Subject.name == subject_name)\
            .group_by(Group.id).all()
        return result
    finally:
        db.close()


def select_4():
    """Знайти середній бал на потоці (по всій таблиці оцінок)."""
    db = SessionLocal()
    try:
        result = db.query(func.avg(Grade.grade).label('average_grade')).first()
        return result
    finally:
        db.close()


def select_5(teacher_name):
    """Знайти які курси читає певний викладач."""
    db = SessionLocal()
    try:
        result = db.query(Subject.name)\
            .join(Teacher).filter(Teacher.name == teacher_name).all()
        return result
    finally:
        db.close()


def select_6(group_name):
    """Знайти список студентів у певній групі."""
    db = SessionLocal()
    try:
        result = db.query(Student.name)\
            .join(Group).filter(Group.name == group_name).all()
        return result
    finally:
        db.close()


def select_7(group_name, subject_name):
    """Знайти оцінки студентів у окремій групі з певного предмета."""
    db = SessionLocal()
    try:
        result = db.query(Student.name, Grade.grade)\
            .join(Group).join(Grade).join(Subject)\
            .filter(Group.name == group_name, Subject.name == subject_name)\
            .all()
        return result
    finally:
        db.close()


def select_8(teacher_name):
    """Знайти середній бал, який ставить певний викладач зі своїх предметів."""
    db = SessionLocal()
    try:
        result = db.query(
            func.avg(Grade.grade).label('average_grade')
        ).join(Subject).join(Teacher)\
            .filter(Teacher.name == teacher_name).first()
        return result
    finally:
        db.close()


def select_9(student_name):
    """Знайти список курсів, які відвідує певний студент."""
    db = SessionLocal()
    try:
        result = db.query(Subject.name)\
            .join(Grade).join(Student)\
            .filter(Student.name == student_name)\
            .distinct().all()
        return result
    finally:
        db.close()


def select_10(student_name, teacher_name):
    """Список курсів, які певному студенту читає певний викладач."""
    db = SessionLocal()
    try:
        result = db.query(Subject.name)\
            .join(Grade).join(Student).join(Teacher)\
            .filter(Student.name == student_name, Teacher.name == teacher_name)\
            .distinct().all()
        return result
    finally:
        db.close()
