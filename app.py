import google.generativeai as genai
import streamlit as st
from PIL import Image


## Initialize our streamlit app
st.set_page_config(page_title="Skin & Makeup Analysis App")

st.image("images/maintitle.png")

menu = ["Home","About","Skin Analysis", "The Future"]

# Create columns to align buttons horizontally
# Since we have 4 buttons, we need 4 columns
col1, col2, col3, col4 = st.columns(len(menu))

# Display buttons in each column
with col1:
    if st.button("Home"):
        st.session_state.page = "Home"
with col2:
    if st.button("About"):
        st.session_state.page = "About"       
with col3:
    if st.button("Skin Analysis"):
        st.session_state.page = "Skin Analysis"
with col4:
    if st.button("The Future"):
        st.session_state.page = "The Future"

st.markdown('---')

# Initialize session state if not set
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Show content based on the selected page
page = st.session_state.page

# COlor Hex codes
teal = "#adcec8"
pink = "#fadbd3"
text = "#110301"
# Teal buttons: #adcec8
# Light pink: #fadbd3
# Text: #110301


# Formatting buttons with CSS
st.markdown("""
    <style>
    .stButton > button {
        height: auto;
        padding-top: 20px;
        padding-bottom: 20px;
        font-size: 20px;
        font-weight: bold;
        color: white;
        background-color: #adcec8;
        border: none;
        border-radius: 8px;
        width: 100%;
        cursor: pointer;
    }
    .stButton > button:hover {
        border: 2px solid #adcec8;
        background-color: white;
        color: #3E2C1C;
    }
    </style>
    """, unsafe_allow_html=True)

# <link href="https://fonts.googleapis.com/css2?family=The+Seasons&display=swap" rel="stylesheet"> - The Seasons
# <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet"> - Monserrat

# ===========================================================
# HOME PAGE
# ===========================================================
if page == "Home":
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=The+Seasons&display=swap" rel="stylesheet">
        <h1 style="color: #110301; font-family: 'The Seasons', serif; font-weight: bold; text-align: left;">
            The Smart Solution for Skin
        </h1>
        """, unsafe_allow_html=True)
        st.markdown("""
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
        <h6 style="color: #110301; font-family: 'Montserrat', sans-serif; font-weight: normal; text-align: left;">
            Blending the power of advanced AI technology with completely personalized beauty insights to provide
            your customers with tailored skin analysis and makeup recommendations.
        </h6>
        """, unsafe_allow_html=True)
    with col2:
        st.image("images/skincare.gif")

    st.markdown('---')

    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=The+Seasons&display=swap" rel="stylesheet">
    <h1 style="color: #110301; font-family: 'The Seasons', serif; font-weight: bold; text-align: center;">
        What we do
    </h1>
    """, unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div style="background-color: {pink}; padding: 20px; border-radius: 10px;">
            <link href="https://fonts.googleapis.com/css2?family=The+Seasons&display=swap" rel="stylesheet">
            <h5 style="color: #110301; font-family: 'The Seasons', serif; font-weight: bold; text-align: center;">
                AI-Powered Precision
            </h5>
            <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
            <h6 style="color: #110301; font-family: 'Montserrat', sans-serif; font-weight: normal; text-align: center;">
                Detailed skin tone analysis, color matching, and skin-care routine recommendations
            </h6>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div style="background-color: {pink}; padding: 20px; border-radius: 10px;">
            <link href="https://fonts.googleapis.com/css2?family=The+Seasons&display=swap" rel="stylesheet">
            <h5 style="color: #110301; font-family: 'The Seasons', serif; font-weight: bold; text-align: center;">
                Tailored Product Suggestions
            </h5>
            <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
            <h6 style="color: #110301; font-family: 'Montserrat', sans-serif; font-weight: normal; text-align: center;">
                Discover make up products and skincare solutions that align perfectly with individual skin goals.
            </h6>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div style="background-color: {pink}; padding: 20px; border-radius: 10px;">
            <link href="https://fonts.googleapis.com/css2?family=The+Seasons&display=swap" rel="stylesheet">
            <h5 style="color: #110301; font-family: 'The Seasons', serif; font-weight: bold; text-align: center;">
                Guided <br>Expertise
            </h5>
            <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
            <h6 style="color: #110301; font-family: 'Montserrat', sans-serif; font-weight: normal; text-align: center;">
                Ingredient recommendations and routine enhancements for specific concerns.
            </h6>
        </div>
        """, unsafe_allow_html=True)
    st.write('')

    st.markdown('---')

    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=The+Seasons&display=swap" rel="stylesheet">
    <h1 style="color: #110301; font-family: 'The Seasons', serif; font-weight: bold; text-align: left;">
        How It Works
    </h1>
    """, unsafe_allow_html=True)
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
    <h6 style="color: #110301; font-family: 'Montserrat', sans-serif; font-weight: normal; text-align: left;">
        Blending the power of advanced AI technology with completely personalized beauty insights to provide
        your customers with tailored skin analysis and makeup recommendations.
    </h6>
    """, unsafe_allow_html=True)


# ===========================================================
# SKIN ANALYSIS PAGE
# ===========================================================

if page == "Skin Analysis":
    st.header("AI-Powered Skin and Makeup Recommendation")

    genai.configure(api_key='AIzaSyBwJNX-khO8qZg-UvNtz6JPOyTkBJUUlWI')

    ## Prompt Engineering for Skin & Makeup Recommendations
    def generate_skin_analysis_prompt(input, image):
        # Construct a prompt based on user input and the uploaded image for better skin analysis
        prompt = f" Given the uploaded image of a person or a face and the descript of their skin \
                condition as '{input}' (where they might additionally give comments on their skin \
                problems), analyze their skin tone and type. If the input image '{image}' is not \
                in in good quality, try your best to analyze from what you can see. Never state \
                explicitly that you cannot do an analysis but instead, say that this is the best \
                that you can do and that for them to get better results, provide a better image but \
                do the complete analysis as best as possible. But do not ever mention that the image \
                quaity is bad. First, provide an overview of their analysis. Then, \
                provide a detailed color analysis for potential foundation shades and possible shade \
                ranges. Give them the average hex code of their skin and from this analysis, give them \
                a full color analysis on whether they are a cool, warm, or neutral tone and what \
                undertones they have and whether summer, winter, autumn, spring colors suit them better. \
                Then in the make-up section, recommend products such as foundation, concealer, and blush \
                that best matches their skin conditions and give them reasons why. Recommend them precise \
                products from brands. Make sure that you also \
                list out ingredients in products that they should look for or to avoid to target their skin \
                problems or goals. Also try to highlight some things that they should be doing or avoiding \
                in their skin care routine and make the best possible recommendation of a skin care routine \
                for them. This should include specific product that they should use and the reasons why. \
                All of these recommendations should focus on the person and potential product as this \
                will be integrated with make up stores."
        return prompt

    ## Function to the model and get responses
    def get_gemini_response(input, image):
        model = genai.GenerativeModel('gemini-1.5-flash')
        if input != "":
            prompt = generate_skin_analysis_prompt(input, image)
            response = model.generate_content([prompt, image])
        else:
            response = model.generate_content(image)
        return response.text



    # Text input for skin condition
    input = st.text_input("Describe your skin condition (e.g., dry, oily, combination, acne-prone): ", key="input")

    # File uploader for the image
    uploaded_file = st.file_uploader("Upload your face image...", type=["jpg", "jpeg", "png"])

    image = ""   
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.")

    # Button to submit the request
    submit = st.button("Get Makeup & Skincare Recommendations")

    # Logic to handle the submission of the form based on what the user has input
    if submit:
        if input != "" and image != "":
            # If both text and image are provided, process both
            response = get_gemini_response(input, image)
        elif input != "":
            # If only text is provided
            response = get_gemini_response(input, None)
        elif image != "":
            # If only image is provided
            response = get_gemini_response("", image)
        else:
            response = "Please upload an image or provide a description of your skin condition."
        
        # Display the response
        st.subheader("The AI's Analysis and Recommendations:")
        st.write(response)
