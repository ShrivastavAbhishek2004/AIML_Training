from openai import OpenAI
client = OpenAI(api_key="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")

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)
#hello
print(completion.choices[0].message)