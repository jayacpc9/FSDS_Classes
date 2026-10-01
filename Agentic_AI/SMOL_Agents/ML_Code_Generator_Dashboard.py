import os
import litellm
import gradio as gr
from dotenv import load_dotenv
from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel
import google.generativeai as genai

load_dotenv()
# Set Google Gemini API Key Securely
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini Model for SmolAgents
model = LiteLLMModel(
    model_id=os.getenv("GEMINI_MODEL"),
    api_key=os.getenv("GEMINI_API_KEY")
)

# Define the ML Code Generation Agent
ml_code_agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    additional_authorized_imports=['pandas', 'numpy', 'sklearn', 'json'],
    model=model
)

# Function to Generate ML Code dynamically based on uploaded file and user prompt
def generate_ml_code(dataset_file, user_prompt):
    if dataset_file is None:
        return "Error: Please upload a dataset file."
    if not user_prompt.strip():
        return "Error: Please enter a prompt describing what you want to do."

    file_path = dataset_file if isinstance(dataset_file, str) else dataset_file.name

    full_prompt = f"""
    You are an AI assistant helping with machine learning code.
    The user has uploaded a dataset located at this exact file path: {file_path}
    User Request: {user_prompt}
    Instructions:
    1. Load the dataset from the file path provided above using pandas.
    2. Perform the machine learning tasks requested by the user.
    3. Unless explicitly asked to search the web, write the script using your offline knowledge to save time.
    4. Ensure you return the fully working Python code and clearly state the final results or metrics.
    """
    try:
        response = ml_code_agent.run(full_prompt)
        return response
    except Exception as e:
        return f"Error: {str(e)}"

# Frontend Customization: JavaScript for Dark/Light Theme Switching
toggle_theme_js = """
() => {
    document.body.classList.toggle('dark');
    document.querySelector('html').classList.toggle('dark');
}
"""

# Frontend Customization: Technical Texture and Compact UI Components
custom_css = """
/* Technical Dot-Matrix Background Texture - Light Mode */
.gradio-container, body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #f9fafb !important;
    background-image: radial-gradient(#e5e7eb 1.5px, transparent 1.5px) !important;
    background-size: 16px 16px !important;
}

/* Technical Dot-Matrix Background Texture - Dark Mode */
.dark .gradio-container, .dark body {
    background-color: #0b0f19 !important;
    background-image: radial-gradient(#1e293b 1.5px, transparent 1.5px) !important;
    background-size: 16px 16px !important;
}

.title-header {
    text-align: center;
    margin-bottom: 10px;
}

/* Compact Rounded Theme Button Customization */
.theme-toggle-btn {
    max-width: 105px !important;
    height: 34px !important;
    padding: 0px 8px !important;
    font-size: 0.85em !important;
    border-radius: 20px !important;
    margin-top: 16px !important;
    float: right;
}

/* Primary Action Button Customization */
.generate-btn {
    background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%) !important;
    color: white !important;
    border: none !important;
    font-weight: bold !important;
    border-radius: 8px !important;
}
.generate-btn:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
}

/* Glassmorphism Workspace Container Panels */
.group-card {
    border: 1px solid #e5e7eb !important;
    background-color: rgba(255, 255, 255, 0.85) !important;
    backdrop-filter: blur(4px);
    border-radius: 12px !important;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05) !important;
    padding: 15px !important;
}
.dark .group-card {
    border: 1px solid #1e293b !important;
    background-color: rgba(17, 24, 39, 0.85) !important;
    backdrop-filter: blur(4px);
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3) !important;
}
"""

# Constructing the Responsive Dashboard Layout
with gr.Blocks(theme=gr.themes.Soft(), css=custom_css) as iface:
   
    # Header Section with Scaled-down Mode Switcher
    with gr.Row():
        with gr.Column(scale=9):
            gr.Markdown(
                """
                <div class='title-header'>
                    <h1>📊 ML Code Generator Dashboard</h1>
                    <p style='font-size: 1.1em; color: #6b7280;'>Intelligent Python Pipeline Creator</p>
                </div>
                """
            )
        with gr.Column(scale=1, min_width=120):
            theme_btn = gr.Button("🌓 Mode", variant="secondary", elem_classes="theme-toggle-btn")
            theme_btn.click(None, None, None, js=toggle_theme_js)

    gr.Markdown("---")

    # Main Workspace Grid
    with gr.Row():
        # Configuration Inputs (Left Container)
        with gr.Column(scale=1, elem_classes="group-card"):
            gr.Markdown("### 📥 1. Configuration & Data Input")
            dataset_input = gr.File(label="Upload Dataset (CSV/Excel)")
            prompt_input = gr.Textbox(
                lines=5,
                placeholder="Describe your processing target here...\nExample: Train a Logistic Regression model to predict 'Returned' using 'Price'. Keep it simple and skip web searches.",
                label="Enter Machine Learning Tasks"
            )
            submit_btn = gr.Button("🚀 Generate ML Analytics", variant="primary", elem_classes="generate-btn")
       
        # Display Logs & Code Output (Right Container)
        with gr.Column(scale=1, elem_classes="group-card"):
            gr.Markdown("### 💻 2. Execution Logs & Generated Script")
            output_text = gr.Textbox(
                label="AI Workspace Output",
                lines=16,
                interactive=False
            )

    # Core Execution Trigger Link
    submit_btn.click(
        fn=generate_ml_code,
        inputs=[dataset_input, prompt_input],
        outputs=output_text
    )

    # Footer Signature Element
    gr.Markdown(
        """
        <br>
        <div style='text-align: center; font-size: 0.9em; color: #9ca3af;'>
            Application Framework Platform • Created by 
        </div>
        """
    )

if __name__ == "__main__":
    iface.launch()