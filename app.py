import gradio as gr
import os

def test():
    return "Fraud Detection App Working Successfully"

demo = gr.Interface(
    fn=test,
    inputs=[],
    outputs="text",
    title="Fraud Detection System"
)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860))
    )
