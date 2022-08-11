import notion.client from NotionClient 

client = NotionClient(token_v2="dc80caaff4944fb035da7a05cef758eb33f6e652010a19103a0b03c70ab755d6030575e93071cde943d19d3d27753d7d7a00911ffad728785d0b8e339cd880c5227d1343c973e984da3bf7613ac2")

page = client.get_block("https://www.notion.so/78b9beca3c5a4b009e8b04c238dac688?v=654f1df845064563be6ca7c9bcb73c18")

print("The old title is:", page.title)
