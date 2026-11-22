from pyscript import display, document

def create_order(event):
    prod1  =document.getElementById("item1")
    prod2  =document.getElementById("item2")
    prod3  =document.getElementById("item3")
    prod4  =document.getElementById("item4")
    prod5  =document.getElementById("item5")

    subtotal = (float(prod1.value) * prod1.checked) + (float(prod2.value) * prod2.checked) + (float(prod3.value) * prod3.checked)
    + (float(prod4.value) * prod4.checked) + (float(prod5.value) * prod5.checked)

    tax = float(subtotal * 0.15)
    total = float(tax + subtotal)

    display (f'Taxes: {tax}', target="show-tax")
    display (f'Subtotal: {subtotal}', target="show-subtotal")
    display (f'Total: {total}', target="show-total")

