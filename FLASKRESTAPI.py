#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, jsonify


# In[2]:


app = Flask(__name__)


# In[5]:


@app.route('/')
def hello_world():
    return 'Hello, World!'


# In[6]:


if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:




