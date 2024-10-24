import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from secret_key import openapi_key

os.environ['OPENAI_API_KEY'] = openapi_key

llm = OpenAI(temperature = 0.6)


def generate_name(cuisine):
    #chain 1: restaurant name
    prompt_name = PromptTemplate(
        input_variables = ['cuisine'],
        template = "I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
    )

    name_chain = LLMChain(llm = llm, prompt = prompt_name, output_key ="restaurant_name")

    #chain 2: menu items
    prompt_items = PromptTemplate(
        input_variables = ['restaurant_name'],
        template = """Suggest some menu items for {restaurant_name}. Return it as a comma separated string"""

    )

    food_items = LLMChain(llm = llm, prompt =  prompt_items, output_key = "menu_items")

    chain = SequentialChain(
        chains = [name_chain, food_items],
        input_variables = ['cuisine'],
        output_variables = ['restaurant_name', 'menu_items']
    )

    response = chain({"cuisine" : cuisine})
    return response

if __name__ == "main":
    print(generate_name("Italian"))