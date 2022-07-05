import os

fileNum = 0
for (dirpath, dirs, files) in os.walk(os.path.curdir):
    for file in files:
        if file.endswith(".html"):
            filePath = os.path.join(dirpath,file)
            with open(filePath,'r',encoding='utf-8') as f:
                s = f.read().replace("cdn.cookielaw.org/scripttemplates/otSDKStub.js",'').replace("www.googletagmanager.com",'').replace("fonts.googleapis.com",'')
            with open(filePath,'w',encoding='utf-8') as f:
                f.write(s)

            fileNum = fileNum + 1
            message = ">>>修改完成  进度：" + f'{round(fileNum / 25414 * 100, 2)}' + "%  文件: " + filePath
            print(message)
print("共修改",fileNum,"个文件")
