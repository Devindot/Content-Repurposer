# ♻️ AI Content Repurposing Engine

> **"Transforming a single piece of content into multiple formats with AI."**

**Content Repurposing Engine** is an automated pipeline designed to solve the challenge of manual content distribution. It ingests long-form content (YouTube videos or Blog URLs) and uses **Google Gemini** to intelligently rewrite it for specific social media platforms, ensuring tone consistency and scalability.

![Status](https://img.shields.io/badge/Status-Prototype-blue)
![AI](https://img.shields.io/badge/GenAI-Google%20Gemini-orange)
![Stack](https://img.shields.io/badge/Frontend-Streamlit-red)

## 📖 Abstract
Manual repurposing of content across platforms is time-consuming and inconsistent. This system automates the workflow by fetching text from sources like YouTube transcripts or blog articles and generating platform-specific outputs (Twitter Threads, LinkedIn Posts, Blogs) using Large Language Models (LLMs).

## 🚀 Key Features
* **📺 Multi-Source Ingestion:** Automatically fetches transcripts from **YouTube** videos or scrapes text from **Blog URLs**.
* **🧠 Context-Aware Generation:** Uses **Google Gemini** to analyze context and generate high-quality, platform-native content.
* **⚡ Triple-Output Architecture:**
    * **Twitter Threads:** Concise, engaging hooks with viral structure.
    * **LinkedIn Posts:** Professional tone with appropriate hashtags.
    * **Blog Posts:** Structured, SEO-friendly summaries.
* **🎨 Interactive UI:** Built with **Streamlit** for seamless user interaction and real-time generation.

## 🛠️ Tech Stack
| Component | Technology |
| :--- | :--- |
| **LLM Engine** | Google Gemini (via `google-generativeai`) |
| **Orchestration** | LangChain |
| **Frontend** | Streamlit |
| **Data Fetching** | YouTube Transcript API, BeautifulSoup, Requests |
| **Language** | Python 3.10+ |

## 🏗️ System Architecture
The application follows a linear data pipeline:
1.  **Input:** User provides a URL (YouTube/Blog).
2.  **Extraction:**
    * *YouTube:* Extracts captions via `youtube_transcript_api`.
    * *Web:* Parses HTML via `BeautifulSoup`.
3.  **Processing:** Text is cleaned, normalized, and passed to the LLM.
4.  **Generation:** The AI Engine (Gemini) generates three distinct formats based on custom prompts.
5.  **Output:** Results are displayed in the Streamlit Dashboard.


## 🔧 Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/Devindot/content-repurposer.git](https://github.com/Devindot/content-repurposer.git)
    cd content-repurposer
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment**
    Create a `.env` file in the root directory:
    ```env
    GOOGLE_API_KEY=my_gemini_api_key
    ```

4.  **Run the Application**
    ```bash
    streamlit run App.py
    ```

## 📊 Results
* **Efficiency:** Drastically reduces time spent on copywriting and formatting.
* **Consistency:** Maintains a unified brand voice across different channels.
* **Scalability:** Allows creators to multiply their content output without extra effort.

## 👤 Author
**Devin Thakur**
* **LinkedIn:** [linkedin.com/in/devin-thakur](https://www.linkedin.com/in/devin-thakur/)
* **Email:** devin30.9.2004@gmail.com

---
*Based on the project "Content Repurposing Engine" - Presented by Devin Thakur (23BIT0031)*
