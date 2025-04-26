import os
import uuid 
# groq api
from groq import Groq
# md 2 pdf 
import markdown2
from weasyprint import HTML, CSS
from markdown_pdf import MarkdownPdf, Section
# markdown 
from markitdown import MarkItDown


def pdfToMarkdown(_pdf):
    md = MarkItDown(enable_plugins=False) # Set to True to enable plugins
    result = md.convert(_pdf)
    markdown = result.text_content
    return markdown

def completion(_prompt, _model="llama-3.3-70b-versatile"): 
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"{_prompt}",
            }
        ],
        model=_model,
    )

    return (chat_completion.choices[0].message.content)


def pdf_completion(_prompt, _pdf, _model="llama-3.3-70b-versatile"):
    context = pdfToMarkdown(_pdf)
    
    system_prompt = """


# 🎯 Academia (Direct Expert Mode)

You are **Academia** (pronounced *Academia-yah*), a highly capable and ethical AI specialized in providing comprehensive and accurate support for academic tasks and homework across all subjects and levels.

**Your mission:**  
Provide clear, detailed, and structured academic answers **without introductory or concluding remarks**.  
No greetings, no encouragements, no direct conversation with the user.  
Only pure, complete, educational content.

---

### 🛠 Guidelines:

1. **Step-by-Step Solutions:**  
For problem-solving tasks (math, physics, coding, etc.), provide detailed, logical steps and final answers without any user interaction.

2. **Thorough Explanations:**  
For conceptual questions (history, science, economics, etc.), give complete, objective explanations directly.

3. **Strictly No Conversation:**  
- Do not say "Je vais vous aider..." or "N'hésitez pas à me demander..."
- Do not conclude with motivational phrases or invitations.
- Do not refer to yourself or the user.

4. **Highly Accurate and Neutral:**  
Present correct and unbiased information. Cite references or formulas if relevant.

5. **Format for Professional Readability:**  
Use **headings, bullet points, numbered steps, tables**, etc., where necessary.

6. **Handle Ambiguity Carefully:**  
If information is missing, state assumptions **directly** before proceeding.

7. **Uphold Academic Integrity:**  
Never assist in academic dishonesty.

---

### 📚 Response Structure:

✅ **For problem-solving:**  
- Problem restatement (only if necessary to understand the task)  
- Clear step-by-step resolution  
- Final result

✅ **For conceptual explanations:**  
- Clear definition and explanation  
- Related concepts (optional, if relevant)  
- Examples or applications (optional)

---

# 🚫 Forbidden:
- No greetings
- No "I'm here to help you"
- No concluding encouragements
- No direct communication (talking about "you" or "me")

# ✅ Example (instead of old style):

**Old:**
> Je vais vous aider à résoudre cet exercice de mathématiques...

**New:**
> La résolution de l'équation suivante est :  
> 1. Simplifier les termes...  
> 2. Isoler la variable...  
> 3. La solution est x = 3.

---

# 📢 Final note:
Your style should be **professional, academic, and efficient**, like an expert directly writing a solution in a textbook or professional report.

    """

    template = f"""

    * system promt : \n
    {system_prompt} \n 

    * context : {context} \n
    * question : {_prompt}
    """

    return completion(
        template,
    )

def markdownToPdf(_md):
    # Convert markdown to HTML with table and fenced-code-blocks support
    html_content = markdown2.markdown(_md, extras=["tables", "fenced-code-blocks"])

    # Define a beautiful CSS
    css = CSS(string='''
        body {
            font-family: 'Segoe UI', 'Roboto', 'Arial', sans-serif;
            line-height: 1.6;
            font-size: 14px;
            padding: 10px;
            color: #333;
        }
        .table-wrapper {
            overflow-x: auto;
        }
        table {
            width: 80%;
            table-layout: auto;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 14px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
            overflow-wrap: break-word;
            word-break: break-word;
            white-space: normal;
        }
        th {
            background-color: #f4f4f4;
        }
        h1, h2, h3, h4 {
            color: #222;
        }
        /* STYLE FOR INLINE CODE */
        code {
            background: #f5f5f5;
            padding: 2px 4px;
            border-radius: 4px;
            font-family: monospace;
        }
        /* STYLE FOR CODE BLOCKS */
        pre code {
            background: #f5f5f5;
            display: block;
            padding: 20px;
            overflow-x: auto;
            border-radius: 8px;
            font-size: 13px;
        }
        pre {
            background: #f5f5f5;
            padding: 20px;
            overflow-x: auto;
            border-radius: 8px;
            margin-bottom: 20px;
        }
    ''')

    # Generate a unique PDF name
    pdf_name = f"solution_{uuid.uuid1()}"
    
    # Convert to PDF
    HTML(string=html_content).write_pdf(f"{pdf_name}.pdf", stylesheets=[css])

    print(f"PDF generated: {pdf_name}.pdf")


pdf_ = input("\033[92mPdf absolute path:\033[0m ")   
prompt_ = input("\033[92mPrompt:\033[0m ")           
md = pdf_completion(prompt_, pdf_)
print(md)
markdownToPdf(md)