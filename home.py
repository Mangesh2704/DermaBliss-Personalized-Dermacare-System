ortfrom numpy.core.fromnumeric import prod
import tensorflow as tf
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# Import the Dataset 
skincare = pd.read_csv("exports_skincare.csv", encoding='utf-8', index_col=None)

# Header
st.set_page_config(page_title="Personlized Dermacare System", page_icon=":blossom:", layout="wide",)

# Displays the main page
st.title("Personlized Dermacare System :sparkles:")

st.write('---') 

# Displaying a local video file

video_file = open("skincare.mp4", "rb").read()
st.video(video_file, start_time = 1) # Displaying the video 


st.write('---') 

st.write(
    """
    ##### **AThe Skin Care Product Recommendation application is an implementation of a Machine Learning project that can provide skin care product recommendations according to your skin type and problems. You can enter your skin type, complaints and desired benefits to get recommendations for the right skin care products**
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
    st.snow()
