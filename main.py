
import pandas as pd
import numpy as np
from numpy.core.arrayprint import _leading_trailing
import streamlit as st
from streamlit_metrics import metric_row
button=st.button('按钮')
st.text_input('请输入最喜欢的编程语言',key="name")
st.write('Hello streamlit.')
st.text('Hello streamlit.')
st.header('header')
st.subheader('header')
number = st.slider('pick a number ',0,100)
flag = st.checkbox('yes')
languages = ['python','c','rust','c++']
st.radio('pick a language',languages)
st.selectbox('用过哪几种编程语言？',('python','c','java','rust'))
date=st.date_input('pick a date')
color = st.color_picker('pick a color')
file = st.file_uploader('pick a file')
with st.form ("my_form",clear_on_submit=False):
    name = st.text_input("请输入用户名")
    passwd = st.text_input("请输入密码",type="password")
    passwd_re = st.text_input("请再次输入密码",type="password")
    
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write(f'欢迎用户{name}')
st.json({
    "code":0,
    "data":{
        "sex": "female",
        "age":18,
        "score":100
    }
}
)


code = """
    def func():
        print('Hello streamlit.')
"""
st.code(code, language='python')

df = pd.DataFrame(np.random.randn(50, 5), columns=(
    'col %d' % i for i in range(5)))
st.dataframe(df)

df = pd.DataFrame(np.random.randn(50, 5), columns=(
    'col %d' % i for i in range(5)))
st.table(df)


st.write("一周数据统计")
metric_row(
    {
        "关注人数": 100,
        "点赞人数": 200,
        "在看人数": 300,
        "分享人数": 400
    }
)











