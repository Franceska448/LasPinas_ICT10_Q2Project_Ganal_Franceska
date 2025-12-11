from js import document

def calculate_gwa(*args, **kwargs):
    try:
        fname = document.getElementById("fname").value.strip()
        lname = document.getElementById("lname").value.strip()

        # Check names
        if not fname or not lname:
            document.getElementById("total").innerText = "Please enter your first and last name."
            document.getElementById("average").innerText = ""
            document.getElementById("status").innerText = ""
            return

        subjects = ["sci","math","eng","fil","ict","pe"]
        total = 0
        for sub in subjects:
            val_str = document.getElementById(sub).value
            if val_str == "":
                document.getElementById("total").innerText = "Please fill all grade fields."
                document.getElementById("average").innerText = ""
                document.getElementById("status").innerText = ""
                return
            val = float(val_str)
            if val < 0 or val > 100:
                document.getElementById("total").innerText = "Grades must be between 0 and 100."
                document.getElementById("average").innerText = ""
                document.getElementById("status").innerText = ""
                return
            total += val

        average = total / len(subjects)
        status = "PASSED" if average >= 75 else "FAILED"

        document.getElementById("total").innerText = f"{fname} {lname}'s Total: {total:.2f}"
        document.getElementById("average").innerText = f"Average: {average:.2f}"
        document.getElementById("status").innerText = f"Status: {status}"

    except Exception as e:
        document.getElementById("total").innerText = "Error: please enter valid numbers."
        document.getElementById("average").innerText = ""
        document.getElementById("status").innerText = ""

# Connect the button to the function
document.getElementById("calculate").addEventListener("click", calculate_gwa)
    