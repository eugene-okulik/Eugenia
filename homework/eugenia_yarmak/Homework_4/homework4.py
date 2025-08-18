my_dict = {
    "tuple": (1, 2, 3, 4, 5),
    "list": ["red", "blue", "pink", "white", "orange"],
    "dict": {"mango": 1, "banana": 2, "apple": 3, "peach": 4, "melon": 5},
    "set": {10, 20, 30, 40, 50}
}

print(my_dict["tuple"][-1])

my_dict["list"].append("green")
my_dict["list"].pop(1)

my_dict["dict"][('i am a tuple',)] = "test"
my_dict["dict"].pop("banana")

my_dict["set"].add(60)
my_dict["set"].remove(20)

print("Final result: ", my_dict)