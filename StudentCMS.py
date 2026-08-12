#StudentCMS
#import
from Student import Student
import time
import pandas as pd

class StudentCMS:
    def __init__(self):
        self.stu_list=[]

    def show_view(self):
        print('*'*23)
        print('StudentCMS')
        print('\t1.add student information')
        print('\t2.delete student information')
        print('\t3.update student information')
        print('\t4.search single student information')
        print('\t5.print all students information')
        print('\t6.save students information')
        print('\t0.quilt CMS')
        print('*'*23)

    def add_student(self):
        #student self,name,gender,age,phone,desc
        print('Please input student\'s information')
        name=input('Name:')
        gender=input('Gender:')
        age=int(input('Age:'))
        phone=input('Phone number:')
        desc=input('Descrimination:')
        stu=Student(name,gender,age,phone,desc)
        
        self.stu_list.append(stu)
        
        print('successfully add')

    def delete_student(self):
        name=input('Name u want to delete:')
        for stu in self.stu_list:
            if stu.name==name:
                self.stu_list.remove(stu)
                print(f'delete{stu.name}')
                break
            else:
                print('no such student')

    def update_student(self):
        name=input('student u want to update:')
        for stu in self.stu_list:
            if stu.name==name:
                stu.name=input('Name:')
                stu.gender=input('Gender:')
                stu.age=int(input('Age:'))
                stu.phone=input('Phone number:')
                stu.desc=input('Descrimination:')
                break
        else:
            print('no such student')

    def search_single_student(self):
        name=input('student u want to search:')
        for stu in self.stu_list:
            if stu.name==name:
                print(stu)
                break
            else:
                print('no such student')

    def search_all_student(self):
        if len(self.stu_list)==0:
            print('no student information')
        else:
            for stu in self.stu_list:
                print(stu)
        print('\n')

    def save_student_information(self):
        # stu_dict=[stu.__dict__ for stu in self.stu_list]
        # with open('./stu_information','w',encoding='utf-8') as dest_file:            
        #     dest_file.write(str(stu_dict))
        # print('successfully saved')
        std_dict=[stu.__dict__ for stu in self.stu_list]
        df=pd.DataFrame(std_dict)
        df.to_excel('./stu_information.xlsx',index=False,engine='openpyxl')
        print('successfully saved')

    def load_stu(self):
        # try:
        #     with open('./stu_information','r',encoding='utf-8') as source_file:
        #         stu_data=source_file.read()
                
        #     if len(stu_data)==0:
        #         self.stu_list=[]
        #     else:
        #         stu_list=eval(stu_data)
        #         self.stu_list=[Student(**stu) for stu in stu_list]
        # except:
        #     with open('./stu_information','w',encoding='utf-8') as source_file:
        #         pass
        try:
            df = pd.read_excel('./stu_information.xlsx')
            stu_dict_list=df.to_dict(orient='records')
            self.stu_list=[Student(**stu) for stu in stu_dict_list]
        except:
            empty_df=pd.DataFrame()
            empty_df.to_excel('./stu_information.xlsx',index=False)

    def excute(self):
        self.load_stu()
        while 1:
            time.sleep(1)
            
            self.show_view()
            
            #input
            input_num=int(input('choose what u want to do ->'))
            
            if input_num==1:
                self.add_student()

            elif input_num==2:
                self.delete_student()

            elif input_num==3:
                self.update_student()

            elif input_num==4:
                self.search_single_student()

            elif input_num==5:
                self.search_all_student()

            elif input_num==6:
                self.save_student_information()

            elif input_num==0:
                num=input('Are u sure?(Y/N)')
                if num.lower()=='y':
                    self.save_student_information()
                    print('Thanks for  using')
                    break

            else:
                print('Error input,try again\n')

            print('\n')
                
                