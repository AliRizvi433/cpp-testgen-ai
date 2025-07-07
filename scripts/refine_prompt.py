import os
import yaml

# Define paths
log_path = "logs/build_output.log"
prompt_txt_path = "prompts/refine_prompt.txt"
output_yaml_path = "prompts/refine.yaml"

# Read static refine prompt
with open(prompt_txt_path, "r", encoding="utf-8") as f:
    refine_prompt = f.read()

# Read build logs
with open(log_path, "r", encoding="utf-8") as f:
    build_output = f.read()

# Construct YAML content
yaml_data = {
    "instructions": refine_prompt.strip(),
    "build_output": build_output.strip()
}

# Write to refine.yaml
with open(output_yaml_path, "w", encoding="utf-8") as f:
    yaml.dump(yaml_data, f, sort_keys=False)

print(f"✅ refine.yaml created successfully at {output_yaml_path}")
