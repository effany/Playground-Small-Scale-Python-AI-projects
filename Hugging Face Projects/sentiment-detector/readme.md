# Sentiment Detector 😿🤩

A simple GUI application that analyzes the sentiment of your text using Hugging Face's transformers library.

## Features

- Enter any sentence and get instant sentiment feedback
- Visual emoji responses:
  - 🤩 for **positive** sentiment
  - 😿 for **negative** sentiment
  - 🫨 default/neutral state

## Tech Stack

- **Python** with Tkinter for the GUI
- **Hugging Face Transformers** for sentiment analysis
- **Model**: `distilbert-base-uncased-finetuned-sst-2-english`

## Installation

```bash
pip install transformers torch
```

## Usage

```bash
python main.py
```

Type a sentence in the input field and click the emoji button to analyze its sentiment!

## How It Works

1. User enters text in the input field
2. Clicks the emoji button to trigger analysis
3. The DistilBERT model classifies the text as POSITIVE or NEGATIVE
4. The emoji updates accordingly and resets after 2 seconds
