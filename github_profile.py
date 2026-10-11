import json
import sys
from pathlib import Path
from urllib.request import urlopen,Request

# 解决输出乱码问题
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8",errors="replace")


url="https://api.github.com/users/GYQ88"
request=Request(url, headers={"User-Agent": "stage-0-practice"})
with urlopen(request,timeout=10) as response:
    profile_data=json.load(response)


result=f"{profile_data['login']} 有 {profile_data['followers']} 位关注者"
print(result)
Path("result.txt").write_text(result + "\n", encoding="utf-8")