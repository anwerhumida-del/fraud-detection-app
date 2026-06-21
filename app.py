import gradio as gr

def test():
    return "Fraud Detection App Working Successfully"

demo = gr.Interface(
    fn=test,
    inputs=[],
    outputs="text",
    title="Fraud Detection System"
)

if __name__ == "__main__":
    demo.launch()
