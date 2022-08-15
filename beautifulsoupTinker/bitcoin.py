from tkinter import *
from PIL import Image, ImageTk
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re  
from datetime import datetime
import webbrowser

URL = "https://kr.investing.com/crypto/bitcoin/"
hdr = {'User-Agent': 'Mozilla/5.0'}

root = Tk()
root.title("비트코인 시세 조회")
root.geometry("500x200")
root.option_add("*Font", "맑은고딕 20")
root.config(bg="black")

# Frame 생성
my_frame = Frame(root)
my_frame.pack(pady=20)

#비트코인 logo 표시
img = ImageTk.PhotoImage(Image.open('images/bitcoin.png').resize((100, 100)))
logo_label = Label(my_frame, image=img)
logo_label.grid(row=0, column=0)

#비트코인 가격 표시
bit_label = Label(my_frame)
bit_label.grid(row=0, column=1)

status = Label(root)
status.pack()

def update():
    #비트코인 site 접속
    req = Request(URL, headers=hdr)
    page = urlopen(req)
    #웹페이지 파싱
    html = BeautifulSoup(page, "html.parser")
    found = html.find(class_="newInput inputTextBox alertValue")
    found = re.search("[0-9,.]+", str(found))
    price = found.group()
    #가격 표시
    bit_label.config(text=price)
    # 현재 시간 표시
    now = datetime.now()
    current_time = now.strftime("%I:%M:%S %p")
    status.config(text=f"최근 갱신 - {current_time}")
    
    #timer 를 5 초로 setting
    root.after(5000, update)
    
# program start 시 update 함수 수행 
update()

#website 직접 연결 button 생성
def callback():
    webbrowser.open_new(URL)
    
btn = Button(my_frame, text="웹사이트 바로가기")
btn.config(command=callback)
btn.grid(row=0, column=2)

root.mainloop()
