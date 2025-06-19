import qrcode

# Take input from the user
name = input("Enter Name: ").strip()
age = input("Enter Age: ").strip()
gender = input("Enter Gender: ").strip()
phone = input("Enter Phone Number: ").strip()
email = input("Enter Email: ").strip()
idnumber = input("Enter the Idnumber: ").strip()
professionality = input("Enter the Professionality: ").strip()


# Combine the details into a single string
details = f"Name: {name}\nAge: {age}\nGender:{gender}\nPhone: {phone}\nEmail: {email}\nidnumber: {idnumber}\nprofessionality: {professionality}"

# Generate QR code
img = qrcode.make(details)

# Display QR code
img.show()

# Save QR code to a PNG file
img.save("generated.png")

print("QR code successfully generated and saved as 'generated.png'")