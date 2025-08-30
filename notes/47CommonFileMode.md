# Common File Modes in Python

When working with files in Python, different **modes** determine how the file is opened.  

| **Mode** | **Description**                                                                 |
|----------|---------------------------------------------------------------------------------|
| `"r"`    | **Read (default):** Opens a file for reading. Error if the file does not exist. |
| `"w"`    | **Write:** Opens a file for writing (creates new or overwrites if file exists). |
| `"a"`    | **Append:** Opens a file for writing, data is added at the end of the file.     |
| `"x"`    | **Create:** Creates a new file. Fails if the file already exists.               |
| `"b"`    | **Binary mode:** Used for binary files (e.g., images, videos). Combine with other modes like `"rb"` or `"wb"`. |
| `"t"`    | **Text mode (default):** Used for text files. Can be skipped (e.g., `"rt"` = `"r"`). |

---

## Examples

```python
# Open file for reading
file = open("data.txt", "r")

# Open file for writing (overwrites if exists)
file = open("data.txt", "w")

# Open file for appending
file = open("data.txt", "a")

# Create a new file (error if it already exists)
file = open("newfile.txt", "x")

# Read binary file
file = open("image.png", "rb")

# Write binary file
file = open("output.bin", "wb")
