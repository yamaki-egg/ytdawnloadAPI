from yt_dlp import YoutubeDL
from tkinter import filedialog
import tkinter as tk
import os
from tkinter import messagebox
import threading
import Settings
#ラベルとエントリー
class LabelEntry(tk.Frame):
    def __init__(self,master,label_text:str):
        super().__init__(master)
        self.label=tk.Label(self,text=label_text)
        self.label.pack(side=tk.LEFT)

        self.entry=tk.Entry(self)
        self.entry.pack(side=tk.LEFT,expand=True,fill=tk.X)
    #エントリーの文字列を習得
    def extract_text(self)->str:
        if(self.entry.get()!=None):
            return self.entry.get()

class MainFrame(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.url_label=LabelEntry(self,"URL")
        self.url_label.pack(side=tk.TOP,fill=tk.BOTH,expand=True)

        self.storage_label=LabelEntry(self,"保存先")
        self.storage_label.pack()
        self.download_button=tk.Button(self,text="ダウンロード",command=self.Dawnload_Clicked)
        self.download_button.pack(side=tk.RIGHT)
        
        self.storage_button=tk.Button(self,text="保存先を選択",command=self.Storege_Clicked)
        self.storage_button.pack()

        self.json=Settings.Storage()
        self.yt_dlp=Yt_Download(self.json)
        
    def Dawnload_Clicked(self):
        self.yt_dlp.url=self.url_label.extract_text()
        #YoutubeDLはasnycioに対応してないためthreadingで非同期処理
        thread=threading.Thread(target=self.yt_dlp.download)
        thread.start()
        self.url_label.entry.delete(0,tk.END)
    def Storege_Clicked(self):
        self.foler_path=filedialog.askdirectory()
        setting_dict=self.json.Change_Storage(self.foler_path)
        self.yt_dlp.option["outtmpl"]=setting_dict["outtmpl"]

class Yt_Download:
    def __init__(self,Settings:Settings.Storage):
        self.url=""
        self.option={
        "format":"best",
        "outtmpl":""}
        setting_dict=Settings.ReadJson()
        self.option["outtmpl"]=setting_dict["outtmpl"]
    #option 一覧 https://masayoshi-9a7ee.hatenablog.com/entry/2021/11/06/112639
    def download(self):
        with YoutubeDL(self.option) as yd:
            yd.download(self.url)
        messagebox.showinfo("Success","成功")
    


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("yt-download")

        self.main_frame=MainFrame(self)
        self.main_frame.pack(expand=True,fill=tk.BOTH)

def main():
    app=App()
    #window サイズ
    app.geometry("300x300")
    app.mainloop()

if __name__=="__main__":
    main()


#TODO:クラスの分離

