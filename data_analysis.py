import pandas as pd

def load_data():
    # Загружаем данные из CSV
    df = pd.read_csv("youtube_data.csv")
    return df

def analyze_data(df):
    # Пример простого анализа:
    print("Общее количество видео:", len(df))
    print("Пример данных:\n", df.head())

    # Пример анализа: распределение по каналу
    channel_counts = df["Channel"].value_counts()
    print("Частота появления каналов:\n", channel_counts)

def main():
    # Загружаем данные
    df = load_data()

    # Проводим анализ
    analyze_data(df)

if __name__ == "__main__":
    main()
