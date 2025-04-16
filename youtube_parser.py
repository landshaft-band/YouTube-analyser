import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException

# Функция для настройки и запуска Selenium
def setup_driver():
    options = webdriver.ChromeOptions()
    # Указываем путь к пользовательским данным профиля
    options.add_argument(r"user-data-dir=C:\Users\Дима\AppData\Local\Google\Chrome\User Data")
    options.add_argument(r"profile-directory=Profile 11")  # Заменить на точное имя твоего профиля

    # Указываем, что мы хотим, чтобы браузер был в максимизированном виде
    options.add_argument("--start-maximized")

    # Запускаем драйвер с использованием установщика ChromeDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver


# Функция для прокрутки страницы и сбора данных
def scroll_and_collect(driver, max_videos=100):
    from selenium.common.exceptions import TimeoutException

    video_data = []

    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, 'contents'))
        )
    except TimeoutException:
        print("Не удалось загрузить страницу в отведенное время.")
        driver.quit()
        return []

    seen_titles = set()

    while len(video_data) < max_videos:
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)

        videos = driver.find_elements(By.XPATH, '//ytd-rich-item-renderer')

        for video in videos:
            try:
                title_el = video.find_element(By.XPATH, './/*[@id="video-title"]')
                channel_el = video.find_element(By.XPATH, './/*[@id="channel-name"]//a')
                thumb_el = video.find_element(By.XPATH, './/*[@id="thumbnail"]//img')

                # duration может отсутствовать
                try:
                    time_el = video.find_element(By.XPATH,
                                                 './/*[@id="overlays"]//div[@class="thumbnail-overlay-badge-shape"]')
                    duration = time_el.text.strip()
                except:
                    duration = "N/A"

                title = title_el.text.strip()
                if title in seen_titles:
                    continue
                seen_titles.add(title)

                url = title_el.get_attribute("href")
                channel = channel_el.text.strip()
                channel_url = channel_el.get_attribute("href")
                thumbnail = thumb_el.get_attribute("src")

                video_data.append({
                    "Title": title,
                    "URL": url,
                    "Channel": channel,
                    "Channel URL": channel_url,
                    "Thumbnail": thumbnail,
                    "Duration": duration
                })
            except Exception as e:
                print(f"Ошибка при обработке одного из видео: {e}")
                continue

        print(f"Собрано видео: {len(video_data)}")

        if len(video_data) >= max_videos:
            break

    return video_data


def main():
    driver = setup_driver()
    driver.get("https://www.youtube.com/")

    # Даем время для того, чтобы браузер загрузил профиль и все cookies
    print("Пожалуйста, войдите в аккаунт, если это необходимо. Подождите немного...")
    time.sleep(10)  # Увеличь время, если страница загружается дольше

    video_data = scroll_and_collect(driver, max_videos=500)
    driver.quit()

    # Сохраняем данные в CSV (или передаем в другой файл для дальнейшего анализа)
    df = pd.DataFrame(video_data)
    df.to_csv("youtube_data.csv", index=False)  # Сохраняем в CSV


if __name__ == "__main__":
    main()
