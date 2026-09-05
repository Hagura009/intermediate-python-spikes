# JSONPlaceholder API Manager (CLI)

A Command Line Interface (CLI) tool developed in Python to explore and query the public REST API [JSONPlaceholder](https://jsonplaceholder.typicode.com/). The system simulates a role-based access control environment (**User** and **Admin**) with permission management.

## 🚀 Project Evolution

This project started as a **Spike** (a fast proof of concept) to explore web service consumption and progressively evolved into a cleaner, more modular architecture.

### Version 1: Spike & Prototyping (`v1_spike.py`)
* **Objective:** Experiment with the `requests` library, manipulate JSON responses, and design the menu navigation logic.
* **Implementation:** Direct handling of endpoints, admin code verification, and manual item limiting by iterating with counters.

### Version 2: Clean Code Refactoring (`v2_refactored.py`)
* **DRY (*Don't Repeat Yourself*) Optimization:** Created the `paginar_universal()` function to reuse pagination logic and exception handling instead of duplicating code for every option.
* **List Slicing:** Replaced manual counters with direct sublists (`posts[:10]`), improving efficiency and readability.
* **Maintainability:** Modular structure that simplifies reading and incorporating new endpoints.

---

## 🛠️ Technologies Used

* **Language:** Python 3
* **Libraries:** `requests` (for HTTP requests)

---

## 📋 Key Features

### 👤 User Mode (Restricted Access)
* View limited to the most recent posts, comments, photos, and albums.
* Access restricted from sensitive or personal profile information.

### 🔑 Admin Mode (Full Access)
* Authentication via identification codes (`admins_ids`).
* Full access to the user list (names, emails, and IDs).
* **Interactive Pagination:** Page-by-page navigation (1 to 10) to browse large data collections without cluttering the terminal.

---

💡 Methodology & Development Notes
AI-Assisted Learning: AI was utilized as an interactive tutor to analyze the initial code (Spike), understand the logic behind refactoring (DRY principle, list slicing, and universal functions), and apply these improvements while preserving the original project structure and variable naming.
   
