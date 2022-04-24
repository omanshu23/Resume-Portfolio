import streamlit as st
from PIL import Image

with open('RStyle.css') as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header
st.write("""
# Omanshu Gaidhane
##### *Resume*
""")

image = Image.open('dp.jfif')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info("""
- Kaggle Contributer at Kaggle, `3` Star on `HackerRank` (problem solving) and Data Science Enthusiast
- A Machine Learning enthusiast, zealous for gaining new knowledge in various domains like NLP, CV, RC etc.
- I also like to talk & write about Data Science domain & got insight from data.
""")

#####################
# Navigation

st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://github.com/omanshu23" target="_blank">Omanshu Gaidhane</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#Use-tools">Use Tools</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


#####################
# Custom function for printing text

def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)


def txt3(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5, 2, 2])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)


#####################
st.markdown('''
## Education
''')

txt('**B.Tech** Bansal Institute of Science and Technology, Bhopal (RGPV University)', '2019-2023')
st.markdown("""
- CGPA: `9.1`
- Computer Science Engineering & Data Science
""")

txt('**Allen Career Institute, Indore', '2018-2019')
st.markdown("""
- *Drop* for JEE(Main + Advanced) preparation.
- Studying Mathematics, Physics and Chemistry.
""")

txt('**12th** Excellence Higher Secondary School, Waraseoni', '2017-2018')
st.markdown("""
- Percent: `80%`
- Mathematics, Physics and Chemistry.
""")

txt('**10th** Vivek Jyoti High School, Waraseoni', '2015-2016')
st.markdown("""
- Percent : `86.5%`
""")

#####################
st.markdown('''
## Work Experience
''')

txt('**Machine Learning Application Developer Intership** Technocolab Softwares Indore', 'Jun 2021- July 2021')
st.markdown("""
- Loan Repayment Model develop & Deploy on AWS.
- Importing, cleaning, preprocessing, feature engineering, develop Model, deploy AWS.
""")

st.markdown('''
## Use Tools
''')
txt4('Tableau', 'Data Visualization', 'https://www.tableau.com/')

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `C++`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`Streamlit`')
txt3('Model deployment', '`Streamlit`, `AWS`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'www.linkedin.com/in/omanshu-gaidhane-745a081b2')
txt2('GitHub', 'https://github.com/omanshu23')
