#Original written by @Maredevi,modified by @nftuoa
import requests
import tkinter as tk
from tkinter import messagebox

mainwindow=tk.Tk()
var = tk.StringVar()
IDentry=tk.Entry(mainwindow,textvariable=var).pack()
def download():
    contentid = var.get()

    url ="https://r2-ndr.ykt.cbern.com.cn/edu_product/esp/assets_document/" +contentid+ ".pkg/pdf.pdf"

    header = {
            'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0"
            }

    response = requests.get(url=url, headers=header)

    with open(contentid+'.pdf','wb') as f:
        f.write(response.content)
    messagebox.showinfo("提示","下载成功")
    
    
downloadbutton=tk.Button(mainwindow,text="下载",command=download).pack()
mainwindow.mainloop()
