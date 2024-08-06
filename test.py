def format_yaml_to_markdown(yaml_string):
  """
  Formats a YAML string to a markdown code block.

  Args:
      yaml_string: The YAML string to format.

  Returns:
      A string representing the YAML string in a markdown code block.
  """
  lines = yaml_string.splitlines()
  indented_lines = [f"  {line}" for line in lines]
  return f"`yaml\n{''.join(indented_lines)}\n`"

# Example usage
yaml_string = b"jenkins:\n  tools:\n    nodejs: 14.2.0\n\build:\n"
formatted_string = format_yaml_to_markdown(yaml_string.decode('utf-8'))
print(formatted_string)