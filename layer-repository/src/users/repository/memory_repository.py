from users.repository.abstract_repository import AbstractRepository
from users.model import user_model, course_model


class UserRepository(AbstractRepository):

    def __init__(self):
        self.users = []

    def add(self, user: user_model.User):
        self.users.append(user)

    def get(self, user_id) -> user_model.User:
        user = next((user for user in self.users if user.id == int(user_id)), None)
        return user
    
class CourseRepository(AbstractRepository):

    def __init__(self):
        self.course = []


    def add(self, course: course_model.Course):
        self.course.append(course)

    def get(self, course_id) -> course_model.Course:
        course = next((course for course in self.course if course.id == int(course_id)), None)
        return course
    
    def exists(self, course_name):
        return any(course.name == course_name for course in self.course)
