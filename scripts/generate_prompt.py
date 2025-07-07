import yaml


def load_yaml(file_path):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)


def read_file(path):
    with open(path, "r") as f:
        return f.read()


def write_prompt(output_path, content):
    with open(output_path, "w") as f:
        f.write(content)


if __name__ == "__main__":
    # Load instruction YAML
    instructions = load_yaml("prompts/strict.yaml")

    # Load C++ source code
    cpp_code = read_file("src/main.cpp")

    # Prepare prompt
    prompt = f"""You are an AI tool for generating unit tests for C++ code.

Strict instructions:
{yaml.dump(instructions)}

C++ Source Code:
{cpp_code} 
Please generate clean and compilable Google Test unit tests in C++. Just give the code for the test file.
"""

    # Save prompt
    write_prompt("prompts/prompt.txt", prompt)
    print("✅ Prompt saved to prompts/prompt.txt")
    print("Prompt generation complete.")
    print("You can now run the test generation script.")
