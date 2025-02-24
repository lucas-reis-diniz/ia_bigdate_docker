import pandas as pd
import re
import string

def load_data(file_path):
    return pd.read_csv(file_path)

def clean_text(text):
    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def preprocess_data(df, text_column="Text"):
    print("📊 Colunas disponíveis no DataFrame:", df.columns)
    print("🔍 Procurando pela coluna:", text_column)

    if text_column not in df.columns:
        raise KeyError(f"A coluna '{text_column}' não existe no DataFrame. Colunas disponíveis: {data.columns}")

    df = df.dropna(subset=[text_column])
    df[text_column] = df[text_column].astype(str).apply(clean_text)
    return df

def save_preprocessed_data(df, output_path):
    df.to_csv(output_path, index=False)

def main():
    input_file = "/app/sentiment_analysis/dataset/Reviews.csv"
    output_path = "/app/sentiment_analysis/dataset/Reviews_preprocessed.csv"

    print("🔄 Loading data...")
    df = load_data(input_file)

    print("✨ Preprocessing data...")
    df = preprocess_data(df, text_column="Text")

    print("💾 Saving preprocessed data...")
    save_preprocessed_data(df, output_path)
    print(f"✅ Preprocessed data saved to {output_path}")

    print("✅ Done!")
    
if __name__ == "__main__":
    main()



