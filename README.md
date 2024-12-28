# speedometer-app
### **Step-by-Step Process to Run the Speedometer App**

1. **Install Prerequisites**:  
   - Install **Python 3.9+** and **pip**.  
   - Install **Node.js** and **npm**.  
   - Install **MySQL** and set up the database.

2. **Set Up the Backend**:  
   - Navigate to the backend folder:  
     ```bash
     cd backend
     ```  
   - Create a virtual environment and activate it:  
     ```bash
     python -m venv venv  
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     ```  
   - Install required Python libraries:  
     ```bash
     pip install -r requirements.txt
     ```  
   - Configure the database connection in the code (e.g., username, password, and database name).  
   - Run the backend server:  
     ```bash
     python app.py
     ```

3. **Set Up the Frontend**:  
   - Navigate to the frontend folder:  
     ```bash
     cd frontend
     ```  
   - Install required npm packages:  
     ```bash
     npm install
     ```  
   - Start the React development server:  
     ```bash
     npm start
     ```

4. **Set Up the Database**:  
   - Open MySQL and create a database:  
     ```sql
     CREATE DATABASE speedometer_db;
     ```  
   - Run the database migration script or create the necessary table using the SQL provided.

5. **Testing the Application**:  
   - Use **Postman** or a similar tool to test the backend endpoints (`/insert` for POST and `/latest` for GET).  
   - Verify real-time updates on the frontend speedometer UI.  

6. **Access the Application**:  
   - Open the frontend in your browser at `http://localhost:3000`.  
   - Ensure both the backend (`http://localhost:5000`) and database are running.  

7. **Troubleshooting**:  
   - If you encounter issues, check the backend and frontend logs for error messages.  
   - Verify database connectivity and credentials.  

