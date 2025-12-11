import sqlite3


class DatabaseManager:
    def __init__(self, db_name="university.db"):
        self.db_name = db_name

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def create_tables(self):
        with self._connect() as conn:
            cursor = conn.cursor()            # Таблиця студентів
            cursor.execute("""
                           CREATE TABLE IF NOT EXISTS students
                           (
                               id
                               INTEGER
                               PRIMARY
                               KEY
                               AUTOINCREMENT,
                               full_name
                               TEXT
                               NOT
                               NULL,
                               group_number
                               TEXT
                               NOT
                               NULL,
                               birth_date
                               TEXT
                           )
                           """)
            # Таблиця оцінок (зв'язана зі студентом)
            cursor.execute("""
                           CREATE TABLE IF NOT EXISTS grades
                           (
                               id
                               INTEGER
                               PRIMARY
                               KEY
                               AUTOINCREMENT,
                               student_id
                               INTEGER,
                               subject
                               TEXT,
                               score
                               INTEGER,
                               FOREIGN
                               KEY
                           (
                               student_id
                           ) REFERENCES students
                           (
                               id
                           )
                               )
                           """)
            print("[DB] Таблиці перевірено/створено.")

    # 2. Метод запису даних (INSERT)
    def add_student_data(self, full_name, group_number, birth_date):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO students (full_name, group_number, birth_date) VALUES (?, ?, ?)",
                           (full_name, group_number, birth_date))
            student_id = cursor.lastrowid
            print(f"[DB] Студента {full_name} додано з ID {student_id}.")
            return student_id

    def add_grade(self, student_id, subject, score):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO grades (student_id, subject, score) VALUES (?, ?, ?)",
                           (student_id, subject, score))

    # 3. Метод оновлення даних (UPDATE)
    def update_student_group(self, student_name, new_group):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE students SET group_number = ? WHERE full_name = ?", (new_group, student_name))
            if cursor.rowcount > 0:
                print(f"[DB] Групу студента {student_name} оновлено на {new_group}.")
            else:
                print(f"[DB] Студента {student_name} не знайдено.")

    # 4. Метод видалення даних (DELETE)
    def delete_student(self, student_name):
        with self._connect() as conn:
            cursor = conn.cursor()
            # Спочатку треба знайти ID, щоб видалити оцінки (або використати CASCADE в SQL)
            cursor.execute("SELECT id FROM students WHERE full_name = ?", (student_name,))
            row = cursor.fetchone()
            if row:
                student_id = row[0]
                cursor.execute("DELETE FROM grades WHERE student_id = ?", (student_id,))
                cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
                print(f"[DB] Студента {student_name} та його оцінки видалено.")
            else:
                print(f"[DB] Студента для видалення не знайдено.")

    def show_all_students(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students")
            rows = cursor.fetchall()
            print("\n--- Список студентів у БД ---")
            for row in rows:
                print(row)
            print("-----------------------------")