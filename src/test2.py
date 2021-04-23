import win32com.client

app=win32com.client.Dispatch('Word.Application')

doc=app.Documents.Open(r'‪C:\Users\14580\Desktop\douban.docx')
doc.Content.Copy()
doc.Close()






