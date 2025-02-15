from pathlib import Path
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


def main():
    folder_path = Path("data_md/")
    md_files = list(folder_path.glob("*.md"))
    total_questions = 0
    question_count = 0
    final = ""
    id_file_count = 0
    for file_md in md_files:
        with open(file_md, "r", encoding="utf-8") as file:
            content = file.read()
            if question_count < 25:
                question_count += 1
                final += content + "\n"
            else:
                total_questions += question_count
                print(f"tokens used: {count_tokens(final)}")
                id_file_count += 1
                with open(f"part{id_file_count}.md", "w", encoding="utf-8") as file:
                    file.write(final)
                question_count = 0
                final = ""
    print(f"Total questions on files: {total_questions}")


if __name__ == "__main__":
    main()
