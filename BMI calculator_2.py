#!/usr/bin/env python
# coding: utf-8

# In[4]:


# This program demonstrates simple arythmetic calculaiton in Python by calculating your Body Mass Index (BMI) 
# It also demonstrate the PEMDAS (Pharentheses, exponential, multiplication, division, addition, and substraction) calculation
# order rule.

#In addition, this program categorizes BMI into 5 health categories by using the basic "if, elif, else" conditional clauses.

# To learn more about BMI, follow this link: https://en.wikipedia.org/wiki/Body_mass_index


import math #for the math.ceil() function

#taking inputs
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

#calculate the bmi value
bmi = math.ceil(weight/(height**2))

#check BMI with if conditional clauses
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi >= 25 and bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi >= 30 and bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")


# In[ ]:





# In[ ]:




