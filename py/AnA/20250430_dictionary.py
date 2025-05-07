items = {
    "사과": {
        "type": "과일",
        "description": "달콤하고 아삭한 과일입니다.",
        "price": 2000
    },
    "복숭아": {
        "type": "과일",
        "description": "달콤하고 아삭한 과일입니다.",
        "price": 6000
    },
    "샤인머스켓": {
        "type": "과일",
        "description": "달콤하고 달콤합니다.",
        "price": 8000
    },
    "블루베리": {
        "type": "과일",
        "description": "달콤하고 새콤하고 달콤새콤하고 그렇습니다.",
        "price": 4000
    }
}

for k in items.keys():
    item = items[k]
    print(f"{k}({item["type"]}): {item["price"]}원")
    print(f"ㄴ {item["description"]}")
    print()
