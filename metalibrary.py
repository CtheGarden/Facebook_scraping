# meta 광고 라이브러리 스크래핑 
# -> 실행 collector.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

# Chrome WebDriver 설정 필요
driver = webdriver.Chrome()

# Facebook 광고 라이브러리 URL
driver.get("https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=KR&q=%ED%86%A0%EC%8A%A4&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped&search_type=keyword_unordered&media_type=all")

# 사용자로부터 Enter 입력 대기
input("Press Enter to start scraping")

try:
    # 특정 요소가 로드될 때까지 최대 10초간 대기
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._7jyr')))

    # 모든 '_7jyr' 클래스를 가진 요소 찾기
    elements = driver.find_elements(By.CSS_SELECTOR, '._7jyr')

    # 각 요소의 텍스트를 추출하고 각각의 번호를 매김
    data = [{"number": str(index + 1), "content": element.text} for index, element in enumerate(elements)]

    # JSON 파일로 저장
    with open('metalibrary.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    
finally:
    # 브라우저 종료
    driver.quit()