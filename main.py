print('Welcome to the Student Grading System! \n')
studentsName = input(('Enter student name ')) #Берем имя студента

bool = True #переменная для цикла while, чтобы она работала пока не станет false

while(bool):
    #берем оценки студента
    x1 = int(input(f'Enter score for test 1 (0-100) ')) 
    x2 = int(input(f'Enter score for test 2 (0-100) '))
    x3 = int(input(f'Enter score for test 3 (0-100) '))
    if(x1<0 or x2<0 or x3<0): #если оценка ниже 0
        print('You must input number less than 100, more than 0 ')
        continue
    elif(x1>100 or x2>100 or x3>100): #если оценка больше 100
        print('You must input number less than 100, more than 0 ')
        continue
    else:
        grade = "" #переменная для оценок
        resultAverage = (x1+x2+x3)/3 #средняя оценка баллов
        if(resultAverage>89 and resultAverage<101):
            grade = "A"
        elif(resultAverage>79 and resultAverage<90):
            grade = "B"
        elif(resultAverage>69 and resultAverage<80):
            grage = "C"
        elif(resultAverage>59 and resultAverage<70):
            grade = "D"
        elif(resultAverage<60):
            grade = "F"
        #выводим статистику
        print(f'\nCalculating results...\nStudent: {studentsName}\nTest Scores: {x1}, {x2}, {x3}\nAverage Score: {resultAverage}\nGrade: {grade}')
        continueOrNot = input("\nDo you want to enter another student's details? (yes/no):")#спрашиваем продолжать или нет
        if(continueOrNot == 'yes'):
            #Если пользователь не хочет продолжать, обнуляем все переменные и продолжаем цикл
            studentsName = input(('\nInput students name '))
            resultAverage = 0
            grade = ""
            x1 = 0
            x2 = 0
            x3 = 0
            continue
        else:
            # Если пользователь не хочет продолжать, завершение программы
            print('\nThank you for using the Student Grading System. Goodbye!')
            bool = False #выходим из цикла
        
        
        
