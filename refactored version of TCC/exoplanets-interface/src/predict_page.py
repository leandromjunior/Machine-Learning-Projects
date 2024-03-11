import streamlit as st
import numpy as np
import pickle

def load_file():
    with open ("") as file:
        data = pickle.load(file)
    return data

data = load_file()

model = data

def predict_func():
    pass