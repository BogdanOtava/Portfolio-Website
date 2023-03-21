# Helper functions

def is_active(current_path:str, nav_path:str):
    """Returns a string that shows which page is active in the navigation menu."""

    if current_path == nav_path:
        return "is-active"
    
    return ""


def read_file(file_path:str):
    """Returns the content of a text file as a list of strings where each string is a paragraph."""

    content = []

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

    return content
