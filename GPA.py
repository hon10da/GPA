
import os 
import pandas as pd 
os.system("cls")

old_gpa=float(input("Enter your old GPA :"))
old_hours=int(input("Enter your old hours :"))
old_points=old_gpa*old_hours
os.system("cls")

new_gpa=float(input("Enter your new GPA :"))
new_hours=int(input("Enter your new hours :"))
new_points=new_gpa*new_hours
  
tot_hours=old_hours+new_hours
tot_points=old_points+new_points
tot_gpa=tot_points/tot_hours
os.system("cls")

old=[old_gpa,old_hours,old_points]
new=[new_gpa,new_hours,new_points]
tot=[tot_gpa,tot_hours,tot_points]

pd.set_option('display.float_format', lambda x: '%.2f' % x)
GPA=pd.DataFrame((old,new,tot),index=['Old','New','Total'],columns=['GPA','Hours','Points'])
print("Your currant GPA is :\n\n",GPA)

