from flask import Blueprint, jsonify, request
from users.model.course_model import Course


blueprint = Blueprint('courses_controller', __name__)
courses = []


@blueprint.route("/courses", methods=["POST"])
def insert_course():
    course_data = request.get_json()
    if any(course.name == course_data['name'] for course in courses):
        return jsonify({"message": "Course already exists"}), 400
    
    course = Course(
    id=len(courses) + 1,
    name=course_data["name"],
    description=course_data["description"]
    )

    courses.append(course)

    return jsonify(course)


@blueprint.route("/courses/<course_id>", methods=["GET"])
def get_course(course_id):
    course = next((course for course in courses if course.id == int(course_id)), None)

    if course is None:
        return jsonify({"message": "Courses not found"}), 404

    return jsonify(course)