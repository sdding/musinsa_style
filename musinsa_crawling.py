'''
12개 스타일 
아메리칸 캐주얼, 캐주얼, 시크, 댄디,
포멀, 걸리시, 골프, 레트로,
로맨틱, 스포츠, 스트릿, 뷰티
''' 

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os
import urllib.request

driver = webdriver.Chrome('chromedriver')

# 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
driver.implicitly_wait(3)

# url 에 접근한다.
driver.get('https://www.musinsa.com/app/styles/lists')

# style/lists 페이지 이동 후 , 조회순으로 정렬된 페이지로 이동
tab = driver.find_element(By.CLASS_NAME, "sorter-box")
tab.find_element(By.LINK_TEXT, '조회순').click()
driver.implicitly_wait(1.5)


# 카테고리 별 번호 매기기 위해서  dictionary 자료구조 생성
# 기존 구조에 directory가 존재하면 , dictionary 자료구조 만들어놔야함
# dict={}

"""
@param
URL              :   pagaination 체크 용도 
Category         :   이미지 총 개수 저장
"""

def downloadURLImage(URL, Category):

    # 폴더 상대경로, 저장경로
    dir_path = "/Users/User/Desktop/무신사 추천/"+Category

    # 폴더가 존재 할경우
    if(os.path.isdir(dir_path)):
        img_file_path = dir_path + "/"+Category+"_" + str(len(os.listdir(dir_path))+1) + ".jpg"
        urllib.request.urlretrieve(URL,img_file_path)

    # Category 폴더가 존재 안할경우, 폴더 만들고 안에 저장
    else:
        # dict[Category]=str(len(dict.keys())+1)
        os.mkdir(dir_path)
        img_file_path = dir_path + "/"+Category+"_" + str(len(os.listdir(dir_path))+1) + ".jpg"
        urllib.request.urlretrieve(URL,img_file_path)

"""
While 문
@param 
j               :   pagaination 체크 용도 
image_count     :   이미지 총 개수 저장
want_image_num  :   조회수 순으로 뽑아올 이미지 총 개수 
"""
image_count = 0
want_image_num = 23088
if want_image_num==0:
    exit()

# 이미지 와 Category 분류 진행해보기
print("이미지 크롤링 및 다운로드 진행중 ...")
while True:
    # 총 저장 이미지 개수 저장
    # 한페이지 내에서 카테고리 분류되어있는 이미지 가져오기
    list = driver.find_elements(By.CLASS_NAME, "style-list-item")
    for i in list:
        category = i.find_element(By.CLASS_NAME,"style-list-information").find_element(By.CLASS_NAME,"style-list-information__text")
        if category.text != "":
            #  img 경로 찾기
            img = i.find_element(By.CLASS_NAME,"style-list-thumbnail").find_element(By.TAG_NAME,"img")
            url = img.get_attribute('src')

            # 파일 카테고리에 따라 폴더 만들고 이미지 저장
            # 폴더가 없다면
            downloadURLImage(url,category.text)

            # 이미지 저장후 저장 수 만큼 +1
            image_count+=1

            # print(category.text," : " ,url)
            # print("\n")
            # 저장된 이미지가 원하는 장수넘었는지 확인
            if image_count>=want_image_num:
                print("이미지 원하는 장수 만큼 이미지 저장완료")
                exit()
        else:
            print("...")
    # 총 저장한 이미지가 지정한 장수 이상이면 break;

    # 한페이지 다 읽어 들였으면, 그 다음 페이지로 이동하는 코드 필요
    try:
        page = driver.find_element(By.CLASS_NAME, "pagination").find_element(By.CLASS_NAME, "active")
        page_link = driver.find_element(By.CLASS_NAME, "pagination").find_element(By.LINK_TEXT, str(int(page.text) + 1))
        driver.execute_script("arguments[0].click();", page_link)
    except NoSuchElementException:
        page_link= driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/form/div[4]/div/div[1]/div/div/a[13]")
        driver.execute_script("arguments[0].click();", page_link)
