# Job Vacancy Management Program

This project fetches job vacancies from the HH.ru API, saves them to a file, and provides functionalities to manage the data (add, filter, delete). The implementation follows OOP principles and SOLID design patterns.

- **API Interaction**: Includes an abstract class for API connections, with a concrete class to fetch job vacancies from HH.ru.
- **Vacancy Class**: Stores key attributes like job title, salary, description, and link. Supports data validation and salary-based comparison.
- **File Storage**: Implements classes to save and manipulate job data in JSON format. Optionally extendable to CSV, Excel, and TXT formats.
- **User Interface**: A command-line interface allows users to search, sort by salary, and filter by keywords.
- **Extensibility**: Provides a base class for file storage that can be easily extended to use databases or external storage solutions.
- **Test Coverage**: The program is fully tested to ensure functionality.
