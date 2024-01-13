init python:
    def get_probability_color(probability: int) -> str:
        if probability < 50:
            return "#fd0101"
        elif probability < 75:
            return "#fda101"
        else:
            return "#01fd01"