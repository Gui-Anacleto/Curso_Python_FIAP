users = {}
print(users)

users = {
    "gui":["Guilherme de Freitas Anacleto", "11/02/2022", "Terminal1"],
    "jose":["José Junio Bacili", "10/02/2021", "Terminal2"]
}

print(users)

users["Mariana"] = ["Mariana Alice Ribeiro", "11/02/2022", "Terminal3"]
print(users)

print("####-----####")
print(users.get("gui"))