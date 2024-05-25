score = float(input('Enter Score : '))

if(score < 60 and score > 40) :
    print('The Student is pass only')
elif(score >= 60 and score <= 80) :
    print('The student is first devison')
elif(score > 80) : 
    print('The Student is excellent')
else : 
    print('The student is fail')