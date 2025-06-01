import gradio as gr 
from philosopher_engine import generate_spinozist_reply
from memory_manager import update_memory, save_session_log
from adequacy import compute_adequacy

def process_reflection(text):
    reply = generate_spinozist_reply(text)
    score = compute_adequacy(text)
    update_memory(text, reply, score)
    save_session_log(text, reply, score)
    return f"{reply}\n\nAdequacy Score: {score:.2f}"

with gr.Blocks() as demo:
    gr.Markdown("""
    # 🧠 SpiñO: Emotional Reflection Assistant  
    Reflect deeply with Spinoza-inspired insights — and track your philosophical journey.
    """)
    user_input = gr.Textbox(placeholder="What's on your mind?", label="Your Reflection", lines=2)
    reflect_button = gr.Button("Reflect")
    response_output = gr.Textbox(label="Answer", lines=4)
    reflect_button.click(fn=process_reflection, inputs=user_input, outputs=response_output)

if __name__ == "__main__":
    demo.launch()