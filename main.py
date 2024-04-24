from conf.models import session
from conf.models import Group, Teacher, Student, Subject, Grade

from sqlalchemy import func, desc, select, and_

def select_01():
    """
    SELECT
        s.id,
        s.fullname,
        ROUND(AVG(g.grade), 2) AS average_grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 5;
    """
    result = session.query(Student.id, Student.student_name, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Student).join(Grade).group_by(Student.id).order_by(desc('average_grade')).limit(5).all()
    return result


def select_02():
    """
    SELECT
        s.id,
        s.fullname,
        ROUND(AVG(g.grade), 2) AS average_grade
    FROM grades g
    JOIN students s ON s.id = g.student_id
    where g.subject_id = 1
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 1;
    """
  
    result = session.query(Student.student_name,func.round(func.avg(Grade.grade), 2).label('average_grade')) \
    .select_from(Grade).filter(Grade.subjects_id == 2).join(Student) \
    .group_by(Student.id).order_by(desc('average_grade')).limit(1).all()

    return result


def select_03():
    """
    SELECT s2.topics , g.groups , ROUND(AVG(m.mark), 2) as avgMark
    FROM marks m
    INNER JOIN subjects s2 ON s2.id = m.subject_id 
    INNER JOIN students AS s ON s.id = m.student_id 
    INNER JOIN groups g ON g.id = s.gruop_id  
    WHERE subject_id  = 3
    GROUP by s.gruop_id 
    """

    result = session.query(Subject.subject, Group.group_name, func.avg(Grade.grade)) \
    .select_from(Grade).join(Subject).join(Student).join(Group) \
    .group_by(Subject.subject).group_by(Group.group_name).filter(Subject.id == 2).all()

    return result



def select_04():
    """
    SELECT ROUND(AVG(mark), 2) as avgMark
    FROM marks
    """
  
    result = session.query(func.round(func.avg(Grade.grade), 9).label('average_grade')) \
    .select_from(Grade).all()

    return result



def select_05():
    """
    SELECT t.teacher, s.topics 
    FROM teachers  AS t
    INNER JOIN subjects AS s ON t.id = s.teacher_id 
    ORDER by t.teacher 
    """

    result = session.query(Teacher.fullname, Subject.subject) \
    .select_from(Subject).join(Teacher) \
    .all()
    return result



def select_06():
    """
    SELECT g.groups , student 
    FROM students s 
    INNER JOIN groups g ON g.id = s.gruop_id  
    WHERE gruop_id =1
    """

    result = session.query(Group.group_name, Student.student_name) \
    .select_from(Student).join(Group).filter(Student.group_id == 2) \
    .all()
    return result



def select_07():
    """
    SELECT s2.topics, student, m.mark
    FROM marks AS m
    INNER JOIN students s ON s.id = m.student_id 
    INNER JOIN subjects s2 ON s2.id = m.subject_id 
    WHERE s2.id = 2
    """
  
    result = session.query(Subject.subject, Student.student_name, Grade.grade) \
    .select_from(Grade).join(Subject).join(Student).filter(Grade.subjects_id == 2).filter(Group.id == 2) \
    .all()

    return result



def select_08():
    """
    SELECT t.teacher, s.topics, ROUND(AVG(m.mark), 2) as avgMark 
    FROM marks m
    INNER JOIN subjects s ON s.id = m.subject_id 
    INNER JOIN teachers t ON t.id = s.teacher_id  
    WHERE s.teacher_id  = 2
    GROUP by m.subject_id 
    ORDER by s.topics 
    """
  
    result = session.query(Teacher.fullname, Subject.subject, func.avg(Grade.grade)) \
    .select_from(Grade).join(Subject).join(Teacher).filter(Teacher.id == 5) \
    .group_by(Teacher).group_by(Subject).all()

    return result



def select_09():
    """
    SELECT s.student , s2.topics 
    FROM marks m
    INNER JOIN students s ON s.id = m.student_id 
    INNER JOIN subjects s2 ON s2.id = m.subject_id 
    WHERE student_id = 2
    GROUP by subject_id 
    ORDER by s2.topics 
    """
  
    result = session.query(Student.student_name, Subject.subject) \
    .select_from(Grade).join(Student).join(Subject).filter(Grade.student_id == 5) \
    .group_by(Student.student_name).group_by(Subject.subject).all()

    return result



def select_10():
    """
    SELECT s.student, t.teacher , s2.topics 
    FROM marks m
    INNER JOIN students s ON s.id = m.student_id 
    INNER JOIN subjects s2 ON s2.id = m.subject_id 
    INNER JOIN teachers t ON t.id = s2.teacher_id  
    WHERE m.student_id = 2 AND s2.teacher_id  = 2
    GROUP by m.subject_id 
    """
  
    result = session.query(Student.student_name, Teacher.fullname, Subject.subject) \
    .select_from(Grade).join(Subject).join(Teacher).join(Student).filter(Grade.student_id == 5).filter(Teacher.id == 5) \
    .group_by(Student.student_name).group_by(Teacher.fullname).group_by(Subject.subject).all()

    return result




def select_11():
    """
    SELECT t.teacher, s.student, ROUND(AVG(m.mark), 2) as avgMark
    FROM marks m
    INNER JOIN students s ON s.id = m.student_id 
    INNER JOIN subjects s2 ON s2.id = m.subject_id 
    INNER JOIN teachers t ON t.id = s2.teacher_id  
    WHERE m.student_id = 2 AND s2.teacher_id  = 2
    """
  
    result = session.query(Student.student_name, Teacher.fullname, func.avg(Grade.grade)) \
    .select_from(Grade).join(Student).join(Subject).join(Teacher).filter(Student.id == 2).filter(Teacher.id == 2) \
    .group_by(Student).group_by(Teacher).all()

    return result


if __name__ == '__main__':
    # print(select_01())
    # print(select_02())
    # print(select_03())
    # print(select_04()) 
    # print(select_05()) 
    # print(select_06()) 
    # print(select_07())
    # print(select_08())
    # print(select_09())
    # print(select_10())
    print(select_11())
    # print(select_12())