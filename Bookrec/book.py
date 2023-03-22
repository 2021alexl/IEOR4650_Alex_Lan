
import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/2021alexl/IEOR4650_Alex_Lan/main/Bookrec/Books.csv')

def edit_distance(str1, str2):
    # Initialize a 2D array to store the edit distances
    dp = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
    
    # Initialize the first row and column
    for i in range(len(str1) + 1):
        dp[i][0] = i
    for j in range(len(str2) + 1):
        dp[0][j] = j
        
    # Calculate the edit distance
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
    # Return the edit distance
    return dp[-1][-1]

def main():
    st.session_state.choose = 0
    st.session_state.input = 0
    st.session_state.ed = 0
    st.session_state.bl = 0
    st.session_state.df = 0
    st.session_state.select = 0
    # Define the sidebar
    st.sidebar.title("Hi! I am librarian Mr.Lan📚")
    with st.sidebar:
        with st.expander("Introduction", expanded=False):
            content1 = 'I am utilizing a comprehensive and diverse collection of books as my dataset to conduct collaborative filtering, a technique that aims to analyze the preferences and behaviors of users to generate personalized recommendations. With the ultimate goal of delivering an unparalleled book recommendation experience, I am working diligently to develop a sophisticated and advanced collaborative filtering model that takes into account various factors such as user ratings, book genres, author preferences, and publication dates. By combining state-of-the-art machine learning algorithms with cutting-edge data analysis techniques, my aspiration is to create a recommendation system that is both accurate and intuitive, capable of catering to the unique tastes and interests of each individual user. '
            markdown_text = f"<p style='font-family:sans-serif; color:#8B0000; font-size: 16px;'>{content1}</p>"
            st.markdown(markdown_text, unsafe_allow_html=True)
        favbook = st.text_input("Tell me about your favorite book, and I will make recommendation!")
        if len(favbook) > 0:
            st.session_state.input = 1
        if st.session_state.input == 1:
            if st.button("Let's Find!", key = 2):
                st.write('success')
                df = pd.read_csv('https://raw.githubusercontent.com/2021alexl/IEOR4650_Alex_Lan/main/Bookrec/Books.csv')
                booklist = df['Book-Title'].tolist()
                editdistance = []
                for i in range(len(booklist)): 
                    if 1 == 1:
                        f = []
                        f += [booklist[i]] 
                        f += [edit_distance(str(favbook), str(booklist[i]))] 
                        editdistance += [f]
                st.session_state.ed = editdistance
                st.session_state.bl = booklist
                st.session_state.df = df
                if st.session_state.ed != 0:
                    editdistance = st.session_state.ed
                    searchbase = 0
                    st.session_state.select = False
                    select = [i[0] for i in editdistance[:6]]
                    option = st.selectbox(
    'How would you like to be contacted?',select
                    )
                    st.write('You selected:', option)
                    st.session_state.select = option
                    st.write('Do you mean any of those book?')
                    if st.button("Let's Find!", key = 4):
                        st.session_state.choose = 1
    content2 = 'Alex Lan Book Recommendation📖'            
    markdown_text = f"<p style='font-family:sans-serif; color:#8B0000; font-size: 28px;'>{content2}</p>"
    st.markdown(markdown_text, unsafe_allow_html=True)
    st.image(
        "https://raw.githubusercontent.com/2021alexl/IEOR4650_Alex_Lan/main/Bookrec/main.png",
        width=500)
    
    
    col1, col2 = st.columns([1, 1], gap="large")
    if st.session_state.choose == 1:
        if st.session_state.select != 0:
            for i in range(4):
                booklist = st.session_state.bl 
                df= st.session_state.df = df
                number = int(np.random.randint(1,len(booklist),1))
                book_title = df['Book-Title'][number]
                book_author = df['Book-Author'][number]
                col = 0
                if i%2 == 0:
                    col = col1
                else: 
                    col = col2
                with col:
                    content = 'Recommendation '
                    content += str(i+1)
                    content14= '_________'
                    markdown_text = f"<p style='font-family:sans-serif; color:#8B0000; font-size: 24px;'>{content}</p>"
                    markdown_text2 = f"<p style='font-family:sans-serif; color:#8B0000; font-size: 24px;'>{content14}</p>"
                    
                    st.markdown(markdown_text, unsafe_allow_html=True)
                    st.markdown(markdown_text2, unsafe_allow_html=True)

                    st.markdown(
                        " ".join([
                            "<div class='r-text-recipe'>",
                            "<div class='food-title'>",
                            f"<h4 class='font-title text-bold'>{book_title}</h4>",
                            "</div>",
                            '<div class="divider"><div class="divider-mask"></div></div>',
                            "<h4 class='ingredients font-body text-bold'>Author: </h4>",
                            f"<h5 class='font-title text-bold'>{book_author}</h5>",
                            "</div>"
                        ]),
                        unsafe_allow_html=True
                    )
                    content13 = '     '
                    markdown_text4 = f"<p style='font-family:sans-serif; color:#8B0000; font-size: 24px;'>{content13}</p>"
                    st.markdown(markdown_text4, unsafe_allow_html=True)
                    st.markdown(markdown_text4, unsafe_allow_html=True)

    

if __name__ == "__main__":
    main()
