nep = input("enter marks of Nepali")
nep = int(nep)
print(nep)
eng = input("enter marks of English")
eng = int(eng)
print(eng)
mat = input("enter marks of Maths")
mat = int(mat)
print(mat)
sc = input("enter marks of Science")
sc = int(sc)
print(sc)
pop = input("enter marks of Populations")
pop = int(pop)
print(pop)
total_marks = int(nep + eng + mat + sc + pop)
print(total_marks)
percentage =float(total_marks/5)
print(percentage)
if percentage < 35:
    print('fail')
elif percentage > 35 and percentage < 45:
    print('third Division')
elif percentage >= 45 and percentage < 60:
    print('Second Division')
elif percentage >= 60 and percentage < 75:
    print('Fisrt division')
elif percentage >= 75:
    print('fist division with distiction')
else:
    print('enter marks of each subjects in betwwen 0 to 100')
