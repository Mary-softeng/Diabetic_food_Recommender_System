import streamlit as st
import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from streamlit_option_menu import option_menu
from textblob import TextBlob
from PIL import Image

primaryColor="blue"
col1, mid, col2 = st.columns([1,1,10])
with col1:
    st.image('logo.PNG', width=100)
with col2:
    original_title = '<h1 style="font-family:Courier; color:#2596be; font-size: 40px;">Food Recommender System</h1>'
    st.markdown(original_title, unsafe_allow_html=True)
    
# let's do the navigation bar first
selected = option_menu(
    menu_title=None, options=['Home', 'Recommendation', 'Health Tips'], icons=['house', 'pen', 'book'], menu_icon='cast', default_index=0, orientation='horizontal'
)
if selected == 'Home':
    st.markdown("<h2 style='text-align: center; color: black;'>Diabetic Meal Plans </h2>", unsafe_allow_html=True)

    # st.header("Diabetic Meal Plans")
    st.subheader("Counting Carbs")
    col1, col2 = st.columns(2)
    with col1:
        st.write('''Counting carbohydrates (carbs) is a key strategy for meeting blood glucose levels. This is because the carbs in food are broken down into glucose. Insulin helps to regulate glucose levels.
         This is why counting them is so important.
         Knowing the number of carbs a person needs to eat each day is important to make carb-counting work. 
         ''')
        st.markdown("***************************************************")
    with col2:
         st.image("carbs.PNG")
         st.markdown("***************************************************")
    with col2:
        
        st.write('''The Diabetes Plate Method is the easiest way to create healthy meals that can help manage blood sugar since
        you can create perfectly portioned meals with a healthy balance of vegetables, protein, and carbohydrates—without any counting, calculating, weighing, or measuring. 
        All you need is a plate''')
        
    with col1:
        st.subheader("The Plate Method")
        st.image("platemethod.PNG")
        

if selected == 'Recommendation':


    st.subheader("Personal information")
    col1, col2, col3, col4,col5 = st.columns(5)

    with col1:
        name = st.text_input('What is your name:', '')

    with col2:
        col2 = st.radio("Select your Gender", ("Male", "Female"))

    with col3:
        col3 = st.text_input('Input your age', '')
    with col4:
        col4 = st.text_input('weight(kg):', '')
    with col5:
        col5 = st.text_input("Occupation")

    st.subheader("Food Selection And Recommendation")
    col1, col2 = st.columns(2)

    with col1:


        food = pd.read_csv("new.csv", encoding='cp1252')
        # First we need to convert the datatype to intergers before segmenting it

        def glycemic_class():
            food['Glycemic_index'] = food['Glycemic_index'].astype(int)

            # Lets now feature engineer different classes of aglycemic index
            food['Glycemic_Class'] = pd.cut(food['Glycemic_index'], bins=[0, 55, 70, food['Glycemic_index'].max(
            )], labels=['Low glycemic index', 'Mid glycemic index', 'High glycemic index'])

        glycemic_class()

        cuisine = st.selectbox("Choose the Category!", ['Baked', 'Fruits', 'Breakfast', 'Grains', 'Beans', 'Beverage',
                                                        'Vegetables ', 'Snacks', 'Cookies', 'Noodles', 'Dairy', 'Nuts', 'Salad', 'Chicken', 'Honey'])

        recommend = food[(food['Category'] == cuisine) & (
            food['Glycemic_Class'] == 'Low glycemic index')]
        
        ans = food.loc[(food.Category == cuisine), ['FOOD']]
        names = ans['FOOD'].tolist()
        x = np.array(names)
        ans1 = np.unique(x)

    finallist = ""
    
    bruh = st.button("Recommended Food")
    if bruh == True:
        st.write('These are your recommended Food:', name)
        recommend=recommend.drop(['Glycemic_index','Glycemic load per serving','Glycemic_Class'],axis=1)
        finallist =recommend.style.hide_index()
        
        st.write(finallist.to_html(columns=['FOOD','Serving size (grams)']), unsafe_allow_html=True)
        # if recommend.loc[(recommend['Category'] == 'Cookies') & (recommend['Category'] == 'Vegetables')]:
        #     st.write("The category is not recommended")
            
if selected ==("Health Tips"):
    st.write("Changing your lifestyle could be a big step toward diabetes prevention — and it's never too late to start. Consider these tips.")
    # lst = ['Choose healthier carbohydrates', 'Be more physically active', 'Eat healthy plant foods','Eat healthy fats','Cut down on added sugar',
    # 'Eat more fruit and veg']

    # for i in lst:

    
    #     st.markdown("- " + i)
    col1,col2,col3=st.columns(3)
    with col1:

        image = Image.open('carbohydrates.PNG')

        st.image(image, caption='Choose healthier carbohydrates')
    with col2:

        image = Image.open('vages.PNG')

        st.image(image, caption='Eat healthy plant foods')
    with col3:

        image = Image.open('excer.PNG')

        st.image(image, caption='Be more physically active')
    with col1:

        image = Image.open('fats.PNG')

        st.image(image, caption='Eat healthy fats')

    with col2:

        image = Image.open('low sugar.PNG')

        st.image(image, caption='Eat food with low Sugars')
    with col3:

        image = Image.open('less salt.PNG')

        st.image(image, caption='Eat less salt')
    with col1:

        image = Image.open('processed meat.PNG')

        st.image(image, caption='Eat less red and processed meat')
    with col2:

        image = Image.open('alcohol.PNG')

        st.image(image, caption='Drink alcohol sensibly')
