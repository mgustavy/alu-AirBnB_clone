
# AirBnB Clone - Console

# Overview

The AirBnB Clone is a command-line interface (CLI) application for managing an AirBnB-like system. This project allows users to interact with different models (User, State, City, Place, Amenity, Review) to create, show, update, destroy, and list instances of these models.

# Features

- **Create**: Instantiate new objects and save them to a JSON file.
- **Show**: Display the string representation of an instance by its class and ID.
- **Destroy**: Delete an instance by its class and ID.
- **All**: List all instances of a given class, or all instances if no class is specified.
- **Update**: Update attributes of an instance or add new attributes.

# Usage

The CLI interface is implemented using Python's `cmd` module. The application provides several commands to interact with the models.

# Commands

- **`quit`**: Exit the program.
- **`EOF`**: Exit the program when End Of File (EOF) is reached.
- **`create <class_name>`**: Create a new instance of the specified class and print its ID. Classes include `BaseModel`, `User`, `State`, `City`, `Amenity`, `Place`, and `Review`.
- **`show <class_name> <id>`**: Display the string representation of an instance of the specified class with the given ID.
- **`destroy <class_name> <id>`**: Delete the instance of the specified class with the given ID.
- **`all`**: Display string representations of all instances or all instances of a specified class.
- **`update <class_name> <id> <attribute_name> <attribute_value>`**: Update an attribute of the instance with the specified class and ID. You can also use `update <class_name> <id> <dictionary>` to update multiple attributes.

# Example

```shell
(hbnb) create User
# Output: <user_id>

(hbnb) show User <user_id>
# Output: <User object representation>

(hbnb) update User <user_id> email "example@example.com"
# Updates the email attribute of the User object

(hbnb) all
# List all instances
```

# Installation

1. **Clone the repository**:
   ```shell
   git clone https://github.com/yourusername/airbnb_clone.git
   cd airbnb_clone
   ```

2. **Run the program**:
   ```shell
   python3 console.py
   ```


# Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your proposed changes. Make sure to adhere to the code style and include appropriate tests for your changes.

License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.