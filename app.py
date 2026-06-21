import gradio as gr
from tensorflow.keras.models import load_model
import joblib

model = load_model("fraud_detection_model.keras")
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("label_encoder.pkl")

def check():
    return f"Model Loaded Successfully | Classes: {list(encoder.classes_)}"

demo = gr.Interface(
    fn=check,
    inputs=[],
    outputs="text",
    title="Fraud Detection System"
)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860
    )
