# Academia AI PDF Generation

🚀 **Academia AI PDF Generation** is a Python project that takes an input **PDF**, extracts its content into **Markdown**, combines it with a **prompt**, generates a **high-quality AI academic answer**, and finally converts it back into a **nicely styled PDF** — automatically.

This tool is optimized for academic tasks and produces clean, professional results.

---

## ✨ Features

- 🧠 **Academia Mode:**  
  Specialized expert AI instructions for academic-style outputs (no greetings, no conclusions, no small talk).
  
- 📄 **PDF to Markdown Conversion:**  
  Quickly extracts and cleans content from existing PDFs.

- 📝 **Markdown to AI Completion:**  
  Combines extracted text and your prompt into a context-aware query.

- 📚 **Markdown to Beautiful PDF:**  
  Nicely styled PDFs using professional fonts, table styling, and code block highlighting.

- 🔒 **Secure API Usage:**  
  Uses `GROQ_API_KEY` from environment variables for secure API access.

---

## 📦 Requirements

```bash
pip install groq markdown2 weasyprint markdown-pdf markitdown
```

> **Note:**  
> `weasyprint` may require extra system libraries depending on your OS (like `cairo`, `pango`, `gdk-pixbuf`, etc.).

---

## ⚙️ How it Works

```bash
$ python main.py
```

You'll be prompted to:

- **Enter the absolute path of your PDF**
- **Enter your academic prompt**

Example:

```
Pdf absolute path: /home/user/documents/chapter1.pdf
Prompt: Summarize the key concepts from the uploaded chapter with examples.
```

Then:

- It reads your PDF ➡️ turns it into Markdown
- It builds a structured system prompt + your context
- It asks the Groq AI (using LLaMA 3.3 70b Versatile model)
- It formats the AI answer and saves it as a **new PDF**.

---

## 🧠 System Prompt

Academia Mode is designed to:

- Provide **detailed step-by-step solutions**
- Use **clear, professional formatting** (titles, lists, tables)
- **Avoid any direct conversation** (no greetings, no "I can help you...")
- Stay **strictly educational** and **neutral**

---
## 📁 Project Structure

| File | Purpose |
|:---|:---|
| `chat-pdf.py` | Main script for the full pipeline |
| `README.md` | Project documentation |

---

## 🔑 Setting up the API Key

You must set your **GROQ API Key** as an environment variable:

```bash
export GROQ_API_KEY=your_groq_api_key_here
```

Or create a `.env` file and load it manually if needed.

---

## 🛡️ Important Notes

- This project uses the **Groq** API with the **LLaMA 3.3 70b Versatile** model.
- It is intended for **personal**, **educational**, and **academic** use.
- It **does not** assist in academic dishonesty or direct cheating.

---

## ✨ Author

**[Mohamed Amine BAHASSOU](https://github.com/Medamine-Bahassou)**  
Passionate about AI, automation, and academic tools. 🚀

---

# 🚀 Ready to turn any academic content into perfect PDFs automatically!
