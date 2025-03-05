# Gym Database App

## Description
The **Gym Database App** is a comprehensive application designed to manage and streamline gym operations, including member registration, workout tracking, class scheduling, and payment management. This app helps gym owners, trainers, and members maintain an organized and efficient fitness experience.

## Features
- **Member Management**: Register, update, and manage member profiles.
- **Workout Tracking**: Log exercises, track progress, and set fitness goals.
- **Class Scheduling**: Book and manage fitness classes with real-time availability.
- **Trainer Assignments**: Assign trainers to specific members and classes.
- **Attendance Tracking**: Monitor check-ins and class participation.


## System Overview
The Gym Database App supports different user roles with specific functionalities:

### **Admin**
- Logs in and manages the system.
- Manages gym **equipment**, **employees**, **managers**, and **supplies**.
- Can **add, update, and remove** records for employees and managers.
- Controls **equipment inventory** by adding and updating entries.
- Handles **supplies management** by updating stock records.

### **Client**
- Logs in and navigates to their dashboard.
- **Books fitness classes** and retrieves class details.

### **Restricted User**
- Logs in and accesses limited functionality.
- **Manages room bookings**, including making reservations and cancellations.
- Views and updates equipment conditions.
- Checks **weekly room schedules**.

## Technologies Used
- **Backend**: Python
- **Database**: SQL (MySQL)

## Usage
- Open the app and log in.
- Register new members or update existing profiles.
- Book classes, manage schedules, and track workouts.

## Use Case Scenarios
### **1. Admin Managing Employees**
- Logs in as Admin.
- Navigates to the **Employees Page**.
- Clicks **Add Employee**, fills in details, and submits.
- The system updates the **database** with the new employee record.

### **2. Client Booking a Class**
- Logs in as a Client.
- Clicks the **Class Button** to view available sessions.
- Selects a class and confirms the booking.
- The system updates the **class schedule database**.

### **3. Restricted User Booking a Room**
- Logs in as a Restricted User.
- Clicks the **Room Button** to check availability.
- Selects a room and books it.
- The system updates the **room booking database**.



