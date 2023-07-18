# Card Generator for F-Race

---

### Installation

`pip install -r requirements.txt`

In your .env file

`OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"`

### Utilisation

1. Generate a collection

    `python src/generate.py`

2. Generate image with Midjourney using the scripts

3. Put all images in the images folder of the collection and name thoses like it "1.png"

4. Render all cards of the collection

    `python src/render.py`

5. Upload all the renders with a decentralized tool

6. Update the .json of the collection setting the new ipfs address

7. Upload all the data with a decentralized tool

8. Enjoy!