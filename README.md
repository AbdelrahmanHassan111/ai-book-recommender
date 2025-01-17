# 📚✨ **AI Book Recommendation System using NLP** ✨📚

🌐 **[Try it Live Here](https://huggingface.co/spaces/Abdelrahman-Hassan-1/Book_Recommendation_System) on HuggingFace 🤗** 🌟

---

## 🌟 Table of Contents 🗂️
- [📖 About the Project](#about-the-project)
- [✨ Features](#features)
- [🚀 Getting Started](#getting-started)
  - [🔧 Prerequisites](#prerequisites)
  - [📥 Installation](#installation)
  - [📂 Download Models and Data](#download-models-and-data)
- [🎮 Usage](#usage)
  - [📚 Get Recommendations](#get-recommendations)
  - [🔍 Examples](#examples)
- [🛠️ Technologies Used](#technologies-used)
- [📁 Project Structure](#project-structure)
- [🤝 Contributing](#contributing)
- [📄 License](#license)
- [👥 Team Members](#team-members)
- [🙏 Acknowledgements](#acknowledgements)
- [📬 Contact](#contact)

---

## 📖 About the Project
The **AI Book Recommender** is an intelligent system designed to help readers find new books based on their interests and previous reads. 📚💡 By leveraging **Natural Language Processing (NLP)** techniques, the system analyzes a vast collection of books to provide personalized recommendations instantly. 🚀

---

## ✨ Features
- **🎯 Precise Matching**: Advanced algorithms analyze thousands of books to find the perfect match.
- **🔍 Smart Search**: Case-insensitive search with intelligent error handling.
- **⚡ Fast Results**: Get instant recommendations in seconds.
- **😊 User-Friendly Interface**: Clean and modern design that's easy to use.
- **🌐 Multi-Language Support**: Processes books in multiple languages.
- **⏱️ Real-Time Processing**: Provides on-the-fly recommendations without delays.

---

## 🚀 Getting Started
Follow these steps to get a local copy up and running. 🏃‍♂️💻

### 🔧 Prerequisites
- 🐍 Python 3.7 or higher
- 📦 `pip` package manager

### 📥 Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AbdelrahmanHassan111/ai-book-recommender.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd ai-book-recommender
   ```
3. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

#### 📦 Requirements:
```txt
gradio==4.19.2
pandas==2.1.4
joblib==1.3.2
scikit-learn==1.5.2
huggingface-hub>=0.19.4
```

### 📂 Download Models and Data
The necessary models and data are hosted on Hugging Face Hub. They will be automatically downloaded when you run the app. 🌐📊

---

## 🎮 Usage

### 🚀 Run the Application
```bash
python app.py
```

### 🌐 Access the Interface
Open your web browser and navigate to:
```
http://localhost:7860
```

### 📚 Get Recommendations
1. Enter the title of a book you enjoyed. 📘
2. Choose the number of recommendations you want (1-10). 🔢
3. Click the **"Get Recommendations"** button. 🖱️
4. Discover new books tailored to your taste! 🎉📚

---

## 🔍 Examples
Here are some example queries you can try:

### 💻 Programming Books
- **Input**: `data structures & other objects using java`
- **Recommended Books**:
  1. 📘 Multicast Sockets: Practical Guide for Programmers
  2. 📙 Data Crunching: Solve Everyday Problems Using Java, Python, and More.
  3. 📗 Java in a Nutshell
  4. 📒 Smalltalk with Style
  5. 📕 The C++ Programming Language

### 📖 Fiction Series
- **Input**: `The Majolica Murders`
- **Recommended Books**:
  1. 📘 Four on the Floor
  2. 📙 Caught Dead
  3. 📗 The Weedless Widow
  4. 📒 The Marriage Casket
  5. 📕 How to Build Outdoor Structures

### 🏛️ Historical Books
- **Input**: `The Eastland Disaster`
- **Recommended Books**:
  1. 📘 Forgotten Chicago
  2. 📙 Mount Carmel and Queen of Heaven Cemeteries
  3. 📗 Chicago's Southeast Side
  4. 📒 St. Charles: Culture and Leisure
  5. 📕 The Great Fire of London 1666

---

## 🛠️ Technologies Used
- **Programming Language**: 🐍 Python
- **Frameworks and Libraries**:
  - 🎨 Gradio: For building the user interface
  - 📊 Pandas: For data manipulation
  - 🔢 NumPy: For numerical computations
  - 🤖 Scikit-learn: For machine learning algorithms (TF-IDF, Cosine Similarity)
  - 📝 NLTK: For Natural Language Processing tasks
  - 💾 Joblib: For model persistence
  - 🌐 Hugging Face Hub: For hosting models and data
- **Deployment Platform**: 🚀 Hugging Face Spaces

---

## 📁 Project Structure
```plaintext
ai-book-recommender/
├── app.py                  # Main application script
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .gitattributes          # Git LFS configuration
```

---

## 🤝 Contributing
Contributions are welcome! 🛠️✨ Please follow these steps:

1. **Fork the Repository**. 🍴
2. **Create a Feature Branch**:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. **Commit Your Changes**:
   ```bash
   git commit -m "Add Your Feature"
   ```
4. **Push to the Branch**:
   ```bash
   git push origin feature/YourFeature
   ```
5. **Open a Pull Request**. 📬

---

## 📄 License
This project is licensed under the **MIT License** - see the LICENSE file for details. 📜

---

## 🙏 Acknowledgements
- 📚 Goodreads for providing the book dataset.
- 🤗 Hugging Face for hosting models and deployment platform.
- 🎨 Gradio Team for the user interface framework.
- 🌟 Open-source Community for the amazing tools and libraries.

---

## 📬 Contact
Feel free to reach out if you have any questions or suggestions! 💌

- **Email**: [abdelrahman.h004@gmail.com](mailto:abdelrahman.h004@gmail.com)
- **GitHub Issues**: Create a new issue on the repository

---

✨ Happy Reading! 📖✨
