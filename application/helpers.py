# Helper functions

import json


def is_active(current_path:str, nav_path:str) -> str:
    """Returns a string that shows which page is active in the navigation menu."""

    if current_path == nav_path:
        return "is-active"
    
    return ""


def read_file(file_path:str) -> list:
    """Returns the content of a text file as a list of strings where each string is a paragraph."""

    content = []

    try:
        with open(file_path) as file:
            current_paragraph = ""

            # Loop over each line
            for line in file:
                # Check if the line is blank (i.e. contains only white spaces)
                if line.strip() == "":
                    # If so, add the current paragraph to the list and reset current paragraph
                    content.append(current_paragraph)
                    current_paragraph = ""
                # If line is not blank, add it to the current paragraph
                else:
                    current_paragraph += line

            # Add the final paragraph to the list
            if current_paragraph != "":
                content.append(current_paragraph)
    except FileNotFoundError:
        print(f"ERROR! File could not be found for path: {file_path}.")
        return None
    except Exception as error:
        print(f"ERROR! {error}.")
        return None

    return content


def get_skills(file_path:str) -> list:
    """Returns three lists one for each type of cards in the JSON file."""

    try:
        with open(file_path) as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"ERROR! File could not be found for path: {file_path}.")
        return None
    except json.JSONDecodeError as error:
        print(f"ERROR! {error}.")
    except Exception as error:
        print(f"ERROR! {error}.")

    # Storing the information based on the type of card
    languages = [card for card in data["cards"] if card["type"] == "language"]
    frameworks = [card for card in data["cards"] if card["type"] in ["library", "framework"]]
    technologies = [card for card in data["cards"] if card["type"] == "technology"]

    return languages, frameworks, technologies
