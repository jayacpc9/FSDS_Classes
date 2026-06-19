import streamlit as st
import TipsDataset as tips
import matplotlib.pyplot as plt

st.title("Streamlit : Tips Dataset Demo")
# st.write("This is a simple app to visualize the tips dataset using seaborn.")

all_columns = tips.get_df_coloumns()
fig, ax = plt.subplots(figsize=(8, 6))


def display_plot(title, plot_func):
    st.subheader(title)
    plot_func()
    st.pyplot(fig)
    plt.close(fig)


all_graph_types = ["Select a graph", "Histogram", "Scatter Plot", "Box Plot"]
# 2. Add multiple dropdown menus (selectbox)
graph_type = st.sidebar.selectbox(
    label="Graph type :",
    options=all_graph_types
)
selected_graph_index = all_graph_types.index(graph_type)
if (selected_graph_index != 0):
    with st.sidebar.form("sns_dataset_form"):
        st.write("### Select your attributes to generate a graph:")

        x_axis = st.selectbox(
            label="X-axis attribute:",
            options=all_columns
        )
        if (selected_graph_index != 1):
            y_axis = st.selectbox(
                label="Y-axis attribute:",
                options=all_columns
            )

            hue_val = st.selectbox(
                label="Hue : ",
                options=all_columns
            )


        submitted = st.form_submit_button("Generate Graph")
    log_message =f"**Selected Items:**"
    if submitted:
        st.success(f"Form submitted successfully!")
        match selected_graph_index:
            case 1:
                log_message+=f"x = {x_axis} "
                display_plot("Histogram plot ", lambda: tips.hist_plot(ax, x_axis))
            case 2:
                log_message+=f"x = {x_axis} , y = {y_axis} , hue = {hue_val} "
                display_plot("scatter plot ", lambda: tips.scatter_plot(ax, x_axis, y_axis, hue_val))
            case 3:
                log_message+=f"x = {x_axis} , y = {y_axis} , hue = {hue_val} "
                display_plot("Box plot ", lambda: tips.box_plot(ax, x_axis, y_axis, hue_val))
        st.write(log_message)