@echo off
echo Generating prompt...
python scripts\generate_prompt.py

echo Running Ollama with LLaMA3.2...
ollama run llama3.2 < prompts\prompt.txt > tests\tests_main.cpp

echo Compiling tests...
g++ -std=c++17 tests\tests_main.cpp -I"D:/libs/googletest/googletest-main/googletest-main/googletest/include" -L"D:/libs/googletest/googletest-main/googletest-main/build/lib" -lgtest -lgtest_main -o test.exe > build_output.log 2>&1

echo Running tests...
.\test.exe >> build_output.log
echo Pipeline complete!
pause
