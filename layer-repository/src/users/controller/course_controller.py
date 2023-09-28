from flask import Blueprint, jsonify, request
from users.model.course_model import Course
from users.repository.memory_repository import CourseRepository


blueprint = Blueprint('courses_controller', __name__)
repository = CourseRepository()


@blueprint.route("/courses", methods=["POST"])
def insert_course():
    course_data = request.get_json()

    if repository.exists(course_data["name"]):
        return jsonify({"message": "Course already exists"}), 400


    course = Course(
        id=len(repository.course) + 1,
        name=course_data["name"],
        description=course_data["description"]
    )

    repository.add(course)

    return jsonify(course)


@blueprint.route("/courses/<course_id>", methods=["GET"])
def get_course(course_id):
    course = repository.get(course_id)

    if course is None:
        return jsonify({"message": "Course not found"}), 404

    return jsonify(course)
