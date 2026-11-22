from pyscript import document, display

members = [
    "Adriana Averilla", "Ciara De Guzman", "Rachel Balasico", "Rafael Roncal",
    "Dustin Cunanan", "Ian Salangsang"
]

def check (event):
    first = document.getElementById("firstname").value
    last = document.getElementById("lastname").value

    fullname = first + last

    check = fullname in members
