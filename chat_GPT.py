import os
import openai

openai.api_key ="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"
question = input("What is question?: ")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": question}
  ]
)

answer = completion.choices[0].message.content
print(answer)