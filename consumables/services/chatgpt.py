from openai import OpenAI

IMG_URL = 'https://link.storjshare.io/s/jwow6qthz532jdinka3rp47ybphq/delorian/consumables/photo_5219754633814208532_y.jpg'

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Take all the data from the table and send it to me in JSON format. "
                                         "Let all the keys, even nested ones, be in English, "
                                         "and leave the names of the items in the table in Russian."},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                    }
                },
            ],
        }
    ],
)

print(completion.choices[0].message)