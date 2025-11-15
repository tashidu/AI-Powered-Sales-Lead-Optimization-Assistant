import os
from openai import OpenAI
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def score_lead(lead_details: dict) -> int:
    """
    Scores a lead based on the provided details using the OpenAI API.

    Args:
        lead_details: A dictionary containing lead information 
                      (e.g., name, job_title, company).

    Returns:
        An integer score between 0 and 100, or 0 if scoring fails.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logger.warning("OPENAI_API_KEY not found. Returning a default score of 0.")
        return 0

    client = OpenAI(api_key=api_key)

    prompt = f"""
    Based on the following lead information, please score their potential as a customer for an "AI-Powered Sales & Lead Optimization Assistant" product on a scale of 0 to 100. 
    
    Consider factors like their job title (are they in a decision-making role in sales, marketing, or management?), the company they work for, and their potential need for sales automation.

    Lead Information:
    - Name: {lead_details.get('name', 'N/A')}
    - Job Title: {lead_details.get('job_title', 'N/A')}
    - Company: {lead_details.get('company', 'N/A')}

    Please provide only the integer score as your response.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Using a cost-effective model, gpt-4 is also an option
            messages=[
                {"role": "system", "content": "You are an expert lead scoring assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
        )
        
        score_str = response.choices[0].message.content
        # Clean up the response to get only the number
        score = int("".join(filter(str.isdigit, score_str)))
        
        if 0 <= score <= 100:
            logger.info(f"Successfully scored lead {lead_details.get('name')}: {score}")
            return score
        else:
            logger.warning(f"Score {score} is outside the 0-100 range. Returning 0.")
            return 0

    except Exception as e:
        logger.error(f"An error occurred while scoring lead with OpenAI: {e}")
        return 0
