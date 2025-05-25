import openai

openai.api_key = "your-openai-key"

def generate_description(image_url):
    response = openai.ChatCompletion.create(
        model="gpt-4-vision-preview",
        messages=[
            {"role": "system", "content": "You describe product images for e-commerce listings."},
            {"role": "user", "content": f"Describe this image: {image_url}"}
        ]
    )
    return response['choices'][0]['message']['content']