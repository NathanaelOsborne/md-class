import streamlit as st

def main():
  st.title('Dermatology Machine Learning')
  st.write('This app using machine learning')
  
  #Input data by User
  erythema = st.slider('Erthema', min_value = 0, max_value = 10, value = 3)

if __name__ == "__main__":
  main()
