#Transformation templates for housing, metallic alloys, and electronics
housing = {
    "in": {"R1": 5, "R2": 1, "R3": 5, "R21": 3},
    "out": {"R23": 1, "R23'": 1, "R1": 5}
}

metallic_alloys = {
    "in": {"R1": 1, "R2": 2},
    "out": {"R1": 1, "R21": 1, "R21'": 1}
}

electronics = {
    "in": {"R1": 1, "R2": 3, "R21": 2},
    "out": {"R1": 1, "R22": 2, "R22'": 1}
}
