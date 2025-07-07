# 🧪 C++ Unit Test Generator using LLM

This project generates unit tests for C++ applications using a local LLM (Ollama + LLaMA3).

## 🚀 How it Works

1. **Initial Prompt Generation**  
   Generate a prompt using `generate_prompt.py` based on the source code in `src/`.

2. **AI-Based Test Generation**  
   The LLM (LLaMA 3 via Ollama) processes the prompt and generates test cases in `tests/`.

3. **Refinement Phase**  
   A second prompt (`refine_prompt.txt`) is used to clean duplicates, add necessary headers, and improve coverage.

4. **Build & Execute**  
   Tests are compiled using GoogleTest, and the results are stored in `build_output.log`.


## 📁 Folder Structure
- `src/`: Original C++ source
- `tests/`: AI-generated test cases
- `scripts/`: Automation tools
- `prompts/`: Prompt YAML and plain text files
- `build_output.log`: Compilation + execution log

## ✅ Result
Successfully built and ran:
[==========] 2 tests from 2 test suites ran.
[ PASSED ] 2 tests.

## 🔧 Tools Used
- 🦙 Ollama (LLaMA 3.2 model)
- 🧪 GoogleTest (compiled locally)
- 🧠 YAML instruction system

## 🎯 Future Improvements

- [ ] Automate header detection and code context enrichment
- [ ] Integrate test coverage tools (e.g., `gcov`)
- [ ] Add support for classes with external dependencies