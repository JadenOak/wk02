import requests

# Base URL
url = "https://rickandmortyapi.com/api/character"

# Request API data
response = requests.get(url)
data = response.json()

# Start HTML structure
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rick and Morty Characters</title>
</head>
<body>
"""



# Add character cards
for char in data["results"]:
    html_content += f"""
    <div>
        <img src="{char['image']}" width = "100" alt="{char['name']}">
        <h2>{char['name']}</h2>
        <p><strong>Status:</strong> {char['status']}</p>
        <p><strong>Species:</strong> {char['species']}</p>
        <p><strong>Origin:</strong> {char['origin']['name']}</p>
    </div>
    """
# End character cards

# for char in data["results"]:
#     html_content += f"""
#         <article>
#             <figure>
#                 <img src="{char['image']}" alt="{char['name']}" width="300">
#                 <figcaption>
#                     <h2>{char['name']}</h2>
#                 </figcaption>
#             </figure>
            
#             <section>
#                 <h3>Character Information</h3>
#                 <ul>
#                     <li><strong>Status:</strong> {char['status']}</li>
#                     <li><strong>Species:</strong> {char['species']}</li>
#                     <li><strong>Gender:</strong> {char['gender']}</li>
#                     <li><strong>Origin:</strong> {char['origin']['name']}</li>
#                     <li><strong>Last Known Location:</strong> {char['location']['name']}</li>
#                 </ul>
#             </section>
            
#             <section>
#                 <h3>Data Source</h3>
#                 <p>
#                     <a href="{char['url']}" target="_blank">
#                         View character data from Rick and Morty API
#                     </a>
#                 </p>
#             </section>
#         </article>
#     """


# html_content += """
# </body>
# </html>
# """
# End HTML structure

# Write to HTML file
with open("rick_and_morty.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML file created: rick_and_morty_strong.html")

