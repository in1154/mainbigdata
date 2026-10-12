import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"

temp = [28,20,19,20,23]
day = ["10/12(월)","10/13(화)","10/14(수)","10/15(목)","10/16(금)"]

fig, ax = plt.subplots(figsize=(7,4))
ax.plot(day,temp)

for i, p in enumerate(temp):
    ax.annotate(f"{p:,}", (i, p), textcoords="offset points", xytext=(0, 8), ha="center")

ax.set_title("10월 세번째 주 춘천 날짜별 최고 기온")
fig.savefig("my_first_chart.png")