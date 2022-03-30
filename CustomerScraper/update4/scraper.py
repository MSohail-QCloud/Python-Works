from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from sys import exit as sysExit 
from googlesearch import search
import re
from requests_html import HTMLSession


from PyQt5.QtWidgets import QApplication
from  PyQt5.QtCore import *
from  PyQt5.QtGui import *
from  PyQt5.QtWidgets import *
import os
import subprocess
from PyQt5.QtWidgets import QMessageBox
import threading


from PyQt5.QtWidgets import QMessageBox

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from time import sleep
from lxml import etree
from csv import DictWriter
from web_config import web_config
import uuid


queue_count=[]
webs=[]
queue=[]
count=0
status=False


all_jobs = []
class JobScraper:
    jobs_data = []
    def __init__(self, url, keyword, config, email=None, password=None):
        self.url = url
        self.config = config
        self.email = email
        self.password = password
        self.keyword = keyword

    def main(self):
        global all_jobs
        global webs
        global queue
        global count
        global status
        status=True
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            self.page = browser.new_page()
            #self.page.set_viewport_size({"width": 1920, "height": 1080})
            self.page.goto(self.url,timeout = 0)
            sleep(5)
            self._accept_cookies()
            if 'login' in self.config:
                self.login()
            self._search_job()

            self._close_noti()
            urls = self._parse_html()
            if urls:
                new_url=[]
                for u in range(len(urls)):
                    if 'javascript:;' in urls[u]:
                        pass
                    else:
                        new_url.append(urls[u])
                urls=new_url
                self._goto_job(urls)
                sleep(3)
                # print(self.jobs_data)
                # self.write_csv()
            count-=1
            print(urls)
            print('closing browser')
            browser.close()

    def create_csv_file(self):
        filename = self.config['name'] + '_' + str(uuid.uuid4()) + '.csv'
        self.filepath = f'./{filename}'
        with open(self.filepath, 'w') as f:
            headers = ['job_title', 'company_name', 'email', 'city', 'posted_by']
            csv_writer = DictWriter(f, fieldnames=headers)
            csv_writer.writeheader()

    def write_csv(self, data):
        with open(self.filepath, 'a') as f:
            headers = ['job_title', 'company_name', 'email', 'city', 'posted_by']
            csv_writer = DictWriter(f, fieldnames=headers)
            csv_writer.writerow(data)
        print(f'new data job to {self.filepath}')

    def _goto_job(self, urls):
        if urls:
            for url in urls:
                sleep(3)
                try:
                    if 'compare_url' in self.config:
                        self.page.goto(url)
                        self._read_job()
                    else:
                        if self.config['web_url'] in url:
                            self.page.goto(url)
                            self._read_job()
                        else:
                            if ("https" in url) or ("www." in url):
                                print("yes")
                                self.page.goto(url.replace("//","").replace("www.","https://").replace('https//', ''))
                                print(url.replace("//","").replace("www.","https://"))
                            else:
                                if 'base_url' in self.config:
                                    self.page.goto(self.config['base_url']+url)
                                    print(self.config['base_url']+url)
                                else:
                                    self.page.goto(self.url+url)
                                    print(self.url+url)
                            self._read_job()
                except Exception as e:
                    print(e)
                    print('timeout')
                    sleep(3)
                sleep(3)  
            # self.page.goto(self.url+urls[0])
            # self._read_job()
        return 'urls not found'

    def _read_job(self):
        global all_jobs
        global webs
        global queue
        global count
        global status
        sleep(3)
        print('read job')
        selector_job_title = self.config['job_page']['job_title']
        selector_company_name = self.config['job_page']['company_name']
        selector_email = self.config['job_page']['email']
        selector_city = self.config['job_page']['city']
        selector_posted_by = self.config['job_page']['posted_by']

        html = self.page.inner_html('html')
        # print(html)
        soup = BeautifulSoup(html, 'html.parser')
        soup2=etree.HTML(str(soup))
        try:
            job_title = soup.select_one(selector_job_title)
        except Exception as e:
            
            job_title=soup2.xpath(selector_job_title)[0]
        
        try:
            company_name = soup.select_one(selector_company_name)
        except:
            company_name = soup2.xpath(selector_company_name)[0]
        email = soup.select_one(selector_email)
        city = soup.select_one(selector_city)
        posted_by = soup.select_one(selector_posted_by)
       
        data = {
            'job_title': job_title,
            'company_name': company_name,
            'email': email,
            'posted_by': posted_by,
            'city': city
        }
        # print(data)
        for k,v in data.items():          
            if v is not None:
                value = v.text.replace('\n', ' ')
                value = ' '.join(value.split())
                # print(value)
                data[k] = value.replace(',', ' ')
            else:
                data[k] = 'None'
        # self.jobs_data.append(data)
        print(data)
        if data not in all_jobs:
            queue.append(data)
            
            all_jobs.append(data)

    def _close_noti(self):
        if 'noti' in self.config:
            print('close notifiation')
            selector_button = self.config['noti']['button']
            try:
                self.page.click(selector_button, delay=5.0)
            except:
                print('no noti')
    def login(self):
        print('login to the account')
        email_field = self.config['login']['email_field']
        password_filed = self.config['login']['password_field']
        login_button = self.config['login']['login_button']

        print('entering email')
        self.page.fill(email_field, self.email)
        print('entering password')
        self.page.fill(password_filed, self.password)
        self.page.click(login_button)
        sleep(5)

    def _search_job(self):
        print('search for job')
        job_title = self.keyword
        print(self.config['search_page'])
        try:
            if self.config['search_page']['url_search']==True:
                job_title2=self.keyword.replace(" ","+")
                self.page.goto(self.url+"/jobs/suche?q="+job_title2+"&where=")
                return
        except:
            pass
        selector_input = self.config['search_page']['input_field']
        selector_job = ''
        if 'select_job' in self.config['search_page']:
            selector_job = self.config['search_page']['select_job']
       
        if 'search_button' in self.config['search_page']:
            selector_button = self.config['search_page']['search_button']
        
        if 'goto_job' in self.config['search_page']:
            print('click on job')
            self.page.goto(self.config['search_page']['goto_job'])
            self.page.wait_for_load_state()
        
        sleep(5)
        print('inputing jobtitle')
        self.page.fill(selector_input, job_title)
        sleep(3)
        if 'press_enter' in self.config['search_page']:
            print('press enter')
            self.page.keyboard.press('Enter')
        else:
            self.page.click(selector_button)
        if selector_job:
            print('click job')
            sleep(5)
            self.page.click(selector_job, delay=5)
        sleep(5)

    def _accept_cookies(self):
        print(self.config['name'])
        if self.config['name']=='arbeitsagentur':
            self.page.keyboard.press('Enter')
        if self.config['name']=='karriere':
            self.page.click('body',delay=3)
            sleep(3)
            self.page.keyboard.press('Tab')
            sleep(1)
            self.page.keyboard.press('Tab')
            self.page.keyboard.press('Enter')
            return
        if 'accept_cookies' in self.config:
            print('acceept cookies')
            selector_input = self.config['accept_cookies']['accept']
            try:
                self.page.click(selector_input, delay=1)
                return
            except:
                print('no cookies')
                return
            try:
                self.page.keyboard.press('Tab')
                sleep(4)
                self.page.keyboard.press('Enter')
                #sleep(4)
            except Exception as e:
                print(e)
                print("no cookies")
    def click_on_more2(self, button):
        selector_results = self.config['result_page']['results_container']
        selector_links = self.config['result_page']['links']
        
        print('parsing jobs links')
        urls = []
        self.page.wait_for_load_state()
        is_buttion_exist = self.page.query_selector(button)
        print('clicking on more button')
        cc=self.config['next_page_button_1']['max_clicks']
        while cc!=0:
            try:
                self.page.click(button)
                self.page.wait_for_load_state()
                html = self.page.inner_html(selector_results)
                soup = BeautifulSoup(html, 'html.parser')
                pre_html = ''
                
                
                d = soup.select(selector_links)
                for el in d:
                    try:
                        if not el.attrs['href'] == 'javascript:void(0)':
                            href=el.attrs['href']
                            urls.append(href)
                    except:
                        print('href not found')               
                cc-=1
                print(urls)
            except Exception as e:
                print(e)
                break
            sleep(5)
            is_buttion_exist = self.page.query_selector(button)
        if urls:
            print(len(urls), 'jobs found')
            print(urls)
        else:
            print('no jobs found')
        return urls

    def click_on_more(self, button):
        urls=[]
        selector_results = self.config['result_page']['results_container']
        selector_links = self.config['result_page']['links']
        is_buttion_exist = self.page.query_selector(button)
        print('clicking on more button')
        cc=self.config['next_page_button']['max_clicks']
        for i in range(0,100):
            self.page.keyboard.press("ArrowDown")
        while cc!=0:
            try:
                self.page.click(button)
                self.page.wait_for_load_state()
                
                
                
                
                cc-=1
            except Exception as e:
                print(e)
                break
            sleep(5)
            is_buttion_exist = self.page.query_selector(button)
    def scroll(self):
        self.page.evaluate(
            """
            var intervalID = setInterval(function () {
                var scrollingElement = (document.scrollingElement || document.body);
                scrollingElement.scrollTop = scrollingElement.scrollHeight;
            }, 200);

            """
        )
        prev_height = None
        while True:
            curr_height = self.page.evaluate('(window.innerHeight + window.scrollY)')
            if not prev_height:
                prev_height = curr_height
                sleep(1)
            elif prev_height == curr_height:
                self.page.evaluate('clearInterval(intervalID)')
                break
            else:
                prev_height = curr_height
                sleep(1)
    
    def _parse_html(self):
        selector_results = self.config['result_page']['results_container']
        selector_links = self.config['result_page']['links']
        
        print('parsing jobs links')
        urls = []
        self.page.wait_for_load_state()
        sleep(10)
        if 'next_page_button_1' in self.config:
            if 'scroll' in self.config:
                px = 0
                click = 0
                self.page.keyboard.press("PageDown")
                while px < 100:
                    self.page.click(self.config['scroll']['scroll_container'])
                    self.page.keyboard.press("ArrowDown")
                    print('scroling')
                    px+=1
                if True:
                    sleep(3)
                    button = self.config['next_page_button']['next_button']
                    self.click_on_more(button)
                    click+=1

            else:
                print('press more button')
                button = self.config['next_page_button_1']['next_button']
                urls=self.click_on_more2(button)
                return urls
        if 'next_page_button' in self.config:
            if 'scroll' in self.config:
                px = 0
                click = 0
                self.page.keyboard.press("PageDown")
                while px < 200:
                    self.page.click(self.config['scroll']['scroll_container'])
                    self.page.keyboard.press("ArrowDown")
                    print('scroling')
                    px+=1
                if True:
                    sleep(3)
                    button = self.config['next_page_button']['next_button']
                    self.click_on_more(button)
                    click+=1

            else:
                print('press more button')
                button = self.config['next_page_button']['next_button']
                urls=self.click_on_more(button)
                return urls
        
        
                       
        if 'next_page_url' in self.config:
            page_num = 25
            print('here')
            while True:
                sleep(5)
                self.page.wait_for_load_state()
                html = self.page.inner_html(selector_results)
                soup = BeautifulSoup(html, 'html.parser')
                d = soup.select(selector_links)
                if not d:
                    break
                i = 0
                while i < len(d):
                    try: 
                        href=d[i].attrs['href']
                        if href in urls:
                            break
                        urls.append(href)
                    except:
                        print('href not found')
                    i+=1
                sleep(2)       
                next_url = f"{self.config['next_page_url']}+{self.keyword}&start={page_num}"
                self.page.goto(next_url)
                self.page.wait_for_load_state()
                page_num+=25
       
        self.page.wait_for_load_state()
        html = self.page.inner_html(selector_results)
        soup = BeautifulSoup(html, 'html.parser')
        pre_html = ''
        if 'next_page' in self.config['result_page']:
            selector_next_page = self.config['result_page']['next_page']
            next_page = soup.select(selector_next_page)
            print(next_page)
            next_count=0
            while True:
                if not next_page:
                    break
                next_count+=1
                if next_count==20:
                    break
                sleep(5)
                html = self.page.inner_html(selector_results)
                soup = BeautifulSoup(html, 'html.parser')           
                next_page = soup.select(selector_next_page)
                print('extracing links')
                d = soup.select(selector_links)
                for el in d:
                    try:
                        href=el.attrs['href']
                        urls.append(href)
                    except:
                        print('href not found')
                print('click on next button')
                sleep(1)
                try:
                    if not self.page.is_disabled(selector_next_page):
                        print('clicking on next page')
                        self.page.click(selector_next_page)
                        sleep(2)
                        if html == pre_html:
                            break
                    else:
                        break
                except Exception as e:
                    print(e)
                    break
                pre_html = html
        else:
            print('i am running')
            # print(selector_links)
            d = soup.select(selector_links)
            for el in d:
                try:
                    if not el.attrs['href'] == 'javascript:void(0)':
                        href=el.attrs['href']
                        urls.append(href)
                except:
                    print('href not found')
        if urls:
            print(len(urls), 'jobs found')
            print(urls)
        else:
            print('no jobs found')
        return urls


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(725, 476)
        MainWindow.setStyleSheet("background-color: rgb(15, 15, 15);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_2.setStyleSheet("background-color: rgb(49, 49, 49);\n"
" border-radius: 10px;\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label.setStyleSheet("QLabel {\n"
"    \n"
"    \n"
"background-color: rgb(35, 35, 35);\n"
"  \n"
"    color: rgb(255, 255, 255);\n"
"    border-style: outset;\n"
"    padding: 1px;\n"
"    font: bold 20px;\n"
"    border-width: 1px;\n"
"    border-radius: 0px;\n"
"    border-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("background-color: rgb(49, 49, 49);\n"
" border-radius: 10px;\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_5)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 634, 392))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.checkBox_9 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_9.setObjectName("checkBox_9")
        self.verticalLayout_6.addWidget(self.checkBox_9)
        self.checkBox_15 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_15.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_15.setObjectName("checkBox_15")
        self.verticalLayout_6.addWidget(self.checkBox_15)
        self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_6.addWidget(self.checkBox)
        self.checkBox_10 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_10.setObjectName("checkBox_10")
        self.verticalLayout_6.addWidget(self.checkBox_10)
        self.checkBox_8 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_8.setObjectName("checkBox_8")
        self.verticalLayout_6.addWidget(self.checkBox_8)
        self.checkBox_16 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_16.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_16.setObjectName("checkBox_16")
        self.verticalLayout_6.addWidget(self.checkBox_16)
     
        self.checkBox_7 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout_6.addWidget(self.checkBox_7)
        self.checkBox_20 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_20.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_20.setObjectName("checkBox_20")
        self.verticalLayout_6.addWidget(self.checkBox_20)
        self.checkBox_6 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_6.addWidget(self.checkBox_6)
        self.checkBox_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_6.addWidget(self.checkBox_2)
        
        self.checkBox_12 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_12.setObjectName("checkBox_12")
        self.verticalLayout_6.addWidget(self.checkBox_12)
        
        self.checkBox_18 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_18.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_18.setObjectName("checkBox_18")
        self.verticalLayout_6.addWidget(self.checkBox_18)
        
        self.checkBox_4 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_6.addWidget(self.checkBox_4)
        self.checkBox_13 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_13.setObjectName("checkBox_13")
        self.verticalLayout_6.addWidget(self.checkBox_13)
        self.checkBox_19 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_19.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_19.setObjectName("checkBox_19")
        self.verticalLayout_6.addWidget(self.checkBox_19)
       
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_5.addWidget(self.scrollArea)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_7.setStyleSheet("background-color: rgb(49, 49, 49);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(49, 49, 49);\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit.setMinimumSize(QtCore.QSize(100, 30))
        self.lineEdit.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(74, 74, 74);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit.setMaxLength(1)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        self.label_4.setMinimumSize(QtCore.QSize(100, 0))
        self.label_4.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(49, 49, 49);\n"
"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(200, 30))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(74, 74, 74);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setMaxLength(1000)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.verticalLayout_4.addWidget(self.frame_7, 0, QtCore.Qt.AlignHCenter)
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4.addWidget(self.frame_6, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_4.setStyleSheet("background-color: rgb(49, 49, 49);\n"
" border-radius: 10px;\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 30))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.528, x2:1, y2:0.687409, stop:0 rgba(243, 215, 2, 255), stop:1 rgba(230, 179, 17, 255));\n"
"  \n"
"    color: rgb(57, 57, 57);\n"
"    border-style: outset;\n"
"    padding: 1px;\n"
"    font: bold 16px;\n"
"    border-width: 0px;\n"
"    border-radius: 3px;\n"
"    border-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setMinimumSize(QtCore.QSize(100, 0))
        self.label_3.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(49, 49, 49);\n"
"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout_2.addWidget(self.frame_4, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Website Scrapper"))
        self.checkBox_9.setText(_translate("MainWindow", "Arbeitsagentur für Arbeit:"))
        self.checkBox_15.setText(_translate("MainWindow", "Indeed:"))
        self.checkBox.setText(_translate("MainWindow", "Monster:"))
        self.checkBox_10.setText(_translate("MainWindow", "Stepstone:"))
        self.checkBox_8.setText(_translate("MainWindow", "LinkedIn:"))
        self.checkBox_16.setText(_translate("MainWindow", "Xing:"))
        
        self.checkBox_7.setText(_translate("MainWindow", "eBay Kleinanzeigen:"))
        self.checkBox_20.setText(_translate("MainWindow", "Bundesanzeiger:"))
        self.checkBox_6.setText(_translate("MainWindow", "Jobs.de:"))
        self.checkBox_2.setText(_translate("MainWindow", "Joblift:"))
        
        self.checkBox_12.setText(_translate("MainWindow", "meineStadt:"))

        self.checkBox_18.setText(_translate("MainWindow", "Jobfinder:"))
        
        self.checkBox_4.setText(_translate("MainWindow", "Kimeta:"))
        self.checkBox_13.setText(_translate("MainWindow", "Jobware:"))
        self.checkBox_19.setText(_translate("MainWindow", "Valmedi:"))
        
        self.label_2.setText(_translate("MainWindow", "Thread"))
        self.label_4.setText(_translate("MainWindow", "Keyword"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.label_3.setText(_translate("MainWindow", "%"))






class MainWindow(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.setWindowTitle('Scraper')
        
        self.ui.setupUi(self)
  
               
        #self.timer = QtCore.QTimer(self)
        #self.timer.timeout.connect(self.manage_queue)
        #self.timer.start(2000)
        
        self.ui.pushButton.clicked.connect(self.start)
       
        
        self.show()
    def create_csv_file(self):
        filename = 'DATA SCRAPED.csv'
        #self.filepath = f'./{filename}'
        with open(filename, 'w',encoding='utf-8') as f:
            headers = ['job_title', 'company_name', 'email', 'city', 'posted_by']
            csv_writer = DictWriter(f, fieldnames=headers)
            csv_writer.writeheader()
            f.close()

    def write_csv(self, data):
        strr=""
        filename = 'DATA SCRAPED.csv'
        with open(filename, 'a',encoding='utf-8') as f:
            headers = ['job_title', 'company_name', 'email', 'city', 'posted_by']
            csv_writer = DictWriter(f, fieldnames=headers)
            if data['job_title']!="None":
                print("writing data")
                print(data)
                if data["email"]=="None":
                    query = data["company_name"]+" email"
                    print(query)
                    links = []
                    for j in search(query): 
                        links.append(j) 

                    EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
                    session = HTMLSession()
                    email_count=0
                    for url in links:
                        if email_count==6:
                            break
                        r = session.get(url)

                        for re_match in re.finditer(EMAIL_REGEX, r.text):
                            #print(re_match.group())
                            strr+=re_match.group()+"\n"
                        email_count+=1
                    data["email"]=strr
                    print("email donee")
                try:
                    csv_writer.writerow(data)
                except Exception as e:
                    print(e)
                print("row writted")
                f.close()
        print(f'new data job to {filename}')
    def manage_queue(self):
        global webs
        global queue
        global count
        global status
        global queue_count
        print("queue started")
        
        while True:
            
            if status==True:
                if True:
                    try:
                        data=queue[0]
                        queue_count.append(0)
                        queue.pop(0)
                        self.write_csv(data)
                        #print(data)
                        #queue_count.pop(0)
                    except Exception as e:
                        #print(e)
                        pass
                    
            if status==False:
                break
            
    def start_system(self):
        global webs
        global queue
        global count
        global status
        
        thread=int(self.ui.lineEdit.text())
        self.create_csv_file()
        i_count=0
        print(thread)
        print(len(webs))
        for i in webs:
            
            
            while count>= thread:
                
                pass
            s3=threading.Thread(target=i.main)
            try:
                s3.start()
            except Exception as e:
                print(e)
                count-=1
                pass
            count+=1
            print(count)
            if i_count==0:
                #print('queuerun')
                status=True
                s2=threading.Thread(target=self.manage_queue)
                s2.start()
            i_count+=1
            per=(i_count//len(webs))*100
            self.ui.label_3.setText(str(per)+"%")
            print("update")
        while True:
            if count>0:
                pass
            else:
                status=False
                break
        
        
        
        
    def start(self):
        global webs
        global queue
        global count
        global status
        
        file=open("settings.txt",'r')
        lines=file.readlines()
        for i in range(0,len(lines)):
            lines[i]=lines[i].replace("\n","")
        emaill=lines[0]
        passwordd=lines[1]
        keywordd=self.ui.lineEdit_2.text()
        
        if self.ui.checkBox_9.isChecked()==True:
            obj=scraper = JobScraper(url=web_config['arbeitsagentur']['web_url'],keyword=keywordd,
                                     config=web_config['arbeitsagentur'], email=emaill, password=passwordd)
            webs.append(obj)
        if self.ui.checkBox_15.isChecked()==True:
            obj=scraper = JobScraper(url=web_config['job_indeed']['web_url'],keyword=keywordd,
                                     config=web_config['job_indeed'], email=emaill, password=passwordd)
            webs.append(obj)
        if self.ui.checkBox.isChecked()==True:
            obj=scraper = JobScraper(url=web_config['monster']['web_url'],keyword=keywordd,
                                     config=web_config['monster'], email=emaill, password=passwordd)
            webs.append(obj)
        if self.ui.checkBox_10.isChecked()==True:
            obj=scraper = JobScraper(url=web_config['stone_steps']['web_url'],keyword=keywordd,
                                     config=web_config['stone_steps'], email=emaill, password=passwordd)
            webs.append(obj)
        if self.ui.checkBox_8.isChecked()==True:
            obj=scraper = JobScraper(url=web_config['linkdin']['web_url'],keyword=keywordd,
                                     config=web_config['linkdin'], email=emaill, password=passwordd)
            webs.append(obj)
        if self.ui.checkBox_16.isChecked()==True:
            obj=scraper = JobScraper(url=web_config['xing']['web_url'],keyword=keywordd,
                                     config=web_config['xing'], email=emaill, password=passwordd)
            webs.append(obj)
        if self.ui.checkBox_7.isChecked()==True:
            obj=scraper = JobScraper(url=web_config['ebay']['web_url'],keyword=keywordd,
                                     config=web_config['ebay'], email=emaill, password=passwordd)
            webs.append(obj)
        if self.ui.checkBox_20.isChecked()==True:
            obj=scraper = JobScraper(url=web_config['bundesanzeiger']['web_url'],keyword=keywordd,
                                     config=web_config['bundesanzeiger'], email=emaill, password=passwordd)
            webs.append(obj)
        if self.ui.checkBox_6.isChecked()==True:
            obj=scraper = JobScraper(url=web_config['jobs']['web_url'],keyword=keywordd,
                                     config=web_config['jobs'], email=emaill, password=passwordd)
            webs.append(obj)
        if self.ui.checkBox_2.isChecked()==True:
            obj=scraper = JobScraper(url=web_config['joblift']['web_url'],keyword=keywordd,
                                     config=web_config['joblift'], email=emaill, password=passwordd)
            webs.append(obj)
            
        if self.ui.checkBox_12.isChecked()==True:
            obj=scraper = JobScraper(url=web_config['stadi']['web_url'],keyword=keywordd,
                                     config=web_config['stadi'], email=emaill, password=passwordd)
            webs.append(obj)
        
        if self.ui.checkBox_18.isChecked()==True:
            obj=scraper = JobScraper(url=web_config['jobfinder']['web_url'],keyword=keywordd,
                                     config=web_config['jobfinder'], email=emaill, password=passwordd)
            webs.append(obj)
        
        if self.ui.checkBox_4.isChecked()==True:
            obj=scraper = JobScraper(url=web_config['kimeta']['web_url'],keyword=keywordd,
                                     config=web_config['kimeta'], email=emaill, password=passwordd)
            webs.append(obj)
        if self.ui.checkBox_13.isChecked()==True:
            obj=scraper = JobScraper(url=web_config['job_ware']['web_url'],keyword=keywordd,
                                     config=web_config['job_ware'], email=emaill, password=passwordd)
            webs.append(obj)
        if self.ui.checkBox_19.isChecked()==True:
            obj=scraper = JobScraper(url=web_config['valmedi']['web_url'],keyword=keywordd,
                                     config=web_config['valmedi'], email=emaill, password=passwordd)
            webs.append(obj)
        
        s=threading.Thread(target=self.start_system)
        s.start()
        
        
 



       
        
        
    
        
    
     
        
from sys import exit as sysExit       
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec_()
    breakk=True
    #sysExit(app.exec_())

