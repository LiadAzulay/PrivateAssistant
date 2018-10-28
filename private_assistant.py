"""private_assistant"""

import wx
import wolframalpha
import wikipedia
import os
import speech_recognition as sr

"""GUI"""
class m_frame(wx.Frame):
    def __init__(self):
        os.system("espeak 'hello sir'")
        wx.Frame.__init__(self,None,pos=wx.DefaultPosition,size=wx.Size(450, 125), style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU |
                                                                                         wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN,
                          title="Private Assistant")
        panel = wx.Panel(self)
        m_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,label="Hello I am your private assistant. how can i help you?\n")
        m_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER,self.OnEnter)
        m_sizer.Add(self.txt,0,wx.ALL,5)
        panel.SetSizer(m_sizer)
        self.Show()

    def on_enter(self):
        input = self.txt.GetValue()
        input = input.lower()

        if input == "":
            r = sr.Recognizer()
            with sr.MicroPhone() as source:
                audio = r.listen(source)
            try:
                self.txt.SetValue(r.recognize_google(audio))
            except sr.UnknownValueError:
                print("Google Speech Recognize could not understand audio")
            except sr.RequestError as e:
                print("could not request results from Google Speech Recognize service; {0}".format(e))
        else:
            try:
                app_id = "94692X-YLJV2TY333"
                client = wolframalpha.Client(app_id)
                res = client.query(input)
                answer = next(res.results).text
                os.system("espeak 'the answer is {} sir'".format(answer))

            except:
                input = input.split(' ')
                input = " ".join(input[2:])
                os.system("espeak 'the answer is'")
                print(wikipedia.summary(input))


if __name__ == "__main__":
    app = wx.App(True)
    frame = m_frame()
    app.MainLoop()
