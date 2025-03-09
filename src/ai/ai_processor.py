import google.generativeai as genai

class AIProcessor:
    def __init__(self):
        genai.configure(api_key=os.environ['GEMINI_API_KEY'])
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        
    def process_tweet(self, classified_tweet):
        # Build prompt with context from classification
        prompt = self.build_prompt(classified_tweet)
        
        # Generate response using Gemini model
        response = self.model.generate_content(prompt)
        
        return {
            "original_tweet": classified_tweet["text"],
            "proposed_response": response.text,
            "confidence": self.calculate_confidence(response)
        }
        
    def build_prompt(self, classified_tweet):
        # Construct prompt with relevant Flare knowledge
        context_docs = "\n".join([doc.page_content for doc in classified_tweet["context"]])
        
        prompt = f"""
        As the Flare Network's autonomous social media agent, you need to respond to this tweet:
        
        TWEET: {classified_tweet['text']}
        
        RELEVANT FLARE KNOWLEDGE:
        {context_docs}
        
        Generate a helpful, accurate response about Flare that addresses the tweet.
        """
        
        return prompt