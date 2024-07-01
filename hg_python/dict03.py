# 딕셔너리를 선언합니다. 
dictionay = {
    "name": "7D 건조 망고",
    "type": "당절임"
}

# 요소 제거 전에 내용을 출력해 봅니다. 
print("요소 제거 이전:", dictionay)

# 딕셔너리의 요소를 제거합니다. 
del dictionay["name"]
del dictionay["type"]

# 요소 제거 후에 내용을 출력해 봅니다. 
print("요소 제거 이후:", dictionay)