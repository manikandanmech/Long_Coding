''' ONLINE VIDEO COURSES AND CLASSES'''


class Courses:
    def __init__(self):
        pass

    def beginner(self):
        course_amount = 200
        return (course_amount)

    def intermediate(self):
        course_amount = 500
        return (course_amount)

    def advanced(self):
        course_amount = 800
        return (course_amount)

    def fullStack(self):
        course_amount = 900
        return (course_amount)


class Categories:
    def __init__(self):
        self.category_amount = 1000


class Python(Categories):
    def __init__(self):
        Categories.__init__(self)
        self.python_amount = 200
        obj_courses = Courses()

    def amount(self):
        return (self.python_amount + self.category_amount)

    def duration(self):
        self.duration_python = "2 Months"
        return self.duration_python


class JS(Categories):
    def __init__(self):
        Categories.__init__(self)
        self.js_amount = 100
        obj_courses = Courses()

    def amount(self):
        return (self.js_amount + self.category_amount)

    def duration(self):
        self.duration_js = "3 Months"
        return self.duration_python


class R(Categories):
    def __init__(self):
        Categories.__init__(self)
        self.r_amount = 150
        obj_courses = Courses()

    def amount(self):
        return (self.r_amount + self.category_amount)

    def duration(self):
        self.duration_r = "4 Months"
        return self.duration_python


class HTML(Categories):
    def __init__(self):
        Categories.__init__(self)
        self.html_amount = 300
        obj_courses = Courses()

    def amount(self):
        return (self.r_amount + self.category_amount)

    def duration(self):
        self.duration_python = "1 Months"
        return self.duration_html


class Instructors():
    def __init__(self):
        pass

    def addCourses(self, course_name):
        self.course_name = course_name


def wallet():
    previous_course = ["Java"]
    completion_percent = [60]
    instructors_name = ["zzz"]
    print("Previously Selected Courses :-", *previous_course)
    print("Completion Percentage :-", *completion_percent)
    print("Instructor Name:-", *instructors_name)
    return previous_course, completion_percent, instructors_name


def newwallet():
    previous_course = []
    completion_percent = []
    instructors_name = []
    return previous_course, completion_percent, instructors_name


def categories():
    print("The Categories and Price are given below ")
    print("1.Python", "2.JS", "3.R", "4.HTML", sep='\n')


def userLogin():
    print("Enter User Name :- ", end='')
    user_name = input().strip()
    print("Enter User Id :- ", end='')
    user_id = int(input().strip())
    return (user_name, user_id)


def newCategory():
    print("Enter your New Category Name :- ", end=' ')
    category_name = input().strip()
    return category_name


def categoryName(category_name):
    dict_for_category = {"Python": Python(), "JS": JS(), "R": R(), "HTML": HTML()}
    category_name_obj = dict_for_category[category_name]
    return category_name_obj


def courseType():
    print("Enter The Type of Course :- ")
    print("The Available Type of Courses are :- ")
    print("1.Beginner", "2.Intermediate", "3.Advanced", "4.FullStack", sep='\n')
    course_type = input().strip()
    return course_type


def courseTypeAmount(course_type):
    dict_for_courses = {"Beginner": Courses.beginner(), "Intermediate": Courses.intermediate(),
                        "Advanced": Courses.advanced(), "FullStack": Courses.fullStack()}
    course_type_amount = dict_for_courses[course_type]
    return course_type_amount


def instructor(user_id):
    users_id_details = [13, 72, 48, 70]
    if user_id not in users_id_details:
        return
    else:
        obj_in = Instructors()


def buyCourse(total_amount):
    print("The Payment Will be done Through UPI")
    print("Payment_id :- V32x")
    print("Congratulations!!! The Course has been Added to your Wallet")


def userCheck(user_id):
    users_id = [12, 45, 67]
    user_id_dict = {"xxx": ["Ruby"], "ttt": ["Shell"], "ggg": ["React"]}
    if user_id in users_id:
        return 1
    else:
        return 0


def exixtingUser(user_id):
    # wallet()
    previous_course, completion_percent, instructors_name = wallet()
    categories()
    category_name = newCategory()
    category_name_obj = categoryName(category_name)
    course_type = courseType()
    category_name_amount = category_name_obj.amount()
    course_type_amount = courseTypeAmount(course_type)
    total_amount = category_name_amount + course_type_amount
    print("The Total Amount of The Course is :- ", total_amount)
    print("Are you Willing to buy this Course :- ", end=' ')
    willing = input().strip()
    if willing == "yes":
        buyCourse(total_amount)
        previous_course.append(category_name)
        print("Now The Courses in your Wallet are :- ", *previous_course)
    else:
        print("Thanks for coming!!!")
    exit()


if __name__ == '__main__':
    user_name, user_id = userLogin()
    instructor(user_id)
    check = userCheck(user_id)
    if check == 1:
        exixtingUser(user_id)
    else:
        print("Sign in NEW USER")
        newwallet()
        previous_course, completion_percent, instructors_name = newwallet()
        categories()
        category_name = newCategory()
        category_name_obj = categoryName(category_name)
        course_type = courseType()
        category_name_amount = category_name_obj.amount()
        course_type_amount = courseTypeAmount(course_type)
        total_amount = category_name_amount + course_type_amount
        print("The Total Amount of The Course is :- ", total_amount)
        print("Are you Willing to buy this Course :- ", end=' ')
        willing = input().strip()
        if willing == "yes":
            buyCourse(total_amount)
            previous_course.append(category_name)
            print("Now The Courses in your Wallet are :- ", *previous_course)
        else:
            print("Thanks for coming!!!")
        exit()