from pyscript import document,display

students = ['Ram Betilez', 'Ram Amortizado', 'Ram Magtanggol', 'Ram Correa', 'Ram Evangelista', 'Ram Maniago', 'Ram Caagbay', 'Ram Alip', 'Ram Agacita', 'Ram Lao', 'Ram Buntile', 'Ram Ramos', 'Ram Concengco', 'Ram Chua', 'Ram Coronel', 'Ram Pagud', 'Ram Pagsanhan', 'Ram Montefalco', 'Ram Mondragon', 'Ram Canedo', 'Ram Catu']


def verify(e):
    document.getElementById("result").innerHTML = ""

    first_name = document.getElementById("firstname").value.strip()
    last_name = document.getElementById("lastname").value.strip()
    full_name = f"{first_name.title()} {last_name.title()}"
    is_empty = first_name == "" or last_name == ""
    is_member = full_name in students

    messages = [
        f"Your name is not on the list, please double-check if you are on the right university and campus. Thank you!",
        f"Greetings, {full_name}! We welcome you in this university!"]
    empty_messages = [
        messages[is_member],
        "Please enter both your first and last name."]

    result_message = empty_messages[is_empty]
    display(result_message, target="result")
