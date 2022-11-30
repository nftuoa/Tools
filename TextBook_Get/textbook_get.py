import requests

contentid = input("请输入教材ID")

url ="https://r2-ndr.ykt.cbern.com.cn/edu_product/esp/assets_document/" +contentid+ ".pkg/pdf.pdf"

header = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0"
        }

response = requests.get(url=url, headers=header)

with open(contentid+'.pdf','wb') as f:
    f.write(response.content)

print("下载成功！")
