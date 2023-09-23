class classassignments():
    
    
    def Subfields():

        lists = ['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        print('Sub-fields in AI are: ')
        for temp in lists:

            print(temp)
            
               

    def OddEven():

        num = int(input('Enter the number :'))

        if((num%2)==0):
            print(num,'is even number')

        else:
            print(num,'is odd number')
            
    def Elegible():
        gender = input('Your Gender :') 
        age = int(input('Your Age : '))

        if(gender == 'male','M'):
                if(age > 21):
                    print('Eligble')
                else: 
                    print('Not a eligible')
        elif(gender == 'female','f'):
            if(age > 18):
                print('Eligble')
            else: 
                print('Not eligible')
                
    def percentage():

            sub1 = int(input('Subject1 : '))
            sub2 = int(input('Subject2 : '))
            sub3 = int(input('Subject3 : '))
            sub4 = int(input('Subject4 : '))
            sub5 = int(input('Subject5 : '))

            total = sub1+sub2+sub3+sub4+sub5
            per = total *(100/500)

            print('Total: ',total)
            print('Percentage :',per)
            
    def triangle():

        Height = int(input('Height : '))
        Breadth = int(input('Breadth : '))

        area = (Height*Breadth)/2
        print('Area formula: (Height*Breadth)/2')
        print('Area of the Triangle : ', area)

        Height1 = int(input('Height1 : '))
        Height2 = int(input('Height2 : '))
        Breadth = int(input('Breadth : '))

        peri = Height1+Height2+Breadth
        print('Perimeter formula: Height1+Height2+Breadth')
        print('Perimeter of Triangle : ', peri)


       
     