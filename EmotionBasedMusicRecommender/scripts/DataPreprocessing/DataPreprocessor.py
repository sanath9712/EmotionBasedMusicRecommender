import os
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

# Download stopwords from NLTK
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_text(text, remove_stopwords=False):
    """
    Function to clean the text data.
    - Lowercase the text
    - Remove special characters and punctuations
    - Remove any extra spaces
    - Optionally, remove stop words
    """
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\[.*?\]', '', text)  # Remove text in square brackets
    text = re.sub(r'[%s]' % re.escape('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'), '', text)  # Remove punctuation
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    if remove_stopwords:
        text = ' '.join(word for word in text.split() if word not in stop_words)
    return text.strip()

def preprocess_file(file_path, emotions, remove_stopwords=False):
    """
    Preprocess a single file:
    - Load the CSV file.
    - Remove duplicate dialogues.
    - Exclude dialogues that contain brackets or become empty after preprocessing.
    - Drop rows where 'Dialogue' is empty or 'Emotions' is 'Unknown'.
    - Clean the 'Dialogue' text.
    - Perform one-hot encoding for emotions.
    - Remove the original 'Dialogue' and 'Emotions' columns.
    """
    # Load the file
    df = pd.read_csv(file_path)

    # Remove duplicate dialogues
    df = df.drop_duplicates(subset=['Dialogue'])

    # Handle NaN values in 'Dialogue' column
    df['Dialogue'] = df['Dialogue'].fillna('')

    # Exclude dialogues with brackets
    df = df[~df['Dialogue'].str.contains(r"\(|\)")]

    # Drop rows with empty 'Dialogue' or 'Emotions' as 'Unknown'
    df = df.dropna(subset=['Dialogue'])
    df = df[df['Emotions'] != 'Unknown']

    # Clean 'Dialogue' text
    df['Cleaned_Dialogue'] = df['Dialogue'].apply(lambda x: clean_text(x, remove_stopwords))

    # Exclude dialogues that become empty after preprocessing
    df = df[df['Cleaned_Dialogue'] != '']

    # One-hot encoding for emotions
    for emotion in emotions:
        df[emotion] = df['Emotions'].apply(lambda x: 1 if emotion in str(x) else 0)

    # Remove the original 'Dialogue' and 'Emotions' columns
    df.drop(['Dialogue', 'Emotions'], axis=1, inplace=True)

    return df

def process_directory(directory_path, emotions, remove_stopwords=False):
    """
    Process all files in a given directory and combine them into a single DataFrame.
    """
    all_data = pd.DataFrame()

    for file in os.listdir(directory_path):
        if file.endswith('.csv'):
            file_path = os.path.join(directory_path, file)
            df = preprocess_file(file_path, emotions, remove_stopwords)
            all_data = pd.concat([all_data, df], ignore_index=True)

    return all_data

# List of emotions for one-hot encoding
emotions = [
    "Happiness", "Contentment", "Confidence", "Neutral", "Sadness",
    "Anger", "Fear", "Surprise", "Disgust", "Love",
    "Excitement", "Anticipation", "Nostalgia", "Confusion",
    "Frustration", "Longing", "Optimism"
]

# Directory containing the CSV files
directory_path = 'data/FinalData'  # Replace with your directory path

# Process the directory with original preprocessing and save
unified_data_original = process_directory(directory_path, emotions)
unified_data_original.to_csv('data/Finalpreprocessed_data.csv', index=False)

# Process the directory with stop words removed and save
unified_data_no_stopwords = process_directory(directory_path, emotions, remove_stopwords=True)
unified_data_no_stopwords.to_csv('data/Finalpreprocessed_data_no_stopwords.csv', index=False)
