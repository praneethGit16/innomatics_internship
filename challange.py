import streamlit as st
from pickle import load
st.markdown('<style>body{background-color: lightgoldenrodyellow;}</style>',unsafe_allow_html=True)
pickle_in = open('svmclassifier.pkl', 'rb')
classifier =load(pickle_in)


def prediction(col1,col2):
    prediction = classifier.predict([[col1,col2]])
    if prediction == 1:
        pred = "Yes"
    else:
        pred = "No"
    return pred


def main():
    st.header('Deployment Challenge')
    col1 = st.number_input('enter col1 value',min_value = -134.41,max_value = 134.48)
    col2 = st.number_input('enter col2 value',min_value = -116.65,max_value = 134.45)
    if st.button('Now Predict'):
        output=prediction(col1,col2)
        if st.info(output) == 'Yes':
                st.write(":sunglasses:")
        else:
            st.write(":angry:")




if __name__=='__main__':
    main()
