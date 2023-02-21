class School:
    def __init__(self,name,student):
        self.name=name
        self.student=student
    def __repr__(self) -> str:
        return f"school name: {self.name} total student: {self.student}"

KB=School('K,B Union High School',800)

print(KB)