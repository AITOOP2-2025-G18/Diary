from diaries.DiarySample import DiarySample
from diaries.NaoDiary import NaoDiary
from diaries.SuzukiDiary import SuzukiDiary
from diaries.AkiraaoDiary import AkiraaoDiary

#下のリストには、メンバーの各日記が格納されます
diaries = [
    DiarySample(),
    NaoDiary(),
    AkiraaoDiary(),
    SuzukiDiary(),
    ]

for d in diaries:
    print("----")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()