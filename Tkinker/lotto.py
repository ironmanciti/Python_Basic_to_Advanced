from tkinter import *
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

URL = "https://dhlottery.co.kr/gameResult.do?method=byWin"
hdr = {'User-Agent': 'Mozilla/5.0'}

root = Tk()
root.title('로또 당첨번호')
root.geometry("1000x300")  # window size
root.option_add("*Font", "맑은고딕 20")
root.config(bg="black")  # 배경색 설정

def lotto():
    req = Request(URL, headers=hdr)
    page = urlopen(req)
    html = BeautifulSoup(page, "html.parser")
    txt = html.find("div", attrs={"class": "win_result"}).get_text()
    txt = txt.split('\n')
    lotto_label = Label(root)
    lotto_label.config(text="당첨번호 {}, 보너스 {}".format(txt[7:13], txt[-4]))
    # lotto_label.grid(row=1, column=1)
    lotto_label.pack()

btn = Button(root, text="로또 당첨번호 확인", command=lotto)
# btn.grid(row=0, column=0)
btn.pack()

root.mainloop()
