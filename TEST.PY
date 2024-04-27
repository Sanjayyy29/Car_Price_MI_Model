import streamlit as st

def main():
    st.title("Background Image Example")

    # Load the background image
    background_image = "https://images.pexels.com/photos/168938/pexels-photo-168938.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"

    # Set CSS style to display the background image
    st.markdown(
        f"""
        <style>
            .reportview-container {{
                background: url("{background_image}") no-repeat center center fixed;
                background-size: cover;
            }}

            .st-emotion-cache-uf99v8 {{
        display: flex;
        flex-direction: column;
        width: 100%;
        overflow: auto;
        -webkit-box-align: center;
        align-items: center;
        background: red;
        background: url(https://images.pexels.com/photos/168938/pexels-photo-168938.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1) no-repeat center center fixed;
    }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Add other Streamlit components
    st.write("This is some text on the background image.")

if __name__ == "__main__":
    main()


# background_image = ""

#     # Set CSS style to display the background image
# st.markdown(
#         f"""
#         <style>
#             .reportview-container {{
#                 background: url("{background_image}") no-repeat center center fixed;
#                 background-size: cover;
#             }}

#             .st-emotion-cache-uf99v8 {{
#         display: flex;
#         flex-direction: column;
#         width: 100%;
#         overflow: auto;
#         -webkit-box-align: center;
#         align-items: center;
#         background: red;
#         background: url(https://images.unsplash.com/photo-1542281286-9e0a16bb7366) no-repeat center center fixed;
#     }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# st.image('image/car.jpg', use_column_width ="auto" , caption='car price prdiction')