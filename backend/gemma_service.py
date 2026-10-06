import os
import json
from google import genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMMA_MODEL", "gemma-4-26b-a4b-it")

client = genai.Client(api_key=API_KEY)


def generate_trip(destination, budget, duration, travel_style, interests):
    prompt = f"""
You are an expert AI travel planner.

Create a realistic and personalized travel itinerary.

Destination: {destination}
Budget in INR: {budget}
Duration: {duration} days
Travel style: {travel_style}
Interests: {", ".join(interests)}

Important:
- Stay within the user's budget as much as reasonably possible.
- Give estimated costs, not guaranteed live prices.
- Do not invent real-time availability.
- Prefer practical routes and realistic travel times.
- Include local experiences.
- Keep the itinerary easy to follow.
- Return ONLY valid JSON.
- Do not use Markdown or code fences.

Return exactly this structure:

{{
  "trip_title": "string",
  "destination": "string",
  "summary": "string",
  "budget": {{
    "transport": 0,
    "stay": 0,
    "food": 0,
    "activities": 0,
    "miscellaneous": 0,
    "total": 0
  }},
  "days": [
    {{
      "day": 1,
      "title": "string",
      "morning": "string",
      "afternoon": "string",
      "evening": "string",
      "estimated_cost": 0
    }}
  ],
  "top_places": [],
  "food_recommendations": [],
  "travel_tips": [],
  "best_time": "string"
}}
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    text = response.text.strip()

    # Remove accidental markdown fences
    if text.startswith("```"):
        text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)