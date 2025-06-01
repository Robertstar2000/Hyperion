import os
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

# Configure the Gemini API key
# The API key is loaded from the .env file by Flask/dotenv in app.py,
# but it's good practice for this module to be aware of where it expects the key from.
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    print("Warning: GEMINI_API_KEY not found. AI functionality will be impaired.")
    # You might raise an error here or handle it in a way that the app can gracefully degrade.
    # For now, we'll allow the program to continue, and actual calls will fail.
    gemini_model = None
else:
    try:
        genai.configure(api_key=gemini_api_key)
        gemini_model = genai.GenerativeModel(
            model_name="gemini-1.5-flash-latest", # Or another suitable model
            # Example system instruction, can be customized or passed per request
            system_instruction="You are a helpful AI assistant for a research workflow application. Your responses should be informative and directly relevant to the prompts provided, which will often relate to scientific research, writing, and methodology.",
            safety_settings={
                HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
                # Add other categories if needed, but be mindful of safety.
                # BLOCK_NONE is used here for maximum flexibility in a research context,
                # but this should be reviewed for production environments.
            }
        )
        print("Gemini API configured successfully.")
    except Exception as e:
        print(f"Error configuring Gemini API in gemini_client.py: {e}")
        gemini_model = None

async def generate_text_async(prompt: str) -> str:
    """
    Generates text using the Gemini API.
    Args:
        prompt: The prompt to send to the AI.
    Returns:
        The AI's generated text response or an error message.
    """
    if not gemini_model:
        return "Error: Gemini API client is not configured. Check API key."

    try:
        # For chat-based models, you might use start_chat and send_message
        # For simple text generation, generate_content is often used.
        # Adjusting to use generate_content for more direct prompt-response.
        response = await gemini_model.generate_content_async(prompt)

        # Ensure response.text is accessed correctly
        # Based on Gemini API, the text might be in response.parts[0].text if it's a multi-part response,
        # or directly in response.text if it's simpler.
        # Checking common ways to access text, might need adjustment based on actual API response structure.
        if response.parts:
             return "".join(part.text for part in response.parts if part.text) # Concatenate text from all parts
        elif hasattr(response, 'text') and response.text: # Check if response.text exists and is not None
             return response.text
        else:
            # Fallback or error if text cannot be extracted
            # Log the full response for debugging if text is not found where expected
            print(f"Warning: Could not extract text from Gemini response. Full response: {response}")
            return "Error: Could not extract text from AI response."

    except Exception as e:
        print(f"Error during Gemini API call: {e}")
        return f"Error generating text: {str(e)}"

# Example usage (optional, for direct testing of this module if run standalone)
if __name__ == '__main__':
    import asyncio

    async def main():
        if not gemini_api_key:
            print("Cannot run example: GEMINI_API_KEY not set in environment.")
            return

        test_prompt = "Explain the concept of a hypothesis in 100 words."
        print(f"Sending test prompt: '{test_prompt}'")
        response = await generate_text_async(test_prompt)
        print(f"Received response:\n{response}")

    asyncio.run(main())
