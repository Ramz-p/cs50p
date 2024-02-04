# extensions.py

def main():
    # Prompt the user for the name of a file
    file_name = input("Enter the name of a file: ")

    # Strip leading and trailing spaces from the file name
    file_name_stripped = file_name.strip()

    # Convert the file name to lowercase for case-insensitive comparison
    file_name_lower = file_name_stripped.lower()

    # Determine the media type based on the file extension
    media_type = determine_media_type(file_name_lower)

    # Output the result
    print(media_type)

def determine_media_type(file_name):
    # Check if the file has an extension
    if '.' not in file_name:
        return "application/octet-stream"

    # Check the file extension and return the corresponding media type
    if file_name.endswith(".gif"):
        return "image/gif"
    elif file_name.endswith((".jpg", ".jpeg")):
        return "image/jpeg"
    elif file_name.endswith(".png"):
        return "image/png"
    elif file_name.endswith(".pdf"):
        return "application/pdf"
    elif file_name.endswith(".txt"):
        return "text/plain"
    elif file_name.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"

if __name__ == "__main__":
    main()
