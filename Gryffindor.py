student_data = {
    'Jason': 'Gryffindor',
    'Kaitlynne': 'Ravenclaw',
    'Aidan': 'Slytherin',
    'Nicole': 'Hufflepuff',
    'Antonio': 'Gryffindor',
    'Alexander': 'Ravenclaw',
    'Samantha': 'Slytherin',
    'Reagan': 'Hufflepuff',
    'Lauren': 'Gryffindor',
    'Emma': 'Ravenclaw',
    'Veronica': 'Slytherin',
    'Matthew': 'Hufflepuff',
    'Madison': 'Gryffindor',
    'Jijoy': 'Ravenclaw',
    'Christopher': 'Slytherin',
    'Alex': 'Hufflepuff',
    'Cedric': 'Gryffindor',
    'Jason': 'Ravenclaw',
} #dictionary uses curly brackets

# Print only the students in Gryffindor
print("Students in Gryffindor:")
for student, house in student_data.items():
    if house == 'Gryffindor': # == if house is equal to 
    #print the student names
        print(student)