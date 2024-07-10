from datetime import date
from utils.ora_padej import ora_padej


def extract_data_study(request):
    data = request.data
    establishment = data.get('student_full', {}).get('establishment', '')

    student_gender = data.get('student_full', {}).get('gender', '')
    gender = 1 if student_gender == 'Мужской' else 2
    student = data.get('student_full', {})
    course = student.get('course', '')
    student = f"{student.get('surname', '')} {student.get('name', '')} {student.get('patronymic', '')}"
    student = ora_padej(student, 'ФИО', 'rod', gender)

    mentor_gender = data.get('mentor_full', {}).get('gender', '')
    gender = 1 if mentor_gender == 'Мужской' else 2
    mentor = data.get('mentor_full', {})
    defaul = f"{mentor.get('surname', '')} {mentor.get('name', '')[:1]}. {mentor.get('patronymic', '')[:1]}."
    mentor = f"{ora_padej(mentor.get('surname', ''), 'Ф', 'rod', gender)} {mentor.get('name', '')[:1]}. {mentor.get('patronymic', '')[:1]}."

    start_date = data.get('start_date', '')
    end_date = data.get('end_date', '')
    current = str(date.today())

    return {
        'establishment': establishment,
        'student': student,
        'mentor': mentor,
        'defaul': defaul,
        'course': course,
        'start_date': start_date,
        'end_date': end_date,
        'current': current
    }


def extract_data_internship(request):
    data = request.data

    student = data.get('student_full', {})
    student = f"{student.get('surname', '')} {student.get('name', '')} {student.get('patronymic', '')}"

    mentor_gender = data.get('mentor_full', {}).get('gender', '')
    gender = 1 if mentor_gender == 'Мужской' else 2
    mentor = data.get('mentor_full', {})
    mentor = f"{ora_padej(mentor.get('surname', ''), 'Ф', 'rod', gender)} {mentor.get('name', '')[:1]}. {mentor.get('patronymic', '')[:1]}."

    start_date = data.get('start_date', '')
    end_date = data.get('end_date', '')
    current = str(date.today())

    return {
        'student': student,
        'mentor': mentor,
        'start_date': start_date,
        'end_date': end_date,
        'current': current
    }
