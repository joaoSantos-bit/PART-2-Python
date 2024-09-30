from license_plates_validator import validate

def main():
    fileName = "brasil_missing.cnf"
    plate = "GHV765"

    if (validate(fileName, plate)):
        print(f"The plate {plate} is valid!")
    else:  
        print(f"The plate {plate} is invalid!")

if __name__ == "__main__":
    main()