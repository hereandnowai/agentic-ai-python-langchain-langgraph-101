import gradio as gr
from calculator import calculate

def run(a, operation, b):
    """Called when the user clicks Calculate; return the result as tesxt"""
    return str(calculate(a, operation, b))

demo = gr.Interface(
    fn=run,
    inputs=[
        gr.Number(label="First number"),
        gr.Radio(["add", "subtract", "multiply", "divide"], label="Operation", value="add"),
        gr.Number(label="Second Number")
    ],
    outputs=gr.Textbox(label="Result"),
    title="Simple Calculator",
    description="Python backend + Gradio frontend"
)

if __name__ == "__main__":
    demo.launch()