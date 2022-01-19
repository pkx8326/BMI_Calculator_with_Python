#!/usr/bin/env python
# coding: utf-8

# In[2]:


# This program demonstrates simple arythmetic calculaiton in Python by calculating your Body Mass Index (BMI) 
# It also demonstrate the PEMDAS (Pharentheses, exponential, multiplication, division, addition, and substraction) calculation
# order rule.

# To learn more about BMI, follow this link: https://en.wikipedia.org/wiki/Body_mass_index
                            
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

print(f"Your Body Mass Index (BMI) is {round(weight/(height**2),1)}") 


# In[ ]:




