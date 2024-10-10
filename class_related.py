class Student:
    student_num = 0

    def __init__(self, name: str, gender: str):
        self.name = name
        self.gender = gender
        Student.student_num += 1

    def __str__(self) -> str:
        return (
            f"Student no: {Student.student_num}, "
            f"name: {self.name}, gender: {self.gender}"
        )

    @classmethod
    def from_string(cls, string: str):
        name, gender = string.split(" ")
        return cls(name, gender)


class Util:
    @staticmethod
    def is_male(student: Student) -> bool:
        return student.gender in ("男", "male")


def main() -> None:
    student = Student.from_string("小明 男")
    print(Student.student_num)
    print(student)

    print(Util.is_male(student))


main()
