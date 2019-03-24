#!/usr/bin/env python
# coding: utf-8

# In[81]:


enterprise_name = input("The name of your company or enterprise: ")


# In[75]:


menu_list = []
naive_order_list = []


# In[76]:


import math
b_input = input("Set the constant 'B' unique to your enterprise's function of diminishing satisfaction: ")
b = int(b_input)


# In[77]:


import sympy
import matplotlib.pyplot as plt
import numpy as np
import IPython.display

#sympy.init_printing(use_unicode=True)
sympy.init_printing(use_latex='mathjax')

t, s = sympy.symbols('t s')


# In[78]:


class Menu():
    def __init__(self, menu_name, t_required):
        self.menu_name = menu_name
        self.t_required = t_required
    
    def getMenuName(self):
        return self.menu_name
    
    def getRequiredTime(self):
        return self.t_required
        
    def whenMenuReceived(self, t_received):
        self.t_received = t_received
        satisfaction = 1/(1+exp(b*(t_received-t_required)))
        print("The satisfaction rate for this order is",satisfaction*100,"%.")


# In[79]:


def addMenu():
    n = input("Please enter the name of the menu:")
    t_string = input("Please enter the time it takes to make the menu:")
    print(type(t_string))
    t = int(t_string)
    print(type(t))
    menu = Menu(n,t)
    newlist = [menu]
    menu_list += newlist
    print(menu_list)


# In[80]:


class Order:
    order_name = "lala"
    order_amount = 0

    def __init__(self, name, howmany):
        order_name = name
        order_amount = howmany

    def getOrderName(self):
        return order_name

def addOrder():
    n = input("The name of the new order:")
    a = int(input("The order amount of this order:"))
    neworder = Order(n,a)
    newlist = [neworder]
    naive_order_list += newlist


# In[63]:


def showFunctions():
    for menu in menu_list:
        time_required = menu.getRequiredTime()
        sympy.plot(1/(1+exp(b*(t-time_required))),(t,0,6))


# In[ ]:




