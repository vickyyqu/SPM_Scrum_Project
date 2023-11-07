
# Skill-Based Role Portal

The Internal Role Listing Application is a user-friendly and centralized platform designed to streamline the application process for various job roles within the company. This application is used by staff members, HR, and Managers & Directors to manage internal role listings and internal career mobility.

Link to GitHub repository:

    https://github.com/joel-teo/SPMG4T2
    


## How to run the application
**0. Clone the GitHub project**

EITHER downloading the zip folder 

    https://github.com/joel-teo/SPMG4T2.git


OR run this command line in your terminal

    gh repo clone joel-teo/SPMG4T2


**1. Start up MAMP / WAMP**

**2. Import the sbrp.sql file (located in database_setup) into localhost/phpmyadmin**

**3. Install required (Python) dependencies**
    
    pip install -r requirements.txt
    
**4. Change working directory to backend**

    cd backend

**5. Run python application**

    python app.py

**6. Open a new terminal**

**7. Install the required (JavaScript) dependencies****

    npm install

**8. Run the application in the development environment**

    npm run dev


## API Documentation

[API Docs Google Folder](https://drive.google.com/drive/folders/1LRD6al02ToTOjql-_mKQAYrCdwxRX_ia)


## Environment Variables

To run this project, you will need to edit the following environment variables to your .env file

`DATABASE_URL`

macOS:
```
DATABASE_URL = 'mysql+mysqlconnector://root:root@localhost:3306/sbrp'
```

Windows:
```
DATABASE_URL = 'mysql+mysqlconnector://root:root@localhost:3306/sbrp'
```


## Used By

This project is used by:

- All-In-One


## Authors

- [@Justin Pansacola](https://www.github.com/JustinPansacola)
- [@Vicky Qu](https://www.github.com/vickyyqu)
- [@Mohammad Fadhli](https://www.github.com/mohammadfadhli)
- [@Jessica Fiore](https://www.github.com/jessicafiore09)
- [@Joel Teo](https://www.github.com/joel-teo)
- [@Goh Zhi Yi](https://www.github.com/zzz-zhiyi)





<!-- # Vue 3 + Vite

This template should help get you started developing with Vue 3 in Vite. The template uses Vue 3 `<script setup>` SFCs, check out the [script setup docs](https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup) to learn more.

## Recommended IDE Setup

- [VS Code](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin). -->
