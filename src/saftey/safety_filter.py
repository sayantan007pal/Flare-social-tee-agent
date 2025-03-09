class SafetyFilter:
    def __init__(self):
        # Load blocklists, sensitive topics, and pattern matching rules
        self.initialize_safety_rules()
        
    def check_response(self, ai_response):
        # Run multiple safety checks
        checks = {
            "harmful_content": self.check_harmful_content(ai_response["proposed_response"]),
            "factual_accuracy": self.verify_facts(ai_response),
            "brand_alignment": self.check_brand_alignment(ai_response["proposed_response"]),
            "financial_advice": self.check_financial_advice(ai_response["proposed_response"])
        }
        
        # If any checks fail, reject the response
        if any(not result for result in checks.values()):
            return False, checks
            
        return True, checks