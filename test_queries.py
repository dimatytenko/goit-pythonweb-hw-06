from my_select import select_1, select_2, select_3, select_4, select_5, select_6, select_7, select_8, select_9, select_10


def test_queries():
    print("\n1. Топ 5 студентів із найбільшим середнім балом:")
    print(select_1())

    print("\n2. Найкращий студент з математики:")
    print(select_2("Математика"))

    print("\n3. Середній бал у групах з фізики:")
    print(select_3("Фізика"))

    print("\n4. Середній бал на потоці:")
    print(select_4())

    # Отримуємо ім'я першого викладача
    from config import SessionLocal
    from models import Teacher
    db = SessionLocal()
    teacher_name = db.query(Teacher.name).first()[0]
    db.close()

    print(f"\n5. Курси викладача {teacher_name}:")
    print(select_5(teacher_name))

    # Отримуємо назву першої групи
    from models import Group
    db = SessionLocal()
    group_name = db.query(Group.name).first()[0]
    db.close()

    print(f"\n6. Студенти групи {group_name}:")
    print(select_6(group_name))

    print(f"\n7. Оцінки студентів групи {group_name} з математики:")
    print(select_7(group_name, "Математика"))

    print(f"\n8. Середній бал викладача {teacher_name}:")
    print(select_8(teacher_name))

    # Отримуємо ім'я першого студента
    from models import Student
    db = SessionLocal()
    student_name = db.query(Student.name).first()[0]
    db.close()

    print(f"\n9. Курси студента {student_name}:")
    print(select_9(student_name))

    print(f"\n10. Курси студента {student_name} від викладача {teacher_name}:")
    print(select_10(student_name, teacher_name))


if __name__ == "__main__":
    test_queries()
