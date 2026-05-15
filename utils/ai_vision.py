import ollama
import json
import ast

class VisionAgent:
    @staticmethod
    def verify_ui_elements(screenshot_path: str, prompt: str):
    
        with open(screenshot_path, 'rb') as img_file:
            response = ollama.generate(
                model='qwen3.5:4b',
                prompt=f"You are a strict QA assistant. Look at this screenshot: {prompt}. Answer with 'YES' or 'NO' and a short reason.",
                images=[img_file.read()],
                stream=False
            )
        return response['response']

    @staticmethod
    def get_selector(snapshot, element_description):
        prompt = (
            f"Context: Accessibility Tree Snapshot: {snapshot}\n"
            f"Target Element: {element_description}\n\n"
            f"Task: Identify the ARIA role and accessible name.\n"
            f"Constraint: Return role and name consecutively as a python list. No explanation. No markdown code blocks.\n"
            f"Format: ['button', 'Submit']"
        )
        
        response = ollama.generate(
            model='llama3.2:1b',
            prompt=prompt,
            stream=False,
            options={"temperature": 0} # Set temperature to 0 for consistent JSON
        )
        
        raw_text = response.get('response', '').strip()
        print(f"Raw LLM Response: {raw_text}")
        locator_list = ast.literal_eval(raw_text)
        return locator_list