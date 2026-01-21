from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_google_genai import ChatGoogleGenerativeAI

# Initialize the LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.7)

def generate_blog_post(content):
    """Generates a blog post from the given content."""
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert content writer. Your task is to transform the provided text into a well-structured, engaging blog post. Use a catchy title, an introduction, clear headings for different sections, and a concluding summary."),
        ("user", "Here is the content:\n\n{input_text}")
    ])
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"input_text": content})

def generate_twitter_thread(content):
    """Generates a Twitter thread from the given content."""
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a social media expert specializing in Twitter. Convert the following content into a compelling Twitter thread of 5-7 tweets. Each tweet must be under 280 characters. Start with a strong hook. Number each tweet (e.g., 1/7, 2/7). Use relevant hashtags at the end of the final tweet."),
        ("user", "Here is the content:\n\n{input_text}")
    ])
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"input_text": content})

def generate_linkedin_post(content):
    """Generates a LinkedIn post from the given content."""
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a professional branding expert. Rewrite the following content as a professional LinkedIn post. The tone should be insightful and authoritative. Use paragraphs for readability, bullet points for key takeaways, and include 3-5 relevant professional hashtags."),
        ("user", "Here is the content:\n\n{input_text}")
    ])
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"input_text": content})