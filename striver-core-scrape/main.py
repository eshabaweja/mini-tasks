import requests
from bs4 import BeautifulSoup

URL = "https://takeuforward.org/interviews/must-do-questions-for-dbms-cn-os-interviews-sde-core-sheet/"
page = requests.get(URL)

# print(page.text)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all("details")

# print(results)
f = open("core_interviews.md",'a')
# ques_dict = {}

for details in results:
    all_text = list(filter(None,details.text.split("\n")))
    
    ques = f"<b>{all_text[0]}</b>"
    ans = all_text[1:]
   # ques_dict[ques] = ans
    f.write(f"\n{ques}")
    f.write(''.join([f"- {a}\n" for a in ans]))
    f.write("\n")

# print(ques_dict)
f.close()
