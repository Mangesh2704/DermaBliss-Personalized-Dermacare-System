import streamlit as st
from streamlit_option_menu import option_menu
from numpy.core.fromnumeric import prod
import tensorflow as tf
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image

# Import the Dataset 
skincare = pd.read_csv("exports_skincare.csv", encoding='utf-8', index_col=None)

# Header
st.set_page_config(page_title="Personalized Dermacare System", page_icon=":rose:", layout="wide",)

# 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
EXAMPLE_NO = 2

st.markdown("<h1 style='text-align: center;'>DermaBliss - Personalized Dermacare System ✨</h1>", unsafe_allow_html=True)
st.write("") 
st.write("")
st.write("") 
st.write("")  
def streamlit_menu(example=1):
    if example == 1:
        # 1. as sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Skin Care", "Get Recommendation", "Skin Care Tips"],  # required
                icons=["house", "stars", "book"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
        return selected

    if example == 2:
        # 2. horizontal menu w/o custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Skin Care", "Get Recommendation", "Skin Care Tips"],  # required
            icons=["house", "stars", "book"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        return selected

    if example == 3:
        # 2. horizontal menu with custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Skin Care", "Get Recommendation", "Skin Care Tips"],  # required
            icons=["house", "stars", "book"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
        )
        return selected


selected = streamlit_menu(example=EXAMPLE_NO)

if selected == "Skin Care":
    st.markdown("<h2 style='font-weight: bold; text-align: center;'>Welcome to Our Personalized Dermacare Experience</h2>", unsafe_allow_html=True)
    # st.title(f"{selected} Personalized Dermacare System :sparkles:")
    st.write('---') 
    st.write(
        """
        ##### **The Skin Care Personalized Dermacare System is an implementation of Machine Learning that can provide skin care personalized dermacare recommendations according to your skin type and problems**
        """)
    st.write('')
    # st.write('') 
    st.write(
        """
        ##### You will get recommendations for skin care personalized dermacare recommendations from various cosmetic brands with a total of 1200+ products tailored to your skin's needs. 
        ##### There are 5 categories of skin care products with 5 different skin types, as well as the problems and benefits you want to get from the products. This recommendation application is just a system that provides recommendations according to the data you enter, not a scientific consultation.
        ##### Please select the *Get Recommendation* page to start getting recommendations. Or select the *Skin Care Tips* page to see tips and tricks about skin care.
        """)
    
    st.write(
        """
        **Good luck :) !**
        """)
    # Displaying a local video file

    # video_file = open("skincare.mp4", "rb").read()
    # st.video(video_file, start_time = 1) #displaying the video 

# About Us
    st.markdown("<h2 style='font-weight: bold; text-align: center;'>About Us!</h2>", unsafe_allow_html=True)
    st.write('---') 
    # Create a two-column layout
    col1, col2 = st.columns([2, 1.5])  # Adjust the ratio as needed
    # Left column for content
    with col1:
        st.markdown(""" <p style='font-size:18px;'>    
        This system helps you find the best skincare solutions tailored to your needs.
        Fill out a quick questionnaire to get started, and let us help you achieve your skincare goals!</p>
        """, unsafe_allow_html=True)

        st.markdown(""" <p style='font-size:18px;'> 
        At <b>Skin Care Personalized Dermacare System</b>, we believe that every individual’s skin is unique and deserves tailored care. Our mission is to empower you with personalized skincare solutions that cater to your specific needs, concerns, and lifestyle.
        </p>""", unsafe_allow_html=True)

        st.markdown(""" <p style='font-size:18px;'> 
        Founded by a team of skincare enthusiasts and dermatologists, our platform combines advanced technology with expert knowledge to provide a seamless experience. Whether you’re dealing with acne, dryness, sensitivity, or simply seeking to enhance your natural glow, our system analyzes your skin type and preferences to recommend the best products and routines.
        </p>""", unsafe_allow_html=True)

        st.markdown(""" <p style='font-size:18px;'> Join us on your journey to radiant, healthy skin. Let’s make skincare a delightful and personalized experience together!</p>""", unsafe_allow_html=True)
    # Right column for image
    with col2:
        st.image("about2.png", caption="Your Skincare Journey", width=450, use_column_width=False)

# Our Approach
    st.markdown("<h2 style='font-weight: bold; text-align: center;'>Why Choose Us?</h2>", unsafe_allow_html=True)
    st.write('---') 
    # Create a two-column layout
    col1, col2 = st.columns([2.5, 2])  # Adjust the ratio as needed

    # Left column for content
    with col1:
        video_file = open("skincare.mp4", "rb").read()
        st.video(video_file, start_time = 1) # displaying the video 
    # Right column for image
    with col2:
        st.markdown(""" <p style='font-size:18px;'>    
        At <b>Skin Care Personalized Dermacare System</b>, we are dedicated to transforming the way you approach skincare. Our methodology is built on understanding your unique needs & providing solutions that truly work for you. Here’s how we do it:</p>
        """, unsafe_allow_html=True)
        st.write("""
        1. **Personalized Assessments**: Our in-depth questionnaires gather crucial information about your skin type, concerns, and lifestyle, ensuring that our recommendations are perfectly suited for you.
        2. **Expert-Driven Solutions**: We collaborate with dermatologists and skincare professionals to curate a comprehensive database of products and routines that are safe and effective.
        3. **Continuous Learning**: Skincare is an evolving field. We stay updated on the latest research and trends, so you receive the most current and relevant advice.
        4. **Community Support**: Join our community of skincare lovers where you can share experiences, tips, and support one another on your skincare journey.
        5. **Tailored Recommendations**: No more one-size-fits-all solutions! Our personalized approach means you get what works for you.
        6. **Quality Assurance**: We prioritize quality, ensuring that the products we recommend are effective and dermatologist-approved.
        7. **Holistic Focus**: Skincare is about more than just products. We provide guidance on lifestyle habits, diet, and routines that contribute to healthy skin.
        """)

    # st.info('Credit: Created by Group No. 09')

if selected == "Get Recommendation":
    st.markdown("<h2 style='font-weight: bold; text-align: center;'>Let's Get Recommendation</h2>", unsafe_allow_html=True)
    st.write('')
    st.write(
        """
        ##### **To get recommendations, please enter your skin type, complaints and desired benefits to get recommendations for the right skin care products.**
        """) 
    
    st.write('---') 

    first,last = st.columns(2)

    # Choose a product product type category
    # pt = product type
    category = first.selectbox(label='Product Category : ', options= skincare['product_type'].unique() )
    category_pt = skincare[skincare['product_type'] == category]

    # Choose a skin type
    # st = skin type
    skin_type = last.selectbox(label='Your Skin Type : ', options= ['Normal', 'Dry', 'Oily', 'Combination', 'Sensitive'] )
    category_st_pt = category_pt[category_pt[skin_type] == 1]

    # select complaint
    prob = st.multiselect(label='Skin Problems : ', options= ['Dull Skin', 'Acne', 'Acne Scars', 'Large Pores', 'Dark Spots', 'Fine Lines and Wrinkles', 'Blackheads', 'Uneven Skin Tone', 'Redness', 'Sagging Skin '] )

    # Choose notable_effects
    # From products that have been filtered based on product type and skin type (category_st_pt), we will take a unique value in the notable_effects column
    opsi_ne = category_st_pt['notable_effects'].unique().tolist()
    # The unique notable_effects-notable_effects are then put into the option_ne variable and used for the value in the multiselect which is wrapped in the selected_options variable below
    selected_options = st.multiselect('Notable Effects : ',opsi_ne)
    # We put the results of selected_options into the category_ne_st_pt var
    category_ne_st_pt = category_st_pt[category_st_pt["notable_effects"].isin(selected_options)]

    # Choose product
    # The products that have been filtered are in the filtered_df var, then we filter and take only the unique ones based on product_name and put them in the options_pn var
    opsi_pn = category_ne_st_pt['product_name'].unique().tolist()
    # Create a selectbox containing the product options that have been filtered above
    product = st.selectbox(label='Products Recommended for You', options = sorted(opsi_pn))
    # The product variable above will hold a product that will give rise to recommendations for other products

    ## MODELLING with Content Based Filtering
    # Initialize TfidfVectorizer
    tf = TfidfVectorizer()

    # Performing idf calculations on 'notable_effects' data
    tf.fit(skincare['notable_effects']) 

    # Mapping array from integer index features to name features
    tf.get_feature_names_out()

    # Perform the fit and then transform it into matrix form
    tfidf_matrix = tf.fit_transform(skincare['notable_effects']) 

    # View the tfidf matrix size
    shape = tfidf_matrix.shape

    # Converting tf-idf vector in matrix form with todense() function
    tfidf_matrix.todense()

    # Create a dataframe to view the tf-idf matrix
    # The column is filled with the desired effects
    # The line is filled with the product name
    pd.DataFrame(
        tfidf_matrix.todense(), 
        columns=tf.get_feature_names_out(),
        index=skincare.product_name
    ).sample(shape[1], axis=1).sample(10, axis=0)

    # Calculating cosine similarity on the tf-idf matrix
    cosine_sim = cosine_similarity(tfidf_matrix) 

    # Create a dataframe from the cosine_sim variable with rows and columns in the form of product names
    cosine_sim_df = pd.DataFrame(cosine_sim, index=skincare['product_name'], columns=skincare['product_name'])

    # Look at the similarity matrix for each product name
    cosine_sim_df.sample(7, axis=1).sample(10, axis=0)

    # Create a function to get recommendations
    def skincare_recommendations(nama_produk, similarity_data=cosine_sim_df, items=skincare[['product_name', 'brand', 'description']], k=5):

        # Retrieve data by using argpartition to partition indirectly along a given axis    
        # Dataframe converted to numpy
        # Range(start, stop, step)
        index = similarity_data.loc[:,nama_produk].to_numpy().argpartition(range(-1, -k, -1))

        # Retrieve data with the greatest similarity from the existing index
        closest = similarity_data.columns[index[-1:-(k+2):-1]]

        # Drop product_name so that the name of the product you are looking for does not appear in the recommendation list
        closest = closest.drop(nama_produk, errors='ignore')
        df = pd.DataFrame(closest).merge(items).head(k)
        return df

    # Create a button to display recommendations
    model_run = st.button('Find Other Product Recommendations!')
    # Get recommendations
    if model_run:
        st.write('Following are recommendations for other similar products according to what you want')
        st.write(skincare_recommendations(product))
    
    
if selected == "Skin Care Tips":
    st.markdown("<h2 style='font-weight: bold; text-align: center;'>Take a Look at Skin Care Tips</h2>", unsafe_allow_html=True)
    st.write('---') 

    st.write(
        """
        ##### **Below are tips and tricks that you can follow to maximize the use of skin care products**
        """) 
    
    image = Image.open('skin.png')
    st.image(image, caption='Skin Care Tips')
    
    st.write(
        """
        ### **1. Facial Wash**
        """)
    st.write(
        """
        **- Use facial wash products that have been recommended or that are suitable for you**
        """)
    st.write(
        """
        **- Wash your face a maximum of 2 times a day, namely in the morning and at night before bed. Washing your face too often will remove the skin's natural oils. For those of you who have a dry face, it doesn't matter if you just use plain water in the morning**
        """)
    st.write(
        """
        **- Don't scrub your face roughly because it can remove the skin's natural barrier**
        """)
    st.write(
        """
        **- The best way to cleanse the skin is to use your fingertips for between 30-60 seconds in circular and massaging movements**
        """)
    
    st.write(
        """
        ### **2. Toner**
        """)
    st.write(
        """
        **- Use a toner that has been recommended or is suitable for you**
        """)
    st.write(
        """
        **- Pour toner onto cotton then gently rub onto face. For maximum results, use 2 layers of toner, the first using cotton and the last using your hands to make it more absorbed**
        """)
    st.write(
        """
        **- Use toner after washing your face**
        """)
    st.write(
        """
        **- For those of you who have sensitive skin, as much as possible avoid skin care products that contain fragrance**
        """)
    
    st.write(
        """
        ### **3. Serum**
        """)
    st.write(
        """
        **- Use a serum that has been recommended or is suitable for you for maximum results**
        """)
    st.write(
        """
        **- Serum is used after the face is completely clean so that the serum content is absorbed completely**
        """)
    st.write(
        """
        **- Use the serum in the morning and evening before bed**
        """)
    st.write(
        """
        **- Choose a serum according to your needs, such as removing acne scars or removing black spots or anti-aging or other benefits**
        """)
    st.write(
        """
        **- The way to use serum so that it absorbs more completely is to pour it into the palm of your hand, then gently pat it on your face and wait until it is absorbed**
        """)
    
    st.write(
        """
        ### **4. Moisturizer**
        """)
    st.write(
        """
        **- Use a moisturizer that has been recommended or is suitable for you for maximum results**
        """)
    st.write(
        """
        **- Moisturizer is a mandatory skin care product that you must have because it is able to lock in moisture and various nutrients from the serum that has been used**
        """)
    st.write(
        """
        **- For maximum results, use a different moisturizer in the morning and evening. Morning moisturizer is usually equipped with sunscreen and vitamins to protect the skin from the bad effects of UV rays and pollution, while evening moisturizer contains various active ingredients that help the skin's regeneration process during sleep.**
        """)
    st.write(
        """
        **- Leave a time delay between using the serum and moisturizer for around 2-3 minutes to ensure the serum has been absorbed into the skin**
        """)
    
    st.write(
        """
        ### **5. Sunscreen**
        """)
    st.write(
        """
        **- Use sunscreen that has been recommended or is suitable for you for maximum results**
        """)
    st.write(
        """
        **- Sunscreen is the main key to all skin care products because it protects the skin from the harmful effects of UVA and UVB rays, even blue light. All skin care products will be useless if there is nothing to protect the skin**
        """)
    st.write(
        """
        **- Use sunscreen approximately the length of your index and middle fingers to maximize protection**
        """)
    st.write(
        """
        **- Re-apply sunscreen every 2-3 hours or as much as needed**
        """)
    st.write(
        """
        **- Keep using sunscreen even at home because the sun's rays at 10 o'clock and above still penetrate through the windows and when the weather is cloudy**
        """)
    
    st.write(
        """
        ### **6. Don't change your skin care**
        """)
    st.write(
        """
        **Frequently changing skin care products will cause facial skin to experience stress because it has to adapt to the product content. As a result, the benefits obtained are not 100%. Instead, use skin care products for months to see results**
        """)
    
    st.write(
        """
        ### **7. Consistent**
        """)
    st.write(
        """
        **The key to facial care is consistency. Be diligent and diligent in using skin care products because the results you get are not instant**
        """)
    st.write(
        """
        ### **8. Face is an asset**
        """)
    st.write(
        """
        **Various forms of humans are a gift given by the Creator. Take care of this gift well and truly as a form of gratitude. Choose products and care methods that suit your skin's needs. Using skin care products from an early age is the same as investing in old age.**
        """)
