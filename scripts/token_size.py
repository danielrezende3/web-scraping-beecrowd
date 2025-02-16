import tiktoken


def count_tokens(text: str, model: str = "o3") -> int:
    prompt = """Dado 50 problemas de programação competitiva em um arquivo md, separado por # problema [id], 

Gere um arquivo CSV no formato  id_problema, tag onde  id_problema representa a identificação do problema e tag são os tópicos de algoritmos necessários para resolvê-lo. Separe as tags por espaços. Considere que todos os problemas são de matemática, o interesse é em qual subtópico é cada questão. Use um conjunto de tags relevante para cada problema."""
    # Initialize the encoding for the specified model
    encoding = tiktoken.encoding_for_model(model)
    # Encode the text into tokens
    tokens = encoding.encode(text + prompt)
    # Return the number of tokens
    return len(tokens)


prompt = """Dado 50 problemas de programação competitiva em um arquivo md, separado por # problema [id], 

Gere um arquivo CSV no formato  id_problema, tag onde  id_problema representa a identificação do problema e tag são os tópicos de algoritmos necessários para resolvê-lo. Separe as tags por espaços. Considere que todos os problemas são de matemática, o interesse é em qual subtópico é cada questão. Use um conjunto de tags relevante para cada problema."""

# Example usage
with open("part1.md", "r", encoding="utf-8") as file:
    complete_prompt = prompt + file.read()
model = "o3"  # Replace with the model you're using
num_tokens = count_tokens(complete_prompt, model)
print(f"Number of tokens: {num_tokens}")
