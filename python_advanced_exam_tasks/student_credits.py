def students_credits(*courses):
    courses_data = []
    total_credits = 0

    for course_data in courses:
        course_name, course_credits, max_points, diyan_points = course_data.split("-")

        diyan_credits = int(course_credits) * (int(diyan_points) / int(max_points))
        total_credits += diyan_credits
        courses_data.append((course_name, diyan_credits))

    courses_data.sort(key=lambda x: x[1], reverse=True)

    result = []

    if total_credits >= 240:
        result.append(f"Diyan gets a diploma with {total_credits:.1f} credits.")
    else:
        result.append(f"Diyan needs {240 - total_credits:.1f} credits more for a diploma.")

    for course_data in courses_data:
        result.append(f"{course_data[0]} - {course_data[1]:.1f}")

    return "\n".join(result)
