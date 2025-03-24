courses = []
while True:
   course = input("Enter a course name (or press Enter to finish): ")
   if course == "":
       break
   courses.append(course)

if courses:
   print("Last course studied is: %s" % courses[-1])
else:
   print("No courses entered")