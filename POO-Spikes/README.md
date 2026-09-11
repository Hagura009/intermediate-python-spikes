# Python OOP Foundations: 6-Part Lab Series

Welcome! This repository is a step-by-step learning journey designed to master Object-Oriented Programming (OOP) in Python. 

It consists of **6 lightweight spikes / proofs of concept**, starting from basic drafts to building a small, functional shopping pseudo-app.

---

## Project Structure & Roadmap

V1: Draft / Initial Spike** — Basic syntax, dictionary operations, and initial class setup.
V2: Encapsulation** — Protecting state and bundling data with methods.
V3: Inheritance** — Reusing code and extending classes.
V4: Polymorphism — Overriding methods and unified interfaces.
V5: Abstraction** — Using abstract classes (`abc`) and hiding implementation details.
V6: Final Pseudo-App** — Combining all OOP pillars into a simple CLI shopping app.

---

## Spike: V1;

This initial draft explores managing categorized items and prices using Python dictionaries inside a simple class.

### Objective
Test basic state management, method calls, and dictionary manipulation within an object.

### Key Concepts Tested
- Class initialization (`__init__`) and attribute storage.
- Dynamic data updates via `dict.update()`.
- Item removal using `dict.pop()`.
- Formatting output with `__str__` and basic loops.
## Spike V2;
##1. Robust Error Handling
Added conditional validation before removing items from the dictionary to prevent runtime KeyError exceptions.

Implemented custom exception raising (ValueError) for invalid numeric inputs in financial operations.

## 2. Encapsulation Implementation
Converted the wallet balance attribute to a private variable (__wallet_balance) to restrict direct external access.

Introduced business logic methods (add_funds and buy_item) to handle balance modifications safely.

## 3. Dynamic Property Calculation
Integrated a property getter (ClientCategory) to calculate the customer tier based on the current balance in real time.

## Encapsulation Architecture in V2
Encapsulation in this implementation isolates internal state and controls how data is modified or retrieved.

### Private State Protection
Variable Scope: The prefix __ applied to __wallet_balance restricts direct attribute mutation from outside the class instance.

State Integrity: External scripts cannot overwrite financial data arbitrarily.

Controlled Access Points
Mutators: Balance changes are only executed through add_funds() and buy_item(). These methods enforce preconditions (checking for negative inputs and validating sufficient balance) before applying state changes.

Accessors: The @property decorator for ClientCategory reads the private balance state to evaluate the tier category without exposing a direct setter method.
## Spike V3;
