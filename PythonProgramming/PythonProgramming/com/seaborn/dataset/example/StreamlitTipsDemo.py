import streamlit as st
import TipsDataset as tips
import matplotlib.pyplot as plt

st.title("Streamlit : Tips Dataset Demo")
st.write("This is a simple app to visualize the tips dataset using seaborn.")
# 1. Define your options list
all_columns = tips.get_df_coloumns()
fig, ax = plt.subplots(figsize=(8, 6))

# function create and display plot
def display_plot(title, plot_func):
    st.subheader(title)
    plot_func()
    st.pyplot(fig)
    plt.close(fig)


# 2. Add multiple dropdown menus (selectbox)

# 2. Create a form container
with st.form("sns_dataset_form"):
    st.write("### select your attributes and click Submit to generate the graph:")
    x_axis = st.selectbox(
        label="Select x-axis attribute:",
        options=all_columns
    )

    y_axis = st.selectbox(
        label="Select y-axis attribute:",
        options=all_columns
    )

    hue_val = st.selectbox(
        label="Select Hue : ",
        options=all_columns
    )


    # checkbox_states = {}
    #
    # for column in all_columns:
    #     checkbox_states[column] = st.checkbox(column)
    #
    submitted = st.form_submit_button("Submit Selections")



# 4. Process the data only AFTER submission
if submitted:
    # Filter the dictionary to get checked items
    # selected_fruits = [fruit for fruit, checked in checkbox_states.items() if checked]

    st.success(f"Form submitted successfully!")
    st.write(f"**Selected Items:** \nx_axis : {x_axis}\n , y_axis : {y_axis}\n , hue_val : { hue_val} ")
    display_plot("scatter plot ", lambda: tips.scatter_plot(ax, x_axis, y_axis, hue_val))

# display_plot("scatter plot ", lambda: tips.scatter_plot(ax, "total_bill", "tip", "time"))

