# Health Management App

Welcome to the Health Management App! This application helps users monitor and manage their dietary habits by analyzing food images and providing caloric content estimates. Leveraging Google's Gemini Pro Vision model and built with Streamlit, this app offers an intuitive and interactive user experience for effective nutritional tracking.

## 🚀 Features

- **📸 Image-Based Calorie Estimation:** Upload images of your meals to get an estimate of the total calories.
- **🔬 Detailed Nutritional Analysis:** Receive a breakdown of calories for each food item identified in the image.
- **🖥️ User-Friendly Interface:** Easily upload images and view results through a simple and accessible interface.

## 🛠️ Technologies Used

- **🧠 Google Gemini Pro Vision:** For advanced image analysis and food identification.
- **🌐 Streamlit:** For creating an interactive and user-friendly web interface.
- **🐍 Python:** The core programming language used for the app's development.
- **🖼️ Pillow (PIL):** For image handling and display.
- **🔑 dotenv:** For managing configuration data like API keys.

## 📦 Setup and Installation

1. **📥 Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/health-management-app.git
    cd health-management-app
    ```

2. **⚙️ Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **🔧 Set Up Environment Variables:**
    - Create a `.env` file in the project root directory.
    - Add your Google API key in the `.env` file:
      ```plaintext
      GOOGLE_API_KEY=your_google_api_key
      ```

4. **▶️ Run the App:**
    ```bash
    streamlit run app.py
    ```

## 💡 Usage

1. **📝 Input Prompt:** Enter a description or leave it as is for a default prompt.
2. **🖼️ Upload Image:** Choose an image file (jpg, jpeg, png) of your meal.
3. **🚀 Submit:** Click the "Tell me the total calories" button to get the analysis.
4. **📊 View Results:** The app will display the total calories and detailed breakdown of each food item in the image.

## 🤝 Contributing

Contributions are welcome! If you have any suggestions or improvements, please create a pull request or open an issue.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## 🙌 Acknowledgements

- Google for providing the Gemini Pro Vision API.
- Streamlit for their powerful and user-friendly web app framework.

---

Feel free to reach out if you have any questions or need further assistance. Happy tracking!
