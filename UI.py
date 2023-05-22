import gradio as gr
import tensorflow as tf

model = tf.keras.models.load_model('StockPricePrediction.h5')

def predict_price(open_price, high_price, low_price, volume):
    prediction = model.predict([[open_price, high_price, low_price, volume]])
    return prediction[0][0]

inputs = [
    gr.inputs.Number(label="Open Price"),
    gr.inputs.Number(label="High Price"),
    gr.inputs.Number(label="Low Price"),
    gr.inputs.Number(label="Volume")
]

outputs = [
    gr.outputs.Textbox(label="Predicted Price")
]

gr.Interface(fn=predict_price, inputs=inputs, outputs=outputs).launch(share=True)

