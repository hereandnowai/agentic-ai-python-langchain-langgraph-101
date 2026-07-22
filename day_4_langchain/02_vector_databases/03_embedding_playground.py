import os  # brings in tools to read settings from the computer, like secret keys
import matplotlib; matplotlib.use("Agg")  # brings in the drawing toolkit and sets it to draw without a screen
import matplotlib.pyplot as plt  # brings in the part of the toolkit that makes charts, nicknamed plt
import numpy as np  # brings in a fast number-crunching toolkit, nicknamed np
from sklearn.decomposition import PCA  # brings in a helper that shrinks long number lists down to two for plotting
from langchain_openai import OpenAIEmbeddings  # brings in a helper that turns text into lists of numbers
from dotenv import load_dotenv  # brings in a helper that loads secret settings from a file
from pydantic import SecretStr  # brings in a safe wrapper for holding secret text like a key
import gradio as gr  # brings in a toolkit for making a simple web window

load_dotenv()  # reads the hidden .env file so secret keys become available
emdeddings = OpenAIEmbeddings(  # sets up the text-to-numbers helper with the settings below
    model=os.environ.get("EMBED_MODEL", "openai/text-embedding-3-small"),
    base_url="https://openrouter.ai/api/v1",
    api_key=SecretStr(os.environ["OPENROUTER_API_KEY"]),
    check_embedding_ctx_length=False,
)

def word_map(text):  # a recipe that draws a picture showing which words are close in meaning
    words = [w.strip() for w in text.split(",") if w.strip()]  # splits the text at commas into a clean list of words
    vectors = np.array(emdeddings.embed_documents(words))  # turns every word into a list of numbers and stacks them together
    xy = PCA(n_components=2).fit_transform(vectors)  # squeezes each long list down to just two numbers so it can be plotted
    fig, ax = plt.subplots()  # makes a blank chart to draw on
    for word, point in zip(words, xy):  # goes through each word and its spot on the chart
        ax.scatter(point[0], point[1], color="purple")  # draws a purple dot at that word's spot
        ax.annotate(word, point)  # writes the word next to its dot
    return fig  # gives back the finished chart

demo = gr.Interface(word_map,  # builds a web window that runs the word_map recipe
                    gr.Textbox(label="Words (comma separated)", value="home loan, credit score, savings account, interest rate, mortgage, python, java, machine learning, artificial intelligence, data science"),
                    gr.Plot(), title="Word Map - close dots mean similar meaning")

if __name__ == "__main__":  # runs the part below only when this file is started directly
    demo.launch()  # opens the word-map window in the browser
