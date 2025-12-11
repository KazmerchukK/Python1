from models import Student, RealPerformance, DesiredPerformance, StudentData
from database import DatabaseManager


def main():
    db = DatabaseManager("university.db")
    db.create_tables()

    print("\n--- Створення об'єктів Python ---")

    student_obj = Student("Петренко Іван Олексійович", "КН-21", "2005-05-15")

    real_perf = RealPerformance()
    real_perf.add_subject("Програмування", 85)
    real_perf.add_subject("Математика", 90)

    desired_perf = DesiredPerformance(desired_avg_score=95)  # Хоче середній 95

    full_data = StudentData(student_obj, real_perf, desired_perf)

    print(f"Студент: {full_data.student.full_name}")
    print(f"Реальний середній бал: {full_data.real_perf.average_score()}")
    print(f"Бажаний середній бал: {full_data.desired_perf.average_score()}")

    print("\n--- Запис даних у БД ---")

    st_id = db.add_student_data(
        full_data.student.full_name,
        full_data.student.group_number,
        full_data.student.birth_date
    )

    # Запис оцінок в БД
    for i in range(len(full_data.real_perf.subjects)):
        subj = full_data.real_perf.subjects[i]
        score = full_data.real_perf.scores[i]
        db.add_grade(st_id, subj, score)

    db.show_all_students()

    # 3. Оновлення даних
    print("\n--- Оновлення даних ---")
    db.update_student_group("Петренко Іван Олексійович", "КН-22 (Нова)")
    db.show_all_students()

    # 4. Видалення даних
    db.delete_student("Петренко Іван Олексійович")
    db.show_all_students()


if __name__ == "__main__":
    main()