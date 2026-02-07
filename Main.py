import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def research_agent(query):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"system","content":"You are a research agent."},
                  {"role":"user","content":query}]
    )
    return response.choices[0].message.content

def analysis_agent(research_data):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"system","content":"Analyze this logically and clearly."},
                  {"role":"user","content":research_data}]
    )
    return response.choices[0].message.content

def final_agent(research, analysis):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"system","content":"Combine research + analysis into a final answer."},
                  {"role":"user","content":f"Research:\n{research}\nAnalysis:\n{analysis}"}]
    )
    return response.choices[0].message.content

def run_agent(user_input):
    research = research_agent(user_input)
    analysis = analysis_agent(research)
    final = final_agent(research, analysis)
    return {"research": research, "analysis": analysis, "final": final}
