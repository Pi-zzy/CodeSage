# CodeSage

CodeSage is an AI-powered automated code review system specifically designed for evaluating and providing feedback on daily programming exercises. The system automatically detects newly submitted code, performs multi-dimensional analysis, and provides detailed review reports.

## 📝 How to Submit Daily Code
**Before participating, you need to contact the repository owner to add your email to the collaborator list, so you can directly push to the main repository. Please do not break the repository with incorrect submissions!**

### 1. Navigate to the Corresponding Date Folder
Each day’s programming exercise is placed in a separate folder named in the format `YYYYMMDD`, e.g., `20250121`. Navigate to the folder for the specific date.

```bash
cd 20250121
```

### 2. Read the Problem Statement
Inside the folder for the specific date, there is a `README.md` file that contains the problem description and requirements for that day’s exercise. Please read this file carefully to understand the problem and the goal of the exercise.

![49a373fabe6e5c3340a11ebed988bfc2](https://github.com/user-attachments/assets/52a28e20-9e0e-4950-b271-5bbfcc9f3eaa)

```bash
cat README.md
```

### 3. Submit Code to the `codes` Folder
In the `codes` folder, name your code file using your initials (pinyin abbreviation). For example, if your name is Zhang San, you can name your C code as `zs.c`, Python code as `zs.py`, or Java code as `zs.java`.

![image](https://github.com/user-attachments/assets/dfd0df72-819f-4d8d-877f-4ed12593bad1)

Click the upload button, and you can either upload your file or directly edit it on GitHub, such as `zzy.cpp`, `zzy.py`, `zzy.java` are all valid file names.

![image](https://github.com/user-attachments/assets/173fbb92-e753-4669-84f2-7e4383dac9f7)

Make sure the code runs successfully and solves the problem requirements before submitting it to the `codes` folder.

### 4. Review Report Generation
Once the code is submitted, the system will automatically perform a code review. The review results will be generated in the `reviews` folder with filenames corresponding to the code files, for example, `zs_review.md`.

You can view the review report to see feedback on code style, problem-solving approach, correctness, and improvement suggestions.

---

## 📋 Features

- 🤖 Automated code review and scoring
- 📊 Multi-dimensional code analysis (code style, problem-solving approach, correctness)
- ⏰ Automatically checks for new submissions every hour
- 📝 Independent review reports
- 🔄 Supports multiple programming languages (C, C++, Python, Java)

## 📁 Repository Structure

```
├── YYYYMMDD/              # Daily exercise folder
│   ├── README.md         # Problem statement
│   ├── codes/           # Code folder
│   │   ├── xxx.c
│   │   ├── xxx.cpp     
│   │   ├── xxx.py      
│   │   └── xxx.java    
│   └── reviews/        # Review folder
│       ├── xxx_review.md
│       └── ...
├── bot/                 # Review bot code (coming soon...)
│   └── code_review_bot.py
└── README.md           # This file
```

## 📝 Submission Guidelines

### Code File Naming
- Use the initials (pinyin abbreviation) of the author’s name.
- For example: `zs.cpp`, `ls.py`, `ww.java`.

### Review File Format
Each code file will have a corresponding `xxx_review.md` file containing:
- Score (1-10)
- Code style evaluation
- Problem-solving approach analysis
- Correctness evaluation
- Overall evaluation
- Improvement suggestions

## 🔄 Automated Review Process

1. The system automatically checks for new code submissions every hour.
2. New or updated code is reviewed.
3. A review report is generated and automatically submitted.
4. Review results can be found in the `reviews` folder in the corresponding date folder.

## 📊 Scoring Criteria

The scoring is based on a 1-10 scale, based on the following criteria:

1. **Code Style (30%)**
   - Variable naming conventions
   - Code formatting
   - Comment completeness

2. **Problem-Solving Approach (40%)**
   - Algorithm choice
   - Implementation approach
   - Code efficiency

3. **Code Correctness (30%)**
   - Functionality
   - Boundary handling
   - Exception handling

## 🤝 Contributing

1. Fork this repository.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to your branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Maintainers

- [@Pi-zzy](https://github.com/Pi-zzy)

## ⭐ Acknowledgements

Thanks to all the contributors who have helped with this project!

